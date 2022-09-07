# Ciclo While o mientras

# declarar una variables centinela o variable de 
# control para evaluar la ejecución de mi ciclo 

import math


i = 0
#menu de opciones
print ("***Menu***")
print ("1. Sumar dos números")
print ("2. Restar dos números")
print ("3. Encontrar la raiz cuadrada de número")
print ("4. Multiplicar dos números")
print ("5. Salir")
#programar la estructura del ciclo mientras 
while(i!= 5):
    i= int (input("Digite una opción del menú: "))
    
    if(i==1):
        print("Dime un numero")
        primerNumero = int(input())
        print ("Dime otro numero")
        segundoNumero = int(input())
        print ("Su suma es")
        print (primerNumero + segundoNumero)
    elif(i==2):
        print("Dime un numero")
        primerNumero = int(input())
        print ("Dime otro numero")
        segundoNumero = int(input())
        print ("Su resta es")
        print (primerNumero - segundoNumero)
    elif(i==3):
        print("Dime un numero")
        numero = int (input())
        raiz = math.sqrt(numero)
        print ("Su raiz cuadrada es")
        print (raiz)
    elif(i==4):
        print("Dime un numero")
        primerNumero = int(input())
        print ("Dime otro numero")
        segundoNumero = int(input())
        print ("Su multiplicacion es")
        print (primerNumero * segundoNumero)
    elif(i==5):
        break
    else:
        print("Digita una opción valida")
        
    #print ("Estoy saltando cuerda",i) 
    #i = i + 1 #contador
print("Salimos del while")


 