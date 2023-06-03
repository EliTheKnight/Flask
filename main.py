from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    return f'Hello {name}'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def process_login():
    username = request.form["username"]
    password = request.form["password"]

    if username == 'eli' and password == '1234':
        response = redirect(url_for('success', name=username), 200)
    else:
        response = redirect('/', 302)

    return response

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


if __name__ == '__main__':
    app.run(debug=True, port=1111)
