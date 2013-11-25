import requests
import json
import pickle

from libsaas.services import github
from Usuario import Usuario

class GerenteUsuario:
    
    #na nuvem
    def getUsuarios(self):  
        gh = github.GitHub("1caa7d1d703267253a4da559872a5179d0aef170")
        usuarios = json.loads(requests.get("https://api.github.com/users").text)
        
        usuarios2 = []
        
        for user in usuarios:
            u = json.loads(requests.get("https://api.github.com/users/" + user["login"]).text)
            if(u.__contains__("location")):
                location = u["location"]
            else:
                location = ""
            repos = json.loads(requests.get(user["repos_url"]).text)
            usuarios2.append(Usuario(user["login"], location, repos))
        
        return usuarios2
     #na nuvem          
    def getUsuarioSince(self, ID):
        gh = github.GitHub("1caa7d1d703267253a4da559872a5179d0aef170")
        usuarios = json.loads(requests.get("https://api.github.com/users?since=" + str(ID)).text)
        return usuarios
    
    def salvarUsuarios(self, usuarios):
        f = open("usuarios.pck", "w")
    
        for user in usuarios:
            pickle.dump(user, f)
        
        f.close()
    #no arquivo
    def recuperarUsuarios(self):
        f = open("usuarios.pck", "r")
        usuarios = []
    
        for i in range(100):
            usuarios.append(pickle.load(f))
        
        return usuarios
    #no arquivo
    def buscarUsuario(self, login):
        f = open("usuarios.pck", "r")
        
        for i in range(100):
            u = pickle.load(f)
            if u["login"] == login:
                return u
    
    def checarArquivo(self):
        try:
            f = open("usuarios.pck", "r")
            f.close()
            return True
        except:
            f = open("usuarios.pck", "w")
            f.close()
            return False
    #na nuvem
    def getLinguagens(self, login):
        gh = github.GitHub("1caa7d1d703267253a4da559872a5179d0aef170")
        repos = json.loads(requests.get("https://api.github.com/users/" + str(login) + "/repos").text)
        
        dicionarioLinguagens = {"JavaScript": 0, "Java": 0, "Ruby": 0, "C": 0, "Erlang": 0}
        
        for repo in repos:
            languages = json.loads(requests.get(repo["languages_url"]).text)
            for lang in languages:
                dicionarioLinguagens[lang] += 1
        return dicionarioLinguagens