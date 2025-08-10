#angel alonzo villegas angulo matricula:250217
#calcula la suma de 4 num introducidos por teclado

#define
acumulador= 0
num= 0
#establece el ciclo
for i in range (4):
    num= float (input(f"introdusca el {i+1} numero: "))
    acumulador= (acumulador)+(num)

print(f"la suma de los 4 numeros es {acumulador}")