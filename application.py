from flask import Flask, render_template, url_for, request

application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/contact')
def contact():
    return render_template('contact.html')


@application.route('/about')
def about():
    return render_template('about.html')


@application.route('/gallery')
def gallery():
    return render_template('gallery.html')


@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return f'{request.form["username"]} + {request.form["password"]}'
    else:
        return render_template('login.html')


@application.route("/s/")
def szablon():
    return render_template('n_index.html', user='Stan', email='a@b.su')


@application.route('/new_index')
def new_index():
    return render_template('new_index.html')

@application.route('/base')
def base():
    return render_template('base.html')

@application.route('/menu')
def menu():
    return render_template('menu')


if __name__ == '__main__':
    application.run(debug=True, host='localhost')
