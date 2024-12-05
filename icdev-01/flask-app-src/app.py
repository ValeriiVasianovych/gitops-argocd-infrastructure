from flask import Flask, Response, request
from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest
import time

app = Flask(__name__)

REQUEST_COUNT = Counter('flask_app_requests_total', 'Total number of requests', ['method', 'endpoint'])
ACTIVE_USERS = Gauge('flask_app_active_users', 'Number of active users')
REQUEST_DURATION_HISTOGRAM = Histogram('flask_app_request_duration_seconds', 'Histogram for the duration of requests', ['method', 'endpoint'])
REQUEST_DURATION_SUMMARY = Summary('flask_app_request_duration_seconds_summary', 'Summary for the duration of requests', ['method', 'endpoint'])
EXCEPTIONS_COUNT = Counter('flask_app_exceptions_total', 'Total number of exceptions')

@app.route('/')
def index():
    start_time = time.time()
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    ACTIVE_USERS.inc()
    try:
        response = "Example Flask App to demonstrate Prometheus metrics"
        return response
    except Exception as e:
        EXCEPTIONS_COUNT.inc()
        raise e
    finally:
        duration = time.time() - start_time
        REQUEST_DURATION_HISTOGRAM.labels(method='GET', endpoint='/').observe(duration)
        REQUEST_DURATION_SUMMARY.labels(method='GET', endpoint='/').observe(duration)
        ACTIVE_USERS.dec()

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
