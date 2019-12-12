from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Required


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")


class UserForm(FlaskForm):
    firstname = StringField('Nome: ', validators=[DataRequired()])
    lastname = StringField('Sobrenome: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    


class ClientForm(FlaskForm):
    user_id = IntegerField('User id: ', validators=[DataRequired()])
    data_nasc = StringField('Data de Nascimento: ', validators=[DataRequired()])
    cpf = IntegerField('CPF: ', validators=[DataRequired()])
    estado = StringField('Estado: ', validators=[DataRequired()])
    cidade = StringField('Cidade: ', validators=[DataRequired()])
    bairro = StringField('Bairro: ', validators=[DataRequired()])
    rua = StringField('Rua: ', validators=[DataRequired()])
    numero = IntegerField('Numero: ', validators=[DataRequired()])
    complemento = StringField('Complemento: ', validators=[DataRequired()])
