import os

from flask import Flask, g, render_template, session

from routes.auth import auth_bp
from routes.quiz import quiz_bp
from routes.stats import stats_bp
from routes.tasks import tasks_bp
from utils.db import close_db, get_db, init_app


def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_mapping(
        SECRET_KEY="study_pilot_secure_key",
        DATABASE=os.path.join(app.instance_path, "study_pilot.db"),
    )

    os.makedirs(app.instance_path, exist_ok=True)
    init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(tasks_bp, url_prefix="/tasks")
    app.register_blueprint(quiz_bp, url_prefix="/quiz")
    app.register_blueprint(stats_bp, url_prefix="/stats")

    @app.before_request
    def load_logged_in_user() -> None:
        user_id = session.get("user_id")
        g.user = None

        if user_id is not None:
            db = get_db()
            g.user = db.execute(
                "SELECT id, username FROM users WHERE id = ?", (user_id,)
            ).fetchone()

    @app.teardown_appcontext
    def teardown_db(exc):
        close_db(exc)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
