from flask import Flask, render_template, request
import formDistancia
import math
import formResistencia
import formDiccionario
import diccionario

app = Flask(__name__)



@app.route("/cinepolis")
def indexCinepolis():
    return render_template("layoutCinepolis.html")

@app.route("/cinepolis/calcularTotal", methods=["GET","POST"])
def funcion():
    if request.method == "POST":
        
        cantBoletos = int(request.form.get("cantidadBoletos"))
        cantCompradores = int(request.form.get("cantidadCompradores"))
        
        limBoletos = cantCompradores * 7
        
        if cantBoletos <= limBoletos:
            subtotal = cantBoletos * 12
            
            nombre = request.form.get("nombre")
            tarjeta = request.form.get("opcion")   
            
            descuento = 0
            
            if cantBoletos > 5:
                descuento = 0.15
            elif cantBoletos > 2 and cantBoletos < 6:
                descuento = 0.10
            else:
                descuento = 0
            
            if tarjeta == "true":
                descuento = descuento + 0.10
                
            descuentoAplicar = subtotal * descuento
            
            total = subtotal - descuentoAplicar
            datos = {'cantidadBoletos': cantBoletos, 'nombre': nombre, 'cantCompradores': cantCompradores, 'descuento': descuento, 'total': total}
            
            
            return render_template("indexCinepolis.html", datos = datos)
        else:
            return "<h3>No puede comprar mas de 7 boletos por cliente, lo sentimos</h3>"
    else:
        return "metodo no POST"

@app.route("/distancia")
def indexDistancia():
    form_Distancia = formDistancia.distanciaNumeros_Forms(request.form)
    resultado = 0
    return render_template("indexDistancia.html",form = form_Distancia, resultado = resultado)

@app.route("/distancia/calcularDistancia", methods=["GET","POST"])
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


@app.route("/resistencia")
def indexResistencia():
    datos = ''
    result = ''
    form_Resistencia = formResistencia.resistencia(request.form)
    return render_template("indexResistencia.html", form = form_Resistencia, datos = datos, result = result)

@app.route("/resistencia/calcular", methods=["GET","POST"])
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
  
@app.route("/operaciones")
def index():
    return render_template("index.html")

@app.route("/operaciones/basicas", methods=["GET","POST"])
def operacionesBasicas():
    if request.method == "POST":
        
        operacion1 = request.form.get("operacion")
        
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        
        if operacion1 == "suma": 
            return "<h1>La suma es:  {}</h1>".format(str(int(num1) + int(num2)))
        elif operacion1 == "resta":
            return "<h1>La resta es:  {}</h1>".format(str(int(num1) - int(num2)))
        elif operacion1 == "multiplicacion":
            return "<h1>La multiplicacion es:  {}</h1>".format(str(int(num1) * int(num2)))
        elif operacion1 == "division":
            return "<h1>La division es:  {}</h1>".format(str(int(num1) / int(num2)))
    else:
        return '''
        <form action"/multiplicar method="POST">
            <label>N1:</label>
            <input type="text" name="n1" />
            <br>
            <label>N2:</label>
            <input type="text" name="n2" />
            <input type="submit" />
        </form>
        '''

@app.route("/diccionario")
def indexDiccionario():
    form_diccionario = formDiccionario.diccionario_form(request.form)
        
    return render_template('indexDiccionario.html', form = form_diccionario)

@app.route('/diccionario/guardar', methods=["GET","POST"])
def guardarDiccionario():
    if request.method == "POST":
        form_diccionario = formDiccionario.diccionario_form(request.form)
        ing = form_diccionario.ingles.data
        es = form_diccionario.español.data
        
        diccionario.guardar(ing, es)
        return render_template('indexDiccionario.html', form = form_diccionario)
    else:
        print("no entro")


@app.route('/diccionario/buscar', methods = ["GET","POST"])
def buscarDiccionario():
    if request.method == "POST":
        form_diccionario = formDiccionario.diccionario_form(request.form)
        buscar = form_diccionario.buscar.data
        traduccion = form_diccionario.radio.data
        
        if traduccion == 'español':
            print('es')
            valor = diccionario.buscar_valor(buscar)
        elif traduccion == 'ingles':
            print('ing')
            valor = diccionario.buscar_key(buscar)
        
        
        return render_template('indexDiccionario.html', form = form_diccionario, valorEncontrado = valor)

if __name__ =="__main__":
    app.run(debug = True)