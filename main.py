from flask import Flask, render_template, request
import ejercicio

app = Flask(__name__)


@app.route("/ejercicio")
def index():
    ejercicio.ejecucion()
    return '<h1>ejecucion exitosa</h1>'

if __name__ =="__main__":
    app.run(debug = True)