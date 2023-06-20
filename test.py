import urllib.request, json


url = 'https://covid19-brazil-api.vercel.app/api/report/v1'
resposta = urllib.request.urlopen(url)
# print(resposta)

dados = resposta.read()
# print(dados)

json_data = json.loads(dados)
print(json_data['data'])
dados_covid = json_data['data']

for i in dados_covid:
  print(i['uf'])
