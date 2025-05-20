from flask import Blueprint, render_template

employee_bp = Blueprint("employee", __name__)

@employee_bp.route("/")
def employee():
    return render_template("profile_employee.html")

