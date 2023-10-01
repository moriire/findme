FROM python:3.11.5-bullseye
COPY requirements.text backend/
RUN pip install -r requirements.txt
WORKDIR backend/
COPY . .
EXPOSE 8000
CMD ["gunicorn -c gunicorn_config.py"]
