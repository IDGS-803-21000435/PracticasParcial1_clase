from flask import Flask, render_template, request
import formDistancia
import math

app = Flask(__name__)

@app.route("/distancia")
def index():
    form_Distancia = formDistancia.distanciaNumeros_Forms(request.form)
    resultado = 0
    return render_template("indexDistancia.html",form = form_Distancia, resultado = resultado)

@app.route("/calcularDistancia", methods=["GET","POST"])
def calcularDistancia():
    form_Distancia = formDistancia.distanciaNumeros_Forms(request.form)
    if request.method == "POST":
        x1 = int(form_Distancia.x1.data)
        x2 = int(form_Distancia.x2.data)
        y1 = int(form_Distancia.y1.data)
        y2 = int(form_Distancia.y2.data)
        
        exponente = 2
        operacion1 = pow((x2 - (x1)), exponente)
        operacion2 = pow((y2 - (y1)), exponente)
        resultado = math.sqrt((operacion1) + (operacion2))
            
        print('X1: {x}, Y2: {y}, X1: {w}, Y2: {s}'.format(x = x1, y = y1, w = x2, s = y2))
        print('resultado: {}'.format(resultado))
        
        
    
    return render_template("indexDistancia.html", form = form_Distancia, resultado = resultado)


if __name__ =="__main__":
    app.run(debug = True) 