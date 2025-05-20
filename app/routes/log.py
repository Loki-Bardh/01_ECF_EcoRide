from flask import Blueprint, render_template

log_bp = Blueprint("log", __name__)

@log_bp.route("/history")
def history():
    return render_template("history.html")

@log_bp.route("/review")
def review():
    return render_template("review.html")
