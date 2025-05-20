from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app.models import User


user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def user():
    return render_template("profile_user.html")

@user_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not contact or not password:
            return error("All fields are required", 400)
        if password != confirmation:
            return error("Passwords do not match", 400)

        if User.query.filter_by(email=contact).first():
            return error("Email already registered", 400)

        new_user = User(email=email, role="user")  # Or allow selection from form
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully. Please log in.")
        return redirect(url_for("user.login"))

    return render_template("profile.html")


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return error("Email and password are required", 403)

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return error("Invalid credentials", 403)

        session["user_id"] = user.id
        session["user_role"] = user.role
        return redirect(url_for("home.profile_redirect"))

    return render_template("profile.html")
