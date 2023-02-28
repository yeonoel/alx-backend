import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';

const queue = kue.createQueue();

const jobs = [
    {
        phoneNumber: '4153518743',
        message: 'This is the code 4321 to verify your account',
    },
    {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
    },
];

describe('createPushNotificationsJobs', () => {
    before(function () {
        queue.testMode.enter();
    });

    afterEach(function () {
        queue.testMode.clear();
    });

    after(function () {
        queue.testMode.exit();
    });

    it('display an error message if jobs is not an array passing Number', () => {
        expect(() => {
            createPushNotificationsJobs(2, queue);
        }).to.throw('Jobs is not an array');
    });

    it('display an error message if jobs is not an array passing Object', () => {
        expect(() => {
          createPushNotificationsJobs({}, queue);
        }).to.throw('Jobs is not an array');
      });
    
      it('display an error message if jobs is not an array passing String', () => {
        expect(() => {
          createPushNotificationsJobs('Hello', queue);
        }).to.throw('Jobs is not an array');
      });
    
      it('should NOT display an error message if jobs is an array with empty array', () => {
        const ret = createPushNotificationsJobs([], queue);
        expect(ret).to.equal(undefined);
      });
    
      it('should NOT display an error message if jobs is an array with empty array', () => {
        const ret = createPushNotificationsJobs([], queue);
        expect(ret).to.equal(undefined);
      });
    
      it('create two new jobs to the queue', () => {
        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs.length).to.equal(2);
    
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    
        expect(queue.testMode.jobs[0].data).to.equal({
          phoneNumber: '4153518743',
          message: 'This is the code 4321 to verify your account',
        });
    
        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    
        expect(queue.testMode.jobs[1].data).to.equal({
          phoneNumber: '4153518781',
          message: 'This is the code 4562 to verify your account',
        });
    });
});
