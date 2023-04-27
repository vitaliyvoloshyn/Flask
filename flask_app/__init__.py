from flask import Flask

app = Flask(__name__)

# импортируем модуль с представлениями для регистрации роутов
from flask_app import views
