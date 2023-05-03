from flask import render_template, Blueprint
from werkzeug.exceptions import NotFound

users_app = Blueprint(name="users_app",
                      import_name=__name__,
                      url_prefix='/users')
USERS = {
    1: "James",
    2: "Brian",
    3: "Peter",
}


@users_app.route("/", endpoint='list')
def users_list():
    return render_template('users/list.html', users=USERS)


@users_app.route("/<int:user_id>/", endpoint='detail')
def user_details(user_id: int):
    try:
        user_name = USERS[user_id]
    except KeyError:
        raise NotFound(f"User #{user_id} doesn't exist!")
    return render_template('users/detail.html', user_id=user_id,
                           user_name=user_name)
