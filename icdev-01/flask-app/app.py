from flask import Flask, Response
from prometheus_client import Counter, Gauge, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter('flask_app_requests_total', 'Общее количество запросов', ['method', 'endpoint'])
ACTIVE_USERS = Gauge('flask_app_active_users', 'Количество активных пользователей')

@app.route('/')
def index():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    ACTIVE_USERS.inc()
    return "Example Flask App to demonstrate Prometheus metrics"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
