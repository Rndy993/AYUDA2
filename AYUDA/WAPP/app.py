from flask import Flask
from config import Config
from models import db, User
from routes.auth import auth
from routes.patients import patients
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth)
app.register_blueprint(patients)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
