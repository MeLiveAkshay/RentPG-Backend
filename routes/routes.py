# routes/routes.py
def init_route(app):
    @app.route('/routes')
    def routes_home():
        return 'Welcome to the root route!'
