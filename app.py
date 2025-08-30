from flask import Flask, render_template, request, redirect, url_for
import click

from database import db
from models import Student, Class

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///madrasa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.cli.command('init-db')
def init_db():
    db.create_all()
    click.echo('Initialized the database.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def list_students():
    students = Student.query.all()
    return render_template('students.html', students=students)

@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student = Student(
            name=request.form['name'],
            age=request.form.get('age'),
            level=request.form.get('level'),
            guardian_contact=request.form.get('guardian_contact')
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('list_students'))
    return render_template('add_student.html')

@app.route('/classes')
def list_classes():
    classes = Class.query.all()
    return render_template('classes.html', classes=classes)

@app.route('/classes/add', methods=['GET', 'POST'])
def add_class():
    if request.method == 'POST':
        class_ = Class(
            name=request.form['name'],
            schedule=request.form.get('schedule')
        )
        db.session.add(class_)
        db.session.commit()
        return redirect(url_for('list_classes'))
    return render_template('add_class.html')

if __name__ == '__main__':
    app.run(debug=True)

