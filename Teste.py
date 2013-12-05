from controles.GerenteArquivo import GerenteArquivo
from controles.GerenteGitHub import GerenteGitHub

#gu = GerenteUsuario()
#===============================================================================
# usuarios = gu.getUsuarios();
# gu.salvarUsuarios(usuarios);
#===============================================================================
gg = GerenteGitHub()
ga = GerenteArquivo()

login = raw_input('digite o login : ')

user = ga.buscarUsuario(login)

linguagens = gg.getLinguagens(login)
    
for lang in linguagens:
    print lang

