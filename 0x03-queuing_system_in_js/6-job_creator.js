import kue from 'kue';

const queue = kue.createQueue();

const jobFormat = {
  phoneNumber: '54667777',
  message: ''This is the code to verify your account,
};

const queueName = 'push_notification_code';

const job = queue.create(queueName, jobFormat).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  consle.log('Notification completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
}
