import requests
import json
import pickle
from libsaas.services import github

def pegarUsuarios():
    gh = github.GitHub("1caa7d1d703267253a4da559872a5179d0aef170")
    usuarios = json.loads(requests.get("https://api.github.com/users").text)
    return usuarios
                   
def pegarUsuarioSince(ID):
    gh = github.GitHub("1caa7d1d703267253a4da559872a5179d0aef170")
    usuarios = json.loads(requests.get("https://api.github.com/users?since=" + str(ID)).text)
    return usuarios

def salvarUsuarios(usuarios):
    f = open("usuarios.pck", "w")

    for user in usuarios:
        pickle.dump(user, f)
    
    f.close()

def recuperarUsuarios():
    f = open("usuarios.pck", "r")
    usuarios = []

    for i in range(100):
        usuarios.append(pickle.load(f))
    
    return usuarios

def buscarUsuario(login):
    f = open("usuarios.pck", "r")
    
    for i in range(100):
        u = pickle.load(f)
        if u["login"] == login:
            return u

def checarArquivo():
    try:
        f = open("usuarios.pck", "r")
        f.close()
        return True
    except:
        f = open("usuarios.pck", "w")
        f.close()
        return False
    
def linguagens(login):
    gh = github.GitHub("1caa7d1d703267253a4da559872a5179d0aef170")
    repos = json.loads(requests.get("https://api.github.com/users/" + str(login) + "/repos").text)
    
    dicionarioLinguagens = {"JavaScript": 0, "Java": 0, "Ruby": 0, "C": 0, "Erlang": 0}
    
    for repo in repos:
        languages = json.loads(requests.get(repo["languages_url"]).text)
        for lang in languages:
            dicionarioLinguagens[lang] += 1
        break
    return dicionarioLinguagens

print linguagens("mojombo")

