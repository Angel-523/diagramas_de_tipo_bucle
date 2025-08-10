#angel alonzo villegas angulo matricula:250217
#calcula la suma de n num introducidos por teclado
num=0           #def
sum=0           #def
n= 2            #def
contador=1      #estetico
ran=2
for i in range(ran):
    for j in range(n):
        num= float (input(f"escriba el {contador} numero: "))
        sum= sum+num
        contador=contador+1
        
    y_n= str (input("¿desea seguir agregar mas numeros?: "))
    if y_n in ["Si", "si", "S", "s", "Y", "y", "ye", "Ye", "Yes", "yes"]:
        print("¿cuantos numeros mas desea agregar?")
        n= int (input(": "))
    
else: print(f"el resultado es de la suma de {contador} numeros, es: {sum}")
exit()