from wtforms import Form,SelectField,PasswordField,validators
from wtforms.fields.core import StringField

class form_registro(Form):
    
    hotst= StringField('Hostname',[validators.Required(message='Dato requerido')])
    user= StringField('Usuario',[validators.Required(message='Dato requerido')])
    passw= StringField('Contraseña',[validators.Required(message='Dato requerido')])
    puerto= StringField('Puerto',[validators.Required(message='Dato requerido')])
    baDtos= StringField('Base de datos',[validators.Required(message='Dato requerido')])