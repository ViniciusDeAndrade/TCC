import pickle
from controles.GerenteGitHub import GerenteGitHub

gg = GerenteGitHub()

#usuario = raw_input('digite um nome de usuario: ')
gg.salvarRepos("wycats")

#gg.salvarReposFaltando("pjhyett", "sinatra_auth_github")

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