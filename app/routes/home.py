from flask import Blueprint, render_template, session, redirect, url_for
from app.helpers import role_redirect 

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    return render_template("home.html")

@home_bp.route("/profile")
def profile_redirect():
    # Use helper function to redirect based on user role
    return role_redirect()

@home_bp.route("/login/<role>")
def login(role):
    # Fake login for testing roles: admin, employee, user
    session["user"] = {"username": "testuser", "role": role}
    return redirect(url_for("home.profile_redirect"))
