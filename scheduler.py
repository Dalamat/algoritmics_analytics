from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from update_tables import update_table, PARAMETER_SETS
from heartbeat import heartbeat
import time
from log_config import logger

def task_update_events_full():
    logger.info("Starting events_full task")
    update_table(**PARAMETER_SETS["events_full"])
    logger.info("Finished events_full task")

def task_update_groups_full():
    logger.info("Starting groups_full task")
    update_table(**PARAMETER_SETS["groups_full"])
    logger.info("Finished groups_full task")

def task_update_invoices_full():
    logger.info("Starting invoices_full task")
    update_table(**PARAMETER_SETS["invoices_full"])
    logger.info("Finished invoices_full task")

def task_update_students_full():
    logger.info("Starting students_full task")
    update_table(**PARAMETER_SETS["students_full"])
    logger.info("Finished students_full task")

def task_update_events_filter():
    logger.info("Starting events_filter task")
    update_table(**PARAMETER_SETS["events_filter"])
    logger.info("Finished events_filter task")

def task_update_invoices_filter():
    logger.info("Starting invoices_filter task")
    update_table(**PARAMETER_SETS["invoices_filter"])
    logger.info("Finished invoices_filter task")  

def task_update_invoices_filter_2():
    logger.info("Starting invoices_filter_2 task")
    update_table(**PARAMETER_SETS["invoices_filter_2"])
    logger.info("Finished invoices_filter_2 task")  

def task_update_students_filter():
    logger.info("Starting students_filter task")
    update_table(**PARAMETER_SETS["students_filter"])
    logger.info("Finished students_filter task")

def task_update_leads_full():
    logger.info("Starting leads_full task")
    update_table(**PARAMETER_SETS["leads_full"])
    logger.info ("Finished leads_full task")

def task_update_budgets_full():
    logger.info("Starting budgets_full task")
    update_table(**PARAMETER_SETS["budgets_full"])
    logger.info ("Finished budgets_full task")

def task_update_payments_full():
    logger.info("Starting payments_full task")
    update_table(**PARAMETER_SETS["payments_full"])
    logger.info ("Finished payments_full task")

def task_update_payments_filter():
    logger.info("Starting payments_filter task")
    update_table(**PARAMETER_SETS["payments_filter"])
    logger.info ("Finished payments_filter task")

if __name__ == "__main__":
    executors = {
        'default': ThreadPoolExecutor(10)
    }
    scheduler = BackgroundScheduler(executors=executors)

    # Add the jobs to the scheduler
    misfire_grace_time = 60 # Specifies time in seconds within which the task can be executed in case of delay for various reasons
    
    # Run every hour at 25 and 55 minutes from 6 to 23 every day
    scheduler.add_job(task_update_groups_full, 'cron', minute='25,55', hour='0-23', misfire_grace_time=misfire_grace_time)
    scheduler.add_job(task_update_events_filter, 'cron', minute='25,55', hour='0-23', misfire_grace_time=misfire_grace_time)
    scheduler.add_job(task_update_invoices_filter, 'cron', minute='25,55', hour='0-23', misfire_grace_time=misfire_grace_time)
    scheduler.add_job(task_update_invoices_filter_2, 'cron', minute='25,55', hour='0-23', misfire_grace_time=misfire_grace_time)
    scheduler.add_job(task_update_students_filter, 'cron', minute='25,55', hour='0-23', misfire_grace_time=misfire_grace_time)
    scheduler.add_job(task_update_leads_full, 'cron', minute='25,55', hour='0-23', misfire_grace_time=misfire_grace_time)
    scheduler.add_job(task_update_budgets_full, 'cron', minute='25,55', hour='0-23', misfire_grace_time=misfire_grace_time)
    scheduler.add_job(task_update_payments_filter, 'cron', minute='25,55', hour='0-23', misfire_grace_time=misfire_grace_time)

    # Run once a day at midnight
    scheduler.add_job(task_update_groups_full, 'cron', minute='0', hour='0', misfire_grace_time=misfire_grace_time)
    scheduler.add_job(task_update_events_full, 'cron', minute='0', hour='0', misfire_grace_time=misfire_grace_time)
    scheduler.add_job(task_update_invoices_full, 'cron', minute='0', hour='0', misfire_grace_time=misfire_grace_time)
    scheduler.add_job(task_update_students_full, 'cron', minute='0', hour='0', misfire_grace_time=misfire_grace_time)
    scheduler.add_job(task_update_leads_full, 'cron', minute='0', hour='0', misfire_grace_time=misfire_grace_time)
    scheduler.add_job(task_update_payments_full, 'cron', minute='0', hour='0', misfire_grace_time=misfire_grace_time)

    # Run hourly
    scheduler.add_job(heartbeat, 'cron', minute='0', hour='0-23', misfire_grace_time=misfire_grace_time)

    # Start the scheduler
    scheduler.start()
    
    # Keep the script running
    try:
       # Keep the script running
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        logger.info("Shutting down scheduler...")
        scheduler.shutdown()

