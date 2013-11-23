import requests
import json
import pickle

f = open("usuarios.pck", "w")

from libsaas.services import github

gh = github.GitHub("1caa7d1d703267253a4da559872a5179d0aef170")

u = requests.get("https://api.github.com/users")
users = json.loads(u.text)

usuarios = []

for user in users:
    pickle.dump(user, f)
    
f.close()

#===============================================================================
# r = requests.get(user["repos_url"])
# repos = json.loads(r.text)
# 
# for repo in repos:
#     l = requests.get(repo["languages_url"])
#     languages = json.loads(l.text)
#     
#     print repo["name"], ": ", 
#     for language in languages:
#         print language, 
#     
#     print
#  
#     #login do usuario
#     def usuario(login):
#         return login
#     
# #nomeArquivo = input('Digite o nome do arquivo')    
# #arquivo = open( "teste.dat", "w")
# #arquivo.write(nomeArquivo)
# #arquivo.close()
#===============================================================================
