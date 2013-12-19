from libsaas.services import github
import json
import requests
import pickle
from controles.GerenteGitHub import GerenteGitHub


#Leitura do arquivo
class GerenteArquivo:
    
    def ranquearUsuarios(self, linguagem):
        usuarios = self.recuperarUsuarios()
        gg = GerenteGitHub()
        ranking = {}
        
        for usuario in usuarios:
            ranking[usuario["login"]] = 0
        
        #Pega as linguagens dos usuarios no arquivo
        for usuario in usuarios:
            linguagens = gg.getLinguagens(usuario["login"])
            #Agora compara se a linguagem eh a do paremotro
            #Se for, poe o login do usuario na lista que deve ser retornada
            for lang in linguagens:
                if(lang == linguagem):
                    ranking[usuario["login"]] += 1
            
            print usuario["login"] + ' :' + str(ranking[usuario["login"]])
        
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