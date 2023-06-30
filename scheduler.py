from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from update_tables import update_table, PARAMETER_SETS
from heartbeat import heartbeat
import time

def task_update_events_full():
    print("Starting events_full task")
    update_table(**PARAMETER_SETS["events_full"])
    print("Finished events_full task")

def task_update_groups_full():
    print("Starting groups_full task")
    update_table(**PARAMETER_SETS["groups_full"])
    print("Finished groups_full task")

def task_update_invoices_full():
    print("Starting invoices_full task")
    update_table(**PARAMETER_SETS["invoices_full"])
    print("Finished invoices_full task")

def task_update_students_full():
    print("Starting students_full task")
    update_table(**PARAMETER_SETS["students_full"])
    print("Finished students_full task")

def task_update_events_filter():
    print("Starting events_filter task")
    update_table(**PARAMETER_SETS["events_filter"])
    print("Finished events_filter task")

def task_update_invoices_filter():
    print("Starting invoices_filter task")
    update_table(**PARAMETER_SETS["invoices_filter"])
    print("Finished invoices_filter task")  

def task_update_students_filter():
    print("Starting students_filter task")
    update_table(**PARAMETER_SETS["students_filter"])
    print("Finished students_filter task")

def task_update_leads_full():
    print("Starting leads_full task")
    update_table(**PARAMETER_SETS["leads_full"])
    print ("Finished leads_full task")

if __name__ == "__main__":
    executors = {
        'default': ThreadPoolExecutor(10)
    }
    scheduler = BackgroundScheduler(executors=executors)

    # Add the jobs to the scheduler
    
    # Run every hour at 25 and 55 minutes from 6 to 23 every day
    scheduler.add_job(task_update_groups_full, 'cron', minute='25,55', hour='6-22')
    scheduler.add_job(task_update_events_filter, 'cron', minute='25,55', hour='6-22')
    scheduler.add_job(task_update_invoices_filter, 'cron', minute='25,55', hour='6-22')
    scheduler.add_job(task_update_students_filter, 'cron', minute='25,55', hour='6-22')
    scheduler.add_job(task_update_leads_full, 'cron', minute='25,55', hour='6-22')

    # Run once a day at midnight
    scheduler.add_job(task_update_groups_full, 'cron', minute='0', hour='0')
    scheduler.add_job(task_update_events_full, 'cron', minute='0', hour='0')
    scheduler.add_job(task_update_invoices_full, 'cron', minute='0', hour='0')
    scheduler.add_job(task_update_students_full, 'cron', minute='0', hour='0')
    scheduler.add_job(task_update_leads_full, 'cron', minute='0', hour='0')

    # Run hourly
    scheduler.add_job(heartbeat, 'cron', minute='0', hour='0-23')

    # Start the scheduler
    scheduler.start()
    
    # Keep the script running
    try:
       # Keep the script running
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        print("Shutting down scheduler...")
        scheduler.shutdown()

