from datetime import datetime, timedelta
job1 = {"name": "job1", "schedule": "every 1 hour", "last_run": "2026-03-30 8:30", "status": "inactive"}
job2 = {"name": "job2", "schedule": "every day at 6am", "last_run": "2026-03-31 8:30", "status": "active"}
job3 = {"name": "job3", "schedule": "every 2 days", "last_run": "2026-03-29 8:30", "status": "inactive"}
job4 = {"name": "job4", "schedule": "every day at 2pm", "last_run": "2026-04-1 8:30", "status": "active"}
job5 = {"name": "job5", "schedule": "every day at 6pm", "last_run": "2026-04-2 8:30", "status": "inactive"}


jobs = [job1, job2, job3, job4, job5]

def list_job(jobs):
    for job in jobs:
        stat = job["status"]
        if stat == "active":
            print("this job is active: ",job)

def inactive_job(jobs):
    for job in jobs:
        last_run_date = datetime.strptime(job["last_run"], "%Y-%m-%d %H:%M")
        if datetime.now() - last_run_date > timedelta(hours=24):
            print("this job was last run more than 24hrs ago:", job)

def add_job(jobs):
    name = input("enter job name to add: ")
    schedule = input("enter schedule: ")
    last_run = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_job = {"name":name, "schedule": schedule,"last_run": last_run, "status": "active" }
    jobs.append(new_job)
    
def deactivation_f(jobs):
    newput = input("enter job name to deativate ")
    for job in jobs:
        if newput == job["name"]:
            job["status"] = "inactive"
        print(job)


if __name__ == "__main__":
    list_job(jobs)

    inactive_job(jobs)

    add_job(jobs)

    deactivation_f(jobs)


