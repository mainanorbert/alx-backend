// import { client } from 'kue/lib/redis';
import redis from 'redis';

const client = redis.createClient();

client.on('connect', ()=>{
    console.log('Redis client connected to the server');
});
client.on('error', (error)=>{
    console.log(`Redis client not connected to the server: ${error.message}`);
});

const setNewSchool= (schoolName, value) =>{
    client.set(schoolName, value, (error, reply) =>{
        if (error){
            console.log(error)
        }
        console.log(`Reply: ${reply}`);
    });

}

const displaySchoolValue = (schoolName) =>{
    client.get(schoolName, (error, reply)=>{
        if(error){
            console.log(error)
            return
        }
        console.log(`${reply}`)
    })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');