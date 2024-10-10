import redis from 'redis';

const client = redis.createClient()
  .on('error', (err) => console.log('Redis client not connected to the server:', err.stack))
  .on('connect', () => console.log('Redis client connected to the server'));

const channel = 'holberton school channel';

function delay(time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

async function publishMessage(message, time) {
  await delay(time);
  console.log(`About to send ${message}`);
  client.publish(channel, message);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
