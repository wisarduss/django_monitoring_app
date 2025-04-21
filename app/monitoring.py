from prometheus_client import CollectorRegistry, Summary, Counter, start_http_server
import time

# Создаем глобальный реестр метрик
REGISTRY = CollectorRegistry(auto_describe=True)

REQUEST_TIME = Summary(
    'request_processing_seconds',
    'Time spent processing request',
    registry=REGISTRY
)
REQUEST_COUNT = Counter(
    'total_requests',
    'Total number of requests',
    registry=REGISTRY
)

def start_monitoring():
    # Запускаем сервер метрик только в главном процессе
    try:
        start_http_server(8002, registry=REGISTRY)
    except OSError:
        # Если порт занят (значит сервер уже запущен), просто продолжаем
        pass

@REQUEST_TIME.time()
def process_request():
    REQUEST_COUNT.inc()
    time.sleep(0.1)