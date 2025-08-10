#angel alonzo villegas angulo matricula:250217
#calcular e imprimir los cuadrados del 20 al 50
cuadrado=0                                      #def
num=20                                          #numero inicial que es 20 porque se ira del 20 al 50
for i in range(31):                             #el rango es de 31 para que llegue a 50 y no se detenga en 49
    cuadrado= num**2                            #se realiza el cuadrado del num
    num=num+1                                   #se prepara el siguiente, no se uso "i" por cuestiones de inspiracion (lo escribi asi en el diagrama y no encuentro mi borrador T-T)
    print(f"el cuadrado de {num-1}: {cuadrado}")#imprime el cuadrado del numero de turno