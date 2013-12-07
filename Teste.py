from controles.GerenteArquivo import GerenteArquivo
from controles.GerenteGitHub import GerenteGitHub


gg = GerenteGitHub()
ga = GerenteArquivo()

#===============================================================================
# login = raw_input('digite o login : ')
# 
# user = ga.buscarUsuario(login)
# 
# linguagens = gg.getLinguagens(login)
# 
# chaves = linguagens.keys()
# chaves.sort()
# 
# for chave in chaves:
#     print str(chave) + ": " + str(linguagens[chave])
#===============================================================================

ga.ranquearUsuarios("Java")