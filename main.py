from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/calculonotas', methods=['GET', 'POST'])
def calculoNumeros():
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        numero3 = float(request.form['numero3'])
        asistencia = float(request.form['asistencia'])

        resultado = round((numero1 + numero2 + numero3) / 3, 1)

        check = "reprobado"

        if resultado >= 40 and asistencia >= 75:
            check = "aprobado"

        return render_template('calculonotas.html', resultado=resultado, check=check)
    return render_template('calculonotas.html')


@app.route('/calculocaracteres', methods=['GET', 'POST'])
def nombreyedad():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])

        nombres = [nombre1, nombre2, nombre3]
        if len(set(nombres)) < len(nombres):
            # Si hay duplicados, mostrar un mensaje de error
            return render_template('calculocaracteres.html', error="No se permiten nombres duplicados.")


        nombregrande = str
        caracteres1 = len(nombre1)
        caracteres2 = len(nombre2)
        caracteres3 = len(nombre3)
        caracteresgrande = int
        if caracteres1 >= caracteres2 and caracteres1 >= caracteres3:
            nombregrande = nombre1
            caracteresgrande = caracteres1
        elif caracteres2 >= caracteres1 and caracteres2 >= caracteres3:
            nombregrande = nombre2
            caracteresgrande = caracteres2
        else:
            nombregrande = nombre3
            caracteresgrande = caracteres3
        return render_template('calculocaracteres.html', nombregrande=nombregrande, caracteresgrande=caracteresgrande)
    return render_template('calculocaracteres.html')


if __name__ == '__main__':
    app.run(debug=True)