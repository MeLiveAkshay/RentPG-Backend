# routes/profile.py
def init_route(app):
    @app.route('/profile')
    def profile_home():
        return 'Hello from /profile!'
