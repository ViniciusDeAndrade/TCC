from libsaas.services import github
import json
import requests
import pickle
from controles.GerenteGitHub import GerenteGitHub


#Leitura do arquivo
class GerenteArquivo:
    
    def ranquearUsuariosPorBytes(self, linguagem):
        usuarios = self.recuperarUsuarios()
        gg = GerenteGitHub()
        ranking = {}
        
        for usuario in usuarios:
            ranking[usuario["login"]] = 0
        
        #Pega as linguagens dos usuarios no arquivo
        for usuario in usuarios:
            #linguagens = gg.getLinguagensNoArquivo(usuario["login"])
            countBytes = gg.getBytesDaLinguagemNoArquivoComExcecao(usuario["login"], linguagem)

            try:
                ranking[usuario["login"]] += countBytes
            except:
                print '',
            
            print usuario["login"] + ' :' + str(ranking[usuario["login"]])
        
        return ranking

    def ranquearUsuariosPorStars(self, linguagem):
        usuarios = self.recuperarUsuarios()
        gg = GerenteGitHub()
        ranking = {}

        for usuario in usuarios:
            ranking[usuario["login"]] = 0

        for usuario in usuarios:
            countStars = gg.getStarsPorLinguagemNoArquivoComExcecao(usuario["login"], linguagem)

            try:
                ranking[usuario["login"]] += countStars
            except:
                print '',

            print usuario["login"] + ' :' + str(ranking[usuario["login"]])

        return ranking
            
    def ranquearUsuariosPorFork(self, linguagem):
        usuarios = self.recuperarUsuarios()
        gg = GerenteGitHub()
        ranking = {}

        for usuario in usuarios:
            ranking[usuario["login"]] = 0

        #Pega a quantidade de forks do usuario com a linguagem passada por parametro
        for usuario in usuarios:
            countForks = gg.getForksPorLinguagemNoArquivoComExcecao(usuario["login"], linguagem)

            try:
                ranking[usuario["login"]] += countForks
                print usuario["login"] + ' :' + str(ranking[usuario["login"]])
            except:
                print usuario["login"] + ' :' + str(ranking[usuario["login"]])
                
        return ranking
        

    def ranquearUsuarios(self, linguagem):
        gg = GerenteGitHub()
        ranking = {}

        for usuario in self.recuperarUsuarios():
            login = usuario["login"]
            dados = gg.getDadosPorLinguagem(login, linguagem)
            try:
                ranking[login] = round(dados["countStars"] * dados["countForks"] * (dados["countBytes"]/1024))
            except:
                ranking[login] = 0
            
        return ranking
    
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
