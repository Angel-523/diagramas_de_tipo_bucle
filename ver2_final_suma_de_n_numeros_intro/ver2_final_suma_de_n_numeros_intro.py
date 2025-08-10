#angel alonzo villegas angulo matricula:250217
#calcula la suma de n num introducidos por teclado

num=0 #definicion de num
sum=0 #definicion de sum
n= int (input("favor de ingresar la cantidad de numeros que sumara: ")) #el rango que el bucle abarcara

for i in range(n):                                                      #establece el rango con n 
     num= float (input(f"introdusca el {i+1} numero:"))                 #se introducen los numeros a sumar, bajo influencia del bucle se reutilizara estar variable para introducir todos los num a sumar 
     sum=sum+num                                                        #se realiza la operacion de forma que tambien acumule valores anteriores
    
print (f"el resultado es de la suma de {n} numeros, es: {sum}")         #se da el resultado