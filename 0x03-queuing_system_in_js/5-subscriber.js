import redis from 'redis';

const client = redis.createClient();


client.on('connect', ()=>{
    console.log('Redis client connected to the server');
});
client.on('error', (error)=>{
    console.error(`Redis client not connected to the server: ${error}`);
});

client.subscribe('holberton school channel')

client.on('message', (channel, msg) =>{
    console.log(`${msg}`)
    if(msg === 'KILL_SERVER'){
        client.unsubscribe('holberton school channel')
        client.quit();
    }
})