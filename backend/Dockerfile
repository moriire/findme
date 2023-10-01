FROM python:3.11-bullseye 
WORKDIR backend/
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "-c", "gunicorn_config.py"]
