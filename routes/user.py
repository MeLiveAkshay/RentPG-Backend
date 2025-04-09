from flask import request, jsonify

def init_route(app):
    @app.route('/user')
    def user_home():
        return 'Hello from /user!'

    @app.route('/api/v1/login', methods=['POST'])
    def user_login():
        email = request.form.get('email', '')
        password = request.form.get('password', '')

        # Example response
        return jsonify({
            'email': email,
            'password': password,
            'message': 'Login route hit successfully!'
        })
