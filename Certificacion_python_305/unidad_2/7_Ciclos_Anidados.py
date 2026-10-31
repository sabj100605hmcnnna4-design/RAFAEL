#Ciclo externo para el numero de la base de la tabla
for i in range(1,4):
    print(f"---Tabla del{i}")
    #Ciclo interno para multiplicar del 1 al 10
    for j in range(1,11):
    #1(i) x 1(j)=1
       print(f"{1} x {j} = {i*j}")
    print("AQUI TERMINA LA DEL {i}")