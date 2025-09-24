import psutil
import time
import logging
import argparse

# Set up parsing
parser = argparse.ArgumentParser(description="Monitor CPU Usage")
parser.add_argument('--interval', '-i', type=float, default=5.0, help="Seconds between checks")
parser.add_argument('--threshold', '-t', type=float, default=80.0, help="CPU % for alerts")
args = parser.parse_args()

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/app/process_monitor.log', mode='a'),
        logging.StreamHandler()
        ]
    )
logging.getLogger().handlers[0].stream.reconfigure(write_through=True)

# Parsing validation
try:
    if not args.interval > 0:
        logging.error(f"Invalid interval: {args.interval}. Must be above 0")
        raise
    if not args.threshold > 0:
        logging.error(f"Invalid threshold: {args.threshold}. Must be above 0")
        raise
except TypeError as e:
    logging.error(f"Type error in inputs: {e}")
    raise
except ValueError as e:
    logging.error(f"Value error in input validation: {e}")
    raise
except Exception as e:
    logging.error(f"Unexpected error: {e}")
    raise

# Monitor CPU processes
try:
    while True:
        try:
            cpu = psutil.cpu_percent(interval=1)
            logging.info(f"CPU: {cpu}% at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
            if cpu > args.threshold:
                logging.warning(f"High CPU: {cpu}%")
            time.sleep(args.interval)
        except psutil.Error as e:
            logging.error(f"psutil error: {e}")
            continue
except KeyboardInterrupt:
    logging.info("Stopped")

