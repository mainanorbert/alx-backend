const createPushNotificationsJobs = (jobs, kue) => {
    if (Array.isArray(jobs) === false) {
        console.error('Jobs is not an array');
    }
    jobs.forEach((job) => {
        const myJob = kue.create('push_notification_code_3', job).save((error) => {
            if (error) {
                return
            }
            console.log(`Notification job created: ${myJob.id}`)
            myJob.on('complete', () => {
                console.log(`Notification job ${myJob.id} completed`)
            })
            myJob.on('failed', (error) => {
                console.log(`Notification job ${myJob.id} failed: ${error}`)
            })
            myJob.on('progress', (progress) => {
                console.log(`Notification job ${myJob.id} ${progress}% complete`)
            })
        })

    })

}

export default createPushNotificationsJobs



