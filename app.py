from flask import Flask, render_template

frutas = ['Morango', 'Uva', 'Maçã', 'Laranja']

app = Flask(__name__)

@app.route('/')
def principal():
    name = 'renato'
    age = 47
    return render_template(
        'index.html',
        name=name,
        age=age,
        frutas=frutas
    )

@app.route('/about')
def about():
    return render_template(
        'about.html'
    )

app.run(debug=True)

