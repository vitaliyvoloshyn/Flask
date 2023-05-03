from flask import Flask, render_template

from blog.views.users import users_app
from blog.views.articles import articles_app

app = Flask(__name__)


def create_app() -> Flask:
    register_bluprints(app)
    return app

def register_bluprints(app: Flask) -> None:
    app.register_blueprint(users_app)
    app.register_blueprint(articles_app)

@app.route("/")
def index():
    return render_template("index.html")
