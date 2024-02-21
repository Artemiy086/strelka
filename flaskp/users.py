from flask import current_app, render_template, Blueprint

app = current_app
bp_users = Blueprint('users', __name__, url_prefix='')


@bp.route("/")
def index():
    return render_template("index.html", cards_list=[])


@bp.route("/card")
def test_card():
    return render_template("card.html")
