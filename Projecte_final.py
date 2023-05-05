from funcions import *

def generar():
    comprobar(get_files())

    animalsxml = open(parametres(2).rstrip()+"/"+nom_valids+".xml","w")
    animalsxml.write(xml())
    animalsxml.close()


generar()



