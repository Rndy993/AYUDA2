from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = StringField('Role', validators=[DataRequired()])
    submit = SubmitField('Register')

class PatientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=150)])
    lastname = StringField('Lastname', validators=[DataRequired(), Length(min=2, max=150)])
    ci = StringField('CI', validators=[DataRequired(), Length(min=2, max=20)])
    birth_date = StringField('Birth Date', validators=[DataRequired()])
    submit = SubmitField('Save')
