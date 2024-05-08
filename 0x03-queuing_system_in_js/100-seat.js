import redis from 'redis'
const express = require('express')
const kue = require('kue')
import {promisify} from 'util'
const queue = kue.createQueue()

const client = redis.createClient()
const getAsync = promisify(client.get).bind(client)
const setAsync = promisify(client.set).bind(client)



// let availableSeats = 50
const reserveSeat= async (number)=>{
   await setAsync('available_seats', number) 
}
const getCurrentAvailableSeats = async() =>{
    const availSeats = await getAsync('available_seats')
    return parseInt(availSeats || 0)
};

reserveSeat(50)
let reservationEnabled = true

const app = express()
const port = 1245

app.get('/available_seats', async (req, res)=>{
    const noOfSeats = await getCurrentAvailableSeats()
    return res.json({numberOfAvailableSeats: noOfSeats})
})

app.get('/reserve_seat', async(req, res)=>{

    if (reservationEnabled === false){
        return res.json({ "status": "Reservation are blocked" })
    }
    const job = queue.create('reserve_sear').save((error)=>{
        if (error){
            return res.json({ "status": "Reservation failed" })
        }
        return res.json({ "status": "Reservation in process" })

    })
    job.on('complete', ()=>{
        console.log(`Seat reservation job ${job.id} completed`)

    })
    job.on('failed', (error)=>{
        console.error(`Seat reservation job JOB_ID failed: ${error}`)
    })
})

app.get('/process', async (req, res) => {
    res.json({ "status": "Queue processing" });
    queue.process('reserve_seat', async (job, done) => {
        const availableSeats = await getCurrentAvailableSeats();
        if (availableSeats === 0) {
            reservationEnabled = false;
            return done(new Error('Not enough seats available'));
        }
        const newAvailableSeats = availableSeats - 1;
        await reserveSeat(newAvailableSeats);

        if (newAvailableSeats === 0) {
            reservationEnabled = false;
        }
        done();
    });
});



app.listen(port, ()=>{
    console.log(`Listening to port ${port}`)
})


