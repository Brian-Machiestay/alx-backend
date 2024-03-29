import { createClient } from 'redis';


const client = createClient();


client.on('error', err => console.log(`Redis client not connected to the server: ${err.message}`));
client.on('connect', () => {
  console.log('Redis client connected to the server')
  client.subscribe('holberton school channel');
});
         
// connect to the redis instance
client.connect;

const listener = (channel, message) => {
  console.log(message)
  if (message == 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.disconnect;
    process.exit();
  }
}

client.on('message', listener)
