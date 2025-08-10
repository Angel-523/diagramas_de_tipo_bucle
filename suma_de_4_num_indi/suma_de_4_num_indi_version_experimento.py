#angel alonzo villegas angulo matricula:250217
#calcula la suma de 4 num introducidos por teclado

#define
acumulador= 0                                                       #def
num= 0                                                              #def
for i in range (4):                                                 #establece el ciclo de 4 vueltas
    num= float (input(f"introdusca el {i+1} numero: "))             #solicite en numero
    acumulador= (acumulador)+(num)                                  #sume y guardelo en una variable comun

    print(f"{num} y acumula {acumulador}, y es el bucle {i+1}")     #esto es solo un provador de codigo y ojala me acuerde eliminarlo en la final

print(f"la suma de los 4 numeros es {acumulador}")                  #da el resultado