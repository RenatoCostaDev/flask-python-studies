from flask import Flask, render_template, request
import urllib.request, json

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

@app.route('/covid')
def covid():
  url = 'https://covid19-brazil-api.vercel.app/api/report/v1'
  resposta = urllib.request.urlopen(url)
  dados = resposta.read()
  json_data = json.loads(dados)
  dados_covid = json_data['data']

  return render_template(
     'covid.html',
     dados_covid=dados_covid
  )

@app.route('/covid-estado/<estado>')
def covid_estado(estado):

  url = f'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{estado}'
  resposta = urllib.request.urlopen(url)
  dados = resposta.read()
  dados_covid = json.loads(dados)

  return render_template(
     'covid_estado.html',
     dados_covid=dados_covid
  )

app.run(debug=True)

