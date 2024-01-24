from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/operaciones", methods=["GET","POST"])
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

if __name__ =="__main__":
    app.run(debug = True) 