from flask import redirect, url_for, session

def redirect_based_on_role():
    user = session.get("user")
    
    if not user:
        # Not logged in
        return redirect(url_for("home.error"))  # or render_template('error.html')

    role = user.get("role")

    if role == "admin":
        return redirect(url_for("admin.profile_admin"))
    elif role == "employee":
        return redirect(url_for("employee.profile_employee"))
    elif role == "user":
        return redirect(url_for("users.profile_user"))
    else:
        # Unknown role
        return redirect(url_for("error.error"))
