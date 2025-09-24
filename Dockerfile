FROM python:3.9-slim

RUN pip3 install psutil

COPY process_monitor.py /app/

WORKDIR /app

CMD ["python3", "process_monitor.py", "--interval", "2"]
