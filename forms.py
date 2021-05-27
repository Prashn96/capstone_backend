# from __future__ import print_function
# from flask_wtf import FlaskForm
# from wtforms import TextAreaField, SubmitField
# from wtforms.validators import DataRequired
#
#
# class Todo(FlaskForm):
#
#     content = TextAreaField(validators=[DataRequired()])
#     submit = SubmitField('Submit todo')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class Details(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    imageUri = StringField('imageUri', validators=[DataRequired()])
    # sku_num = StringField('SKU No.', validators=[DataRequired()])
    # batch_num = StringField('Batch No.', validators=[DataRequired()])
    # batch_quantity = StringField('Batch Quantity', validators=[DataRequired()])
    # asn_num = StringField('ASN No.', validators=[DataRequired()])
    # sample_quantity= StringField('Sample Quantity', validators=[DataRequired()])
    send = SubmitField('Submit')