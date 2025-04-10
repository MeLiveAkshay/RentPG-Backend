from flask import Flask, render_template
from routes.routes import init_route as init_routes
from routes.profile import init_route as init_profile_routes
from routes.user import init_route as init_user_routes
from routes.main import init_route as init_main_routes
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
init_routes(app)
init_profile_routes(app)
init_user_routes(app)
init_main_routes(app)

# SQLite database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# Initialize database
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)



# Create tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
