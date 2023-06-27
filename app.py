from flask import Flask, flash, render_template, request, redirect, url_for
import urllib.request, json
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

app = Flask(__name__)
frutas = []
registros = []

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cursos.sqlite3"
db.init_app(app)

class cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    descricao = db.Column(db.String(50))
    ch = db.Column(db.Integer)
    def __init__(self, username, descricao, ch):
       self.username = username
       self.descricao = descricao
       self.ch = ch

with app.app_context():
    db.create_all()

# routes - section 5

@app.route('/cursos')
def lista_cursos():
  # page = request.args.get('page', 1, type=int)
  # per_page = 4
  # todos_cursos = cursos.query.paginate(page=1, per_page=4)
  return render_template(
     'cursos.html',
     cursos=cursos.query.all()
   )


@app.route('/novo_curso', methods=['GET', 'POST'])
def cria_curso():
  username = request.form.get('nome')
  descricao = request.form.get('descricao')
  ch = request.form.get('ch')

  if request.method == 'POST':
     if not username or not descricao or not ch:
        flash(' Preencha todos os campos do formulário !!', 'error')
     else:
        curso = cursos(username, descricao, ch)
        db.session.add(curso)
        flash(' Curso criado com sucesso !!', 'error')
        db.session.commit()
        return redirect(url_for('lista_cursos'))

  return render_template(
     'novo_curso.html'
   )

@app.route('/<int:id>/atualiza_curso', methods=['GET', 'POST'] )
def atualiza_curso(id):
   curso = cursos.query.filter_by(id=id).first()
   if request.method == 'POST':
      username = request.form['nome']
      descricao = request.form['descricao']
      ch = request.form['ch']
      cursos.query.filter_by(id=id).update({
         'username': username,
         'descricao': descricao,
         'ch': ch
       })
      flash(' Curso atualizado com sucesso !!', 'error')
      db.session.commit()
      return redirect(url_for('lista_cursos'))

   return render_template(
      'atualiza_curso.html',
      curso=curso
   )

@app.route('/<int:id>/remove_curso')
def remove_curso(id):
   curso = cursos.query.filter_by(id=id).first()
   db.session.delete(curso)
   flash(' Curso deletado com sucesso !!', 'error')
   db.session.commit()
   return redirect(url_for('lista_cursos'))


# routes - section 4

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


if __name__=='__main__':
    app.secret_key = 'unique key'
    app.config['SESSION_TYPE'] = 'filesystem'

app.run(debug=True)

