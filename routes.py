from flask import Flask, render_template, request, url_for, redirect

from todo.models import Board111, db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    return app


app = create_app()


@app.get('/')
def home():
    b_list = Board111.query.all()
    return render_template('board/index.html', b_list=b_list, title='Главная страница')


@app.post('/add')
def add():
    title = request.form.get('title')
    new_board = Board111(title=title)
    db.session.add(new_board)
    db.session.commit()
    return redirect(url_for('home'))


@app.get('/delete/<int:board_id>')
def delete(board_id):
    todo = Board111.query.filter_by(id=board_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))
