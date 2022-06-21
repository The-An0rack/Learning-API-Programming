from flask import Flask

app = Flask(__name__)

@app.route('/user')
def get_user():
    return 'name: Jhon Doe\nemail: john@service.com';

@app.route('/name')
def print_user():
    return 'name: Jhon Doe'

if __name__ == '__main__':
    app.run()