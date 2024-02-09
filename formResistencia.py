from wtforms import Form, SelectField, RadioField

class resistencia(Form):
    color1 = SelectField('Color 1',choices=[('black','Negro'), ('brown','Cafe'), ('red','Rojo'), ('orange','Naranja'), ('yellow','Amarillo'), ('green','Verde'),
                                            ('blue','Azul'),
                                            ('violet','Violeta'),
                                            ('grey','Gris'), ('white', 'Blanco')])
    color2 = SelectField('Color 2',choices=[('black','Negro'), ('brown','Cafe'), ('red','Rojo'), ('orange','Naranja'), ('yellow','Amarillo'), ('green','Verde'),
                                            ('blue','Azul'),
                                            ('violet','Violeta'),
                                            ('grey','Gris'), ('white', 'Blanco')])
    color3 = SelectField('Color 3',choices=[('black','Negro'), ('brown','Cafe'), ('red','Rojo'), ('orange','Naranja'), ('yellow','Amarillo'), ('green','Verde'),
                                            ('blue','Azul'),
                                            ('violet','Violeta'),
                                            ('grey','Gris'), ('white', 'Blanco')])
    radio = RadioField(choices=[(0.05,'Dorado'), (0.10,'Plata')])