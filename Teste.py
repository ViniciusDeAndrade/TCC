import pickle
from controles.GerenteGitHub import GerenteGitHub
from controles.GerenteArquivo import GerenteArquivo

gg = GerenteGitHub()

#usuario = raw_input('digite um nome de usuario: ')
gg.salvarRepos("kevwil")

#gg.salvarReposFaltando("wayneeseguin", "msgpack-ruby")

# dicionarioLinguagens = gg.getLinguagensNoArquivo("mojombo")
# keys = dicionarioLinguagens.keys()
# 
# for key in keys:
#     print key + ": " + str(dicionarioLinguagens[key])

#===============================================================================
# f = open("mojombo/mojombo.repos.bert.languages.txt", "r")
# languages = pickle.load(f)
# 
# keys = languages.keys()
# 
# for key in keys:
#     print key + ": " + str(languages[key])
#===============================================================================


#ga = GerenteArquivo()
#ranking = ga.ranquearUsuarios('CSS')
#print ranking
