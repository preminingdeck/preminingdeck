from flask import Blueprint, render_template, redirect, url_for, request


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index-static.html')

@main.route('/', methods=['POST'])
def index_post():
    email = request.form.get('email')
    print(email,email,email,email,email)
    return redirect(url_for('main.index'))