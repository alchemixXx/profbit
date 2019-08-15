from products_app import app
from config import Config
from management.routes import management
from reports.routes import reports
from db import db
import models


def run_app():
    # init_db()
    # create_user()
    app.config.from_object(Config)
    app.register_blueprint(management)
    app.register_blueprint(reports)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.commit()
    return app


if __name__ == '__main__':
    run_app().run(debug=True)
