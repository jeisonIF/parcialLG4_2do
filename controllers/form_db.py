from wtforms import Form,SelectField,PasswordField,validators
from wtforms.fields.core import StringField

class form_label(Form):
    seccion1= StringField('label 1',
                          [validators.Required(message='Dato requerido')
                           ],
                          )
    seccion2= StringField('label 2',[validators.Required(message='Dato requerido')])
    seccion3= StringField('label 3',[validators.Required(message='Dato requerido')])
    seccion4= StringField('label 4',[validators.Required(message='Dato requerido')])
    seccion5= StringField('label 5',[validators.Required(message='Dato requerido')])
    seccion6= StringField('label 6',[validators.Required(message='Dato requerido')])
    seccion7= StringField('label 7',[validators.Required(message='Dato requerido')])