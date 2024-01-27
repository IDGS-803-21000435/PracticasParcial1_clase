from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layoutCinepolis.html")

@app.route("/calcularTotal", methods=["GET","POST"])
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
            
        #     return '''
        #         <label>Nombre cliente: {x}</label><br>
        #         <label>Cant. Compradores: {y}</label><br>
        #         <label>Cant. Boletos: {t}</label><br>
        #         <label>Tarjeta: {u}</label><br>
        #         <label>Total a pagar: {g} </label><br>
        #         <label>Descuento aplicado: {z}</label>
        # '''.format(x = nombre, y = cantCompradores, t = cantBoletos, u = tarjeta, g = total, z = descuento)
        else:
            return "<h3>No puede comprar mas de 7 boletos por cliente, lo sentimos</h3>"
    else:
        return "metodo no POST"

if __name__ =="__main__":
    app.run(debug = True) 