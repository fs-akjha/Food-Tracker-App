from flask import Blueprint, render_template

main=Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/add')
def add():
    return render_template('add.html')

@main.route('/views')
def view():
    return render_template('view.html')