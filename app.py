from flask import Flask, json, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return jsonify({
        'name': 'About Page'
    })

@app.route('/contact', methods=['GET'])
def contact():
   return json.dumps({
        'name': 'Contact Page'
    })
if __name__ == '__main__':
    app.run(port=8000,host='0.0.0.0',debug=True)