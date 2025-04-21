import os
from .monitoring import start_monitoring

if os.environ.get('GUNICORN_METRICS') == '1':
    start_monitoring()