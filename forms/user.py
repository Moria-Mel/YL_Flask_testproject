from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField,\
    BooleanField, IntegerField, FloatField, DateField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Войти')


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