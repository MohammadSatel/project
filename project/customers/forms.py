#form imports
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

# Flask forms (wtforms) allow you to easily create forms in format:
# variable_name = Field_type('Label that will show', validators=[V_func1(), V_func2(),...])
class CreateCustomer(FlaskForm):
    name = StringField('customer name', validators=[DataRequired()])
    last = TextAreaField('customer last')
    submit = SubmitField('create customer')
