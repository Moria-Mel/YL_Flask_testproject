from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField,\
    BooleanField, IntegerField, FloatField, DateField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Reapeat password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class JobForm(FlaskForm):
    leader_id = IntegerField('ID руководителя', validators=[DataRequired()])
    description = TextAreaField("Описание работы")
    work_size = FloatField('Размер работы в часах', validators=[DataRequired()])
    collaborators = StringField('Члены команды', validators=[DataRequired()])
    is_finished = BooleanField('Работа закончена')
    submit = SubmitField('Отправить работу')