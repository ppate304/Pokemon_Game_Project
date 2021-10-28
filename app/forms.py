from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from .models import User

class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class PokimonForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    password =StringField('Password', validators=[DataRequired()])
    confirm_password = StringField('Confrim Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(form, field):
        same_email_user = User.query.filter_by(email = field.data).first()
    
        if same_email_user:
            raise ValidationError("Email is Already in Use")