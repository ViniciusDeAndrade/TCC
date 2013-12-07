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
        for i in range(100):
            if(gg.getLinguagens(usuarios["Login"]).keys() == linguagem):
                chaves = gg.getLinguagens(usuarios["Login"] ).keys()
                for chave in chaves:
                    print usuarios["Login"] + ' ' + str(chaves)  + ' :' str(gg.getLinguagens(usuarios["Login"]).values())
            

  
    
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


        
        