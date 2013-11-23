import requests
import json

from libsaas.services import github

gh = github.GitHub("1caa7d1d703267253a4da559872a5179d0aef170")


users = requests.get("https://api.github.com/repositories")
users = json.loads(users.text)


for repo in users:
    #print repo
   
    user = repo["owner"]["login"]
    repo_name = repo["name"]
    

    repo = gh.repo(user, repo_name)
    
    languages = repo.languages()
    usuario = gh.user(user)
    #localizacao = usuario["location"]
    print dir(usuario)

    #print user + ": " + str(languages)
    #print localizacao