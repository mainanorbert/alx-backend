import { expect } from "chai";
import createPushNotificationsJobs from "./8-job";
import kue from 'kue';
// const kue = require('kue')

describe('createPushNotificationsJobs', () => {
    let queue;
    beforeEach(() => {
        queue = kue.createQueue();
        queue.testMode.enter();
    });
    afterEach(() => {
        queue.testMode.clear()
        queue.testMode.exit()
    });
    it('Testing creating two jobs in the queue', () => {
        const jobData = [
            {
                phoneNumber: '4154318781',
                message: 'This is the code 4562 to verify your account'
            },
            {
                phoneNumber: '4151218782',
                message: 'This is the code 4321 to verify your account'
            }
        ]
        createPushNotificationsJobs(jobData, queue)
        expect(queue.testMode.jobs.length).to.be.equal(2)
    });

    it('Throwing an error if not array', () => {
        expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');

    })
    it('display a error message if jobs is not an array', () => {
        createPushNotificationsJobs('not an array', queue);
        expect(queue.testMode.jobs.length).to.equal(0);
    });
})
