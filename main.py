from flask import Flask, request, render_template
app = Flask(__name__)

users = {}

@app.route('/login', methods=["POST"])
def login():
    users.update (request.form)
    return users
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)