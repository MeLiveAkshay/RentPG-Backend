def init_route(app):
    @app.route('/')
    def home():
        return 'Hello from routes!'
