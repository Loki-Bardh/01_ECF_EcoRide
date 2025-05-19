from .home import home_bp
from .users import users_bp
from .admin import admin_bp
from .employee import employee_bp

def register_routes(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(employee_bp, url_prefix="/employee")