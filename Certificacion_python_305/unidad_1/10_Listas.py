try:
    #Declarando una lista
    materias=["Programacion","Filosofia","Matematicas","Ingles"]
    print(materias[0])
    matrias.append("Lengua y comunicacion")
    print(materias)
    materias[1].remove("Biologia")
    print(materias)
    materias.remove("Matematicas")
    print(materias)
except IndexError:
    print("Indice correcto")