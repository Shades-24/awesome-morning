"""Scheduling system for daily video delivery."""
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
from datetime import datetime
import config

# Import our application functions
from main import generate_and_send_morning_video

def start_scheduler():
    """Start the scheduler for daily morning videos."""
    scheduler = BlockingScheduler()

    # Parse delivery time (format: "07:00")
    hour, minute = map(int, config.DELIVERY_TIME.split(':'))

    # Set timezone
    timezone = pytz.timezone(config.TIMEZONE)

    # Schedule daily job
    trigger = CronTrigger(
        hour=hour,
        minute=minute,
        timezone=timezone
    )

    scheduler.add_job(
        generate_and_send_morning_video,
        trigger=trigger,
        id='morning_video',
        name='Generate and send morning motivation video',
        replace_existing=True
    )

    print(f"✓ Scheduler started!")
    print(f"  Daily delivery time: {config.DELIVERY_TIME} {config.TIMEZONE}")
    print(f"  Next run: {scheduler.get_jobs()[0].next_run_time}")
    print("\nPress Ctrl+C to stop the scheduler")

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("\n✓ Scheduler stopped")

if __name__ == '__main__':
    start_scheduler()
