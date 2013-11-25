class Usuario:
    __login = ""
    __location = ""
    __repositorios = []
    
    def __init__(self, login, location, repositorios):
        __login = login
        __location = location
        __repositorios = repositorios
    
    def getLogin(self):
        return self.__login
    
    def getLocation(self):
        return self.__location
    
    def getRepositorios(self):
        return self.__repositorios