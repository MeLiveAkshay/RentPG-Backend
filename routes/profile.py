def init_route(app):
    @app.route('/profile')
    def profile():
        return "Hello from profile!"
