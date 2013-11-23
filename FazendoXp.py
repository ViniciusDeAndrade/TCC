import requests
import json

from libsaas.services import github

gh = github.GitHub("1caa7d1d703267253a4da559872a5179d0aef170")

login = raw_input('Digite o usuario')

u = requests.get("https://api.github.com/users/" + login)
user = json.loads(u.text)

r = requests.get(user["repos_url"])
repos = json.loads(r.text)

for repo in repos:
    l = requests.get(repo["languages_url"])
    languages = json.loads(l.text)
    
    print repo["name"], ": ", 
    for language in languages:
        print language, 
    
    print
 
nomeArquivo = input('Digite o nome do arquivo')    
arquivo = open( "teste.dat", "w")
arquivo.write(nomeArquivo)
arquivo.close()