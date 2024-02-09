from flask import Flask, render_template, request
import formResistencia

app = Flask(__name__)

@app.route("/")
def index():
    datos = ''
    result = ''
    form_Resistencia = formResistencia.resistencia(request.form)
    return render_template("indexResistencia.html", form = form_Resistencia, datos = datos, result = result)

@app.route("/calcular", methods=["GET","POST"])
def calcular():
    
    form_Resistencia = formResistencia.resistencia(request.form)
    color1 = form_Resistencia.color1.data
    color2 = form_Resistencia.color2.data
    color3 = form_Resistencia.color3.data

    if color1 == 'black':
        colorNo = 0
    elif color1 == 'brown':
        colorNo = 1
    elif color1 == 'red':
        colorNo = 2
    elif color1 == 'orange':
        colorNo = 3
    elif color1 == 'yellow':
        colorNo = 4
    elif color1 == 'green':
        colorNo = 5
    elif color1 == 'blue':
        colorNo = 6
    elif color1 == 'violet':
        colorNo = 7
    elif color1 == 'grey':
        colorNo = 8
    elif color1 == 'white':
        colorNo = 9
        
    if color2 == 'black':
        colorNo2 = 0
    elif color2 == 'brown':
        colorNo2 = 1
    elif color2 == 'red':
        colorNo2 = 2
    elif color2 == 'orange':
        colorNo2 = 3
    elif color2 == 'yellow':
        colorNo2 = 4
    elif color2 == 'green':
        colorNo2 = 5
    elif color2 == 'blue':
        colorNo2 = 6
    elif color2 == 'violet':
        colorNo2 = 7
    elif color2 == 'grey':
        colorNo2 = 8
    elif color2 == 'white':
        colorNo2 = 9
    
    
    if color3 == 'black':
        colorNo3 = 1
    elif color3 == 'brown':
        colorNo3 = 10
    elif color3 == 'red':
        colorNo3 = 100
    elif color3 == 'orange':
        colorNo3 = 1000
    elif color3 == 'yellow':
        colorNo3 = 10000
    elif color3 == 'green':
        colorNo3 = 100000
    elif color3 == 'blue':
        colorNo3 = 1000000
    elif color3 == 'violet':
        colorNo3 = 10000000
    elif color3 == 'grey':
        colorNo3 = 100000000
    elif color2 == 'white':
        colorNo3 = 1000000000
    
    tolerancia = float(form_Resistencia.radio.data)
    
    textoTolerancia = ""
    
    if tolerancia == 0.05:
        textoTolerancia = "Dorado"
    elif tolerancia == 0.10:
        textoTolerancia = "Plata"
        
    mostrar = textoTolerancia + " " + str(tolerancia)
    
    datos = {
        'color1': color1,
        'color2': color2,
        'color3': color3,
        'tolerancia':  mostrar
    }
    
    result = operacion(colorNo, colorNo2, colorNo3, tolerancia)
    
    return render_template("indexResistencia.html", form = form_Resistencia, result = result, datos = datos, textoTolerancia = textoTolerancia) 

# Calculos necesarios
def operacion(x1, x2, x3, tolerancia):
    
    concatenacion = int(str(x1) + str(x2))
    
    valor = float(concatenacion * x3)
    
    va1 = valor * float(tolerancia)
    
    valorMin = valor - va1
    
    valorMax = valor + va1
    
    resultado = {
        'valor': valor,
        'valorMin': valorMin,
        'valorMax': valorMax,
    }
    
    return resultado
    
# metodo de ejecucion
if __name__ =="__main__":
    app.run(debug = True)