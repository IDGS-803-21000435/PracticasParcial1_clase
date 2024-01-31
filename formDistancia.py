from wtforms import Form
from wtforms import StringField

class distanciaNumeros_Forms(Form):
    x1 = StringField('X1')
    x2 = StringField('X2')
    y1 = StringField('Y1')
    y2 = StringField('Y2')