from .home import home_bp
from .user import user_bp
from .admin import admin_bp
from .employee import employee_bp
from .search import search_bp
from .error import error_bp
from .log import log_bp

def register_routes(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(employee_bp, url_prefix="/employee")
    app.register_blueprint(search_bp, url_prefix="/search")
    app.register_blueprint(error_bp, url_prefix="/error")
    app.register_blueprint(log_bp, url_prefix="/log")

