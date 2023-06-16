from flask import Flask, render_template, request

# frutas = ['Morango', 'Uva', 'Maçã', 'Laranja']
frutas = []
# notas = {'João': 5.0, 'Ana': 6.0, 'Luciana': 10}
registros = []

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def principal():
  if request.method == 'POST':
     if request.form.get('fruta'):
        frutas.append(request.form.get('fruta'))

  return render_template(
  'index.html',
  frutas=frutas,
)

@app.route('/about', methods=['GET', 'POST'])
def about():
  if request.method == 'POST':
     if request.form.get('aluno') and request.form.get('nota'):
        registros.append({
           'aluno': request.form.get('aluno'),
           'nota': request.form.get('nota')
        })

  return render_template(
      'about.html',
      registros=registros
  )

app.run(debug=True)

