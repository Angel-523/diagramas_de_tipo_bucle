#angel alonzo villegas angulo matricula:250217
#calcula la media aritmetica de un numero ingresado por teclado

acumulador=0                                                                    #variable donde depositar resultados y guardarlos
n= int (input("cuantos numeros agregaras: "))                                   #numero de numeros que solicitara el algoritmo

for i in range(n):                                                              #bucle con el rango determinado por el numero de numeros a solicitar

    num= float(input(f"ingrese el {i+1} numero: "))                             #solicita el numero que se agrega a la serie de numeros que se le busca una media
    acumulador=acumulador+num                                                   #suma y guarda los resultados en la variable
print(f"suma un total de {acumulador}, y se sumaron {i+1} numeros")             #da el total de la suma de los numeros y el numero de numeros que lo hicieron
acumulador=acumulador/(i+1)                                                     #obten la media
print(f"la media la suma de {i+1} numeros de dichos numero es {acumulador}")    #devuelve la media junto al numero de numeros que conformaron la serie de numeros a la que se le saca la media