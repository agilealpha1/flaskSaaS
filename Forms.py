from flask_wtf import Form
from wtforms import Form, StringField, SelectField,BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid =StringField('openid',validators=[DataRequired()])
    remember_me =BooleanField('remeber_me', default=False)
    
class MusicSearchForm(Form):
    choices = [('Artist', 'Artist'),
               ('Album', 'Album'),
               ('Publisher', 'Publisher')]
    select = SelectField('Search for music:', choices=choices)
    search = StringField('')