import { createClient } from 'redis';

const client = createClient();

function reserveSeat(number) {
  client.set('available_seats ', number, redis.print);
};

function getCurrentAvailableSeats() {
  const value = await getAsync('available_seats')
}
