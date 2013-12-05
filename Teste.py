from controles.GerenteArquivo import GerenteArquivo
from controles.GerenteGitHub import GerenteGitHub

#gu = GerenteUsuario()
#===============================================================================
# usuarios = gu.getUsuarios();
# gu.salvarUsuarios(usuarios);
#===============================================================================
gg = GerenteGitHub()
ga = GerenteArquivo()

user = ga.buscarUsuario("mojombo")

print user["name"]

