from flask import Blueprint, render_template, session

user_bp = Blueprint('user', __name__)

@user_bp.route('/user')
def user_dashboard():
    user_role = session.get('role', 'Guest')
    return render_template('profile_user.html', title="User", user_role=user_role)