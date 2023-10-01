FROM python:3.11.5-bullseye
WORKDIR backend/
COPY requirements.text .
ENTRYPOINT ["python3"]
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000
ENTRYPOINT ["gunicorn"]
CMD ["-c gunicorn_config.py", "0.0.0.0"]
