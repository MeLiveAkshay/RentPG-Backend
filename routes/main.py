from flask import render_template

def init_route(app):
    @app.route('/')
    def main_home():
        return render_template('index.html')
