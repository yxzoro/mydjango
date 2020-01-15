bind = '0.0.0.0:18888'
reload = True
preload_app = False
backlog = 1024
chdir = '/home/michael/github/outsource/ShareProfit/myproject'
timeout = 30
worker_class = 'sync' # gthread/gevent
workers = 5
threads = 8
worker_connections = 2048
daemon = True
pidfile = './gunicorn.pid'
loglevel = 'info'
accesslog = "./log/gunicorn_access.log"
errorlog = "./log/gunicorn_error.log"

# gunicorn -c gunicorn.conf.py myproject.wsgi:application
# ab -n 10000 -c 100 http://127.0.0.1:18888

