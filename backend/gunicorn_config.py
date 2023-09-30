proc_name= "FindMe Project"
wsgi_app = "backend.wsgi:application"
loglevel = "info"
workers = 3
bind = "127.0.0.1:8000"
reload = True
accesslog = errorlog = "gunicorn/dev.log"
capture_output = True
pidfile = "gunicorn/dev.pid"
daemon = True