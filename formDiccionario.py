from wtforms import Form
from wtforms import StringField, RadioField

class diccionario_form(Form):
    ingles = StringField('Ingles')
    español = StringField('Español')
    mostrar = StringField('Traduccion')
    buscar = StringField('Buscar')
    radio = RadioField(choices=[('español','Español'), ('ingles','Ingles')])