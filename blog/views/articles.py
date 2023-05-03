from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

articles_app = Blueprint("articles_app", __name__, url_prefix='/articles')
ARTICLES = {
    1: "Flask",
    2: "Django",
    3: "JSON:API"
}


@articles_app.route("/", endpoint="list")
def articles_list():
    return render_template("articles/list.html", articles=ARTICLES)

@articles_app.route("/<int:article_id>", endpoint='detail')
def article_detail(article_id: int):
    try:
        article_name = ARTICLES[article_id]
    except KeyError:
        raise NotFound(f"Article #{article_id} doesn't exist!")
    return render_template('articles/detail.html', article_name=article_name, article_id=article_id)
