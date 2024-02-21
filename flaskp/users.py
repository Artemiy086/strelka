from flask import current_app, render_template, Blueprint


app = current_app
bp_users = Blueprint('users', __name__, url_prefix='')


@bp_users.route("/")
def index():
    return render_template("index.html", cards_list=[])


@bp_users.route("/card")
def test_card():
    return render_template("card.html")
