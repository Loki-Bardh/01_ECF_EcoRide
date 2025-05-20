from flask import redirect, url_for, session

from functools import wraps
from flask import session, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("users.login"))
        return f(*args, **kwargs)
    return decorated_function

def role_redirect():
    user = session.get("user")
    
    if not user:
        # Not logged in
        return redirect(url_for("error.error"))  # or render_template('error.html')

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
    
    
from flask import redirect, render_template, session
from functools import wraps

# Created using ChatGPT and Ducky
def cache_clear(local_cache):
    for item in os.listdir(local_cache):
        item_path = os.path.join(local_cache, item)
        try:
            if os.path.isfile(item_path):
                    os.remove(item_path)  # Remove the file
            elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)  # Remove the directory and its contents
        except Exception as e:
             print(f"Error deleting {item_path}: {e}")


def error(message, code=400):
    """Render message as an error to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("error.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function