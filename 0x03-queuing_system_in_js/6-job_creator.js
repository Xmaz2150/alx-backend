const kue = require('kue');

const jobData = {
  phoneNumber: string,
  message: string,
};

const push_notification_code = kue.createQueue();

const job = push_notification_code.create('push_notification_code', jobData).save((error) => {
  console.log('Notification job failed');
});

console.log(`Notification job created: ${job.id}`);
console.log('Notification job completed');