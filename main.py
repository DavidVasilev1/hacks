from flask_cors import CORS
from hacks_api import app, db

from hacks_api.api.example import todo_bp
from hacks_api.model.examples import init_todos

app.register_blueprint(todo_bp)



@app.before_first_request
def init_db():
    with app.app_context():
        db.create_all()
        init_todos()


if __name__ == "__main__":
    cors = CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./volumes/sqlite.db"
    app.run(debug=True, host="0.0.0.0", port="8199")
