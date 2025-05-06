# routes/employee.py
from flask import Blueprint, render_template, session, redirect, url_for

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/employee')
def employee_dashboard():
    if session.get('role') != 'Employee':
        return redirect(url_for('user.user_dashboard'))
    return render_template('profile_employee.html', title="Employee Dashboard")