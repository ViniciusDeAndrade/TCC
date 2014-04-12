import pickle
from controles.GerenteGitHub import GerenteGitHub
from controles.GerenteArquivo import GerenteArquivo

gg = GerenteGitHub()

#usuario = raw_input('digite um nome de usuario: ')
#gg.salvarRepos("KirinDave")

#gg.salvarReposFaltando("KirinDave", "giter8")

# dicionarioLinguagens = gg.getLinguagensNoArquivo("mojombo")
# keys = dicionarioLinguagens.keys()
# 
# for key in keys:
#     print key + ": " + str(dicionarioLinguagens[key])

#gg.getLinguagensNoArquivo("KirinDave")
#print '..'

#===============================================================================
# f = open("mojombo/mojombo.repos.bert.languages.txt", "r")
# languages = pickle.load(f)
# 
# keys = languages.keys()
# 
# for key in keys:
#     print key + ": " + str(languages[key])
#===============================================================================


ga = GerenteArquivo()
#ranking = ga.ranquearUsuarios('JavaScript')
#ranking = gg.getLinguagensNoArquivo("mojombo")
ranking = gg.getLinguagens("vicenteneto")
print "=============================================="

for usuario in ranking:
    print usuario + " " + str(ranking[usuario]) + " pontos"

