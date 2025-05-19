from .home import home_bp
from .user import user_bp
from .admin import admin_bp
from .employee import employee_bp

def register_routes(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(employee_bp, url_prefix="/employee")