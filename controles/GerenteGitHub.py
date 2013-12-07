import requests
import json
import pickle

from libsaas.services import github

#Consulta ao gitHub
class GerenteGitHub:
    
    def getGitHub(self):
        return github.Github("1caa7d1d703267253a4da559872a5179d0aef170")
    #na nuvem
    def getUsuarios(self):  
        gh = self.getGitHub()
        return json.loads(requests.get("https://api.github.com/users").text)
     #na nuvem          
    def getUsuarioSince(self, ID):
        gh = self.getGitHub()
        usuarios = json.loads(requests.get("https://api.github.com/users?since=" + str(ID)).text)
        return usuarios
    
    #na nuvem
    def getLinguagens(self, login):
        gh = self.getGitHub()
        repos = json.loads(requests.get("https://api.github.com/users/" + str(login) + "/repos").text)
        
        dicionarioLinguagens = {}
        
        for repo in repos:
            languages = json.loads(requests.get(repo["languages_url"]).text)
            for lang in languages:
                if lang in dicionarioLinguagens:
                    dicionarioLinguagens[lang] += 1
                else:
                    dicionarioLinguagens[lang] = 1
        return dicionarioLinguagens
    
    def salvarUsuarios(self, usuarios):
        f = open("usuarios.pck", "w")
    
        for user in usuarios:
            pickle.dump(user, f)
        
        f.close()
    #no arquivo
    