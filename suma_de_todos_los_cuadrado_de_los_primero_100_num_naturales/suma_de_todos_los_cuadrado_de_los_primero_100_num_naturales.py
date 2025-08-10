#angel alonzo villegas angulo matricula:250217
#suma el cuadrado de los primeros 100 numeros naturales
acumulador=0
contador=0
num=0
#da un bucle de 100
for i in range(100):                                                                #da un bucle con 100 vueltas
    num= i+1                                                                        #establesca que la variable num, recorra los numeros empezando por 1 y terminando en 100
    acumulador=acumulador+(num**2)                                                  #guarda el cuadrado del numero en la variable num
    contador=contador+1                                                             #un poco irrelevante, pero por gusto tambien lleva un conteo de cada operacion    
print(f"la suma del cuadrado los primeros 100 numero naturales es: {acumulador}")   #da el resultado de la operacion
print(f"efectuando un total de {contador} operaciones")                             #un poquito irrelevante, pero tambien el total de operaciones