from flask import Blueprint, render_template, session, redirect, url_for

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def admin_dashboard():
    if session.get('role') != 'Admin':
        return redirect(url_for('user.user_dashboard'))
    return render_template('profile_admin.html', title="Admin Dashboard")