import pickle

f = open("usuarios.pck", "r")

for i in range(100):
    u = pickle.load(f)
    print u["login"]