from flask import Blueprint, render_template

error_bp = Blueprint("error", __name__)

@error_bp.route("/")
def error():
    return render_template("error.html")
