# routes/user.py
def init_route(app):
    @app.route('/user')
    def user_home():
        return 'Hello from user route!'
