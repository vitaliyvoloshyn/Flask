from flask import Response

from flask_app import app


@app.route("/")
def index():
    return Response(response="<p>Hello, World!</p>")
