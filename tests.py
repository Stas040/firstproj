from flask import Flask, request
app = Flask(__name__)

users = {"stas": "qazplm"}

@app.route('/')
def index():
    return '<p>Перейдите по ссылке "http://192.168.128.50:5000/login?username=ВАШЕ_ИМЯ&password=ВАШ_ПАРОЛЬ" для авторизации</p>'

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username and password:
        if username not in users:
            users[username] = password
            return f"Пользователь {username} был зарегистрирован. Для входа перейдите по той же ссилке или перезагрузите страницу."
        elif users[username] == password:
            return f"Добро пожаловать хозяин, {username}! \nДля перехода в home используйте \n'http://192.168.128.50:5000/home?username=ВАШЕ_ИМЯ'"
        else:
            return "Неверный пароль"
    else:
        return "Необходимо передать имя пользователя и пароль."

@app.route("/home")
def home():
    username = request.args.get('username')
    if username:
        if username not in users:
            return "Вам нужно авторизаваться по ссилке 'http://192.168.128.50:5000/login?username=ВАШЕ_ИМЯ&password=ВАШ_ПАРОЛЬ'"
        else:
            return f"Hello, {username}!"