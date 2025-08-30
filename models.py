from datetime import date

from database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer)
    level = db.Column(db.String(50))
    guardian_contact = db.Column(db.String(120))

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    schedule = db.Column(db.String(120))

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))

    student = db.relationship('Student', backref='enrollments')
    class_ = db.relationship('Class', backref='enrollments')

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enrollment_id = db.Column(db.Integer, db.ForeignKey('enrollment.id'))
    date = db.Column(db.Date, default=date.today, nullable=False)
    status = db.Column(db.String(10))

