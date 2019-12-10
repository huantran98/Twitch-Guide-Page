from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from .models import User


class LoginForm(FlaskForm):
    '''
    Class handles logging in for existing users. Variables are defined with WTForm fields.
    '''
    username = StringField('Username', render_kw={"placeholder": "Enter Username"}, validators=[DataRequired()])
    password = PasswordField('Password', render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class createAccount(FlaskForm):
    '''
    Class handles registering for new users. Variables are defined with WTForm fields.
    '''
    username = StringField('Username', render_kw={"placeholder": "Enter Username"}, validators=[DataRequired()])
    email = StringField('Email', render_kw={"placeholder": "Enter email"}, validators=[DataRequired(), Email()])
    password = PasswordField('Password', render_kw={"placeholder": "Enter password"}, validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', render_kw={"placeholder": "Re-enter password"}, validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        '''Validates username
        :param username:
        :return: Checks if username is not taken; if taken, prompts user to try again
        '''
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        '''Validates email

        :param email:
        :return: Checks if email is not taken; if taken, prompts user to try again
        '''
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a valid email address.')

class PostForm(FlaskForm):
    '''
    Class handles the creation of new tasks.
    '''
    nameTitle = StringField('nameTitle', validators=[DataRequired()])
    content = TextAreaField('content')
    complete = BooleanField('complete')
    submit = SubmitField('Create')

class mailForm(FlaskForm):
    '''
    Class handles sending messages to other users; used by mes()
    '''
    email = StringField('Email', validators=[DataRequired()])
    subject = StringField('Subject')
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('Send')

class forgotForm(FlaskForm):
    '''
    Class handles request for reset of password; used by resetRequest()
    '''
    email = StringField('Email', render_kw={"placeholder": "Enter Email"}, validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        '''Validates email

        :param email:
        :return: Checks if email is not in the system, prompts user to try again
        '''
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class passwordResetForm(FlaskForm):
    '''
    Class handles the reset of password after user clicks on link.
    '''
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')