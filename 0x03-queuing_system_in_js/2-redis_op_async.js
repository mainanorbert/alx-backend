// import { client } from 'kue/lib/redis';
import redis from 'redis';
import {promisify} from 'util';

const client = redis.createClient();


client.on('connect', ()=>{
    console.log('Redis client connected to the server');
});
client.on('error', (error)=>{
    console.error(`Redis client not connected to the server: ${error}`);
});

const setNewSchool= (schoolName, value) =>{
    client.set(schoolName, value, redis.print)

}

const displaySchoolValue = async (schoolName) =>{
   const getAsync = promisify(client.get).bind(client)
    try{
        const rep = await getAsync(schoolName)
        console.log(`${rep}`)
    }
    catch(error){
        console.error(error)

    }
    
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');