import { createClient  } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
};

function displaySchoolValue(schoolName) {
  client.get(schoolNmae, (err, response) => {
    console.log(response);
  });
};

const key = 'HolbertonSchools';
const fields = ['Portland', 'Seattle', 'NewYork', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2,];

fields.forEach((field, index) => {
  client.hset(key, field, values[index], redis.print);
});

client.hgetall(key, (err, value) => {
  console.log(value);
});
