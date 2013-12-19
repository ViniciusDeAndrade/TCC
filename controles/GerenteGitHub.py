import requests
import json
import pickle
import os

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
    
    #no arquivo
    def getLinguagensNoArquivo(self, login):
        f_repos = open(login + ".repos.txt", "r")
        repos = pickle.load(f_repos)
        
        dicionarioLinguagens = {}
        
        for repo in repos:
            f_languages = open(login + ".repos." + repo["name"] + ".languages.txt", "r")
            languages = pickle.load(f_languages)
            
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
    
    def salvarRepos(self, usuario):
        gh = self.getGitHub()
        repos = json.loads(requests.get("https://api.github.com/users/" + str(usuario) + "/repos").text)
        
        directoryPath = r'C:\\Users\User\Dropbox\TCC' + r"\\" + usuario
        os.mkdir(directoryPath)
        
        print "Salvando /" + usuario + "/repos.txt"
        f = open(usuario + "/" + usuario + ".repos.txt", "w")
        pickle.dump(repos, f)
        f.close()
        
        for repo in repos:
            self.__salvarRepositorios(usuario, repo)
            
    def salvarReposFaltando(self, usuario, repoInicial):
        gh = self.getGitHub()
        repos = json.loads(requests.get("https://api.github.com/users/" + str(usuario) + "/repos").text)
        
        salva = False
        
        for repo in repos:
            if repo["name"] == repoInicial:
                salva = True
            elif salva == False:
                continue
            
            self.__salvarRepositorios(usuario, repo)
    
    #Refatorei para esse metodo
    def __salvarRepositorios(self, usuario, repo):
        
        #Aqui, pega cada repo individualmente. Tem dados de cada repo na variavel rep
            rep = json.loads(requests.get(repo["url"]).text)
        
            print "Salvando /" + usuario + "/repos/" + repo["name"] + ".txt"
            ff = open(usuario + "/" + usuario + ".repos." + repo["name"] + ".txt", "w")
            pickle.dump(rep, ff)
            ff.close()
            
            lang = json.loads(requests.get(rep["languages_url"]).text)
            
            print "Salvando /" + usuario + "/repos/" + repo["name"] + "/languages.txt"
            fff = open(usuario + "/" + usuario + ".repos." + repo["name"] + ".languages.txt","w")
            pickle.dump(lang, fff)
            fff.close()