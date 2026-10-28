import os
from flask import Flask, send_from_directory

app = Flask(__name__)
# Берем путь к папке, где лежит этот скрипт
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    # Отдаем history.html прямо из корня папки
    return send_from_directory(BASE_DIR, 'ff.html')

if __name__ == '__main__':
    # host='0.0.0.0' открывает доступ всем в твоей Wi-Fi сети
    app.run(host='0.0.0.0', port=8000, debug=True)
