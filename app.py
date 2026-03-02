from flask import Flask, render_template, request
from generador import (
    generar_contrasena,
    generar_contrasena_memorable,
    calcular_entropia,
    evaluar_fortaleza
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    contrasena = ""
    nivel = ""
    entropia = ""

    if request.method == "POST":

        tipo = request.form["tipo"]

        if tipo == "segura":
            contrasena = generar_contrasena()

        else:
            contrasena = generar_contrasena_memorable()

        entropia = calcular_entropia(contrasena)
        nivel = evaluar_fortaleza(contrasena)

    return render_template(
        "index.html",
        contrasena=contrasena,
        nivel=nivel,
        entropia=entropia
    )

if __name__ == "__main__":
    app.run(debug=True)
    