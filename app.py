from flask import Flask, render_template
from routes.routes import init_route as init_routes
from routes.profile import init_route as init_profile_routes
from routes.user import init_route as init_user_routes
from routes.main import init_route as init_main_routes

app = Flask(__name__)
init_routes(app)
init_profile_routes(app)
init_user_routes(app)
init_main_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
