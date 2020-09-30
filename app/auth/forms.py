from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField, ValidationError
from wtforms.validators import InputRequired,Email,EqualTo
# import email_validator
from ..models import User

class RegistrationForm(FlaskForm):
    username = StringField('Your username', validators = [InputRequired()])
    email = StringField('Your email address',validators=[InputRequired()])
    password = PasswordField('Password',validators = [InputRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [InputRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Oh no! This username has already been taken')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('Oh no! This email account already exists')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[InputRequired(),Email()])
    password = PasswordField('Password',validators =[InputRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

