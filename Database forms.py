from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,DecimalFiled,SelectFiled
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
    class BillPaymentForm(FlaskForm):
    payee = StringField('Payee', validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[InputRequired()])
    payment_method = SelectField('Payment Method', choices=[('bank', 'Bank Transfer'), ('card', 'Credit      Card')], validators=[DataRequired()])
    submit = SubmitField('Pay')
