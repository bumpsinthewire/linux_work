FROM python:3.9-slim

RUN pip install psutil

COPY process_monitor.py

WORKDIR /app

CMD ["python", "process_monitor.py", "--interval", "2"]
