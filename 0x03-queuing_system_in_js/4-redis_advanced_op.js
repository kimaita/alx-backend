import redis from 'redis';

const client = redis.createClient()
  .on('error', (err) => console.log('Redis client not connected to the server:', err.stack))
  .on('connect', () => console.log('Redis client connected to the server'));

const key = 'HolbertonSchools';
client.hmset(key, {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
}, redis.print);

client.hgetall(key, (err, resp) => {
  console.log(resp);
});
