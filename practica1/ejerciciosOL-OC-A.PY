#ejercios de operadores logicos, operadores condicionales y arimeticos


#EJERCICIOS
#1. Dado un número indicar si es par o impar.
#2. Hacer un programa que solicite dos números e
#indique el signo de la multiplicación sin efectuarla.
#3. Introducir dos números enteros por el teclado,
#DIVIDENDO y DIVISOR. Si dividendo es divisible
#por divisor, el programa debe mostrar el mensaje
#“DIVISIBLES” caso contrario “NO SON
#DIVISIBLES”.
#4. Dadas tres notas parciales. Indicar si se promociona,
#va a final o recursa. Sabiendo que:
#[0,4) - Recursa
#[4,7) - Final
#[7-10] - Promociona


#1
#num=int(input("ingresa un numero entero: "))
#n=num
#if(n%2==0):
#    print("es un numero par")
#else:
#    print("es un numero impar") 

#2
#num=int(input("ingrese un numero: "))
#num2=int(input("ingrese otro numero: "))
#if(num>0 and num2>0) or (num<0 and num2<0):
    #print("+")
#else:
    #print("-")    

#3
#num=int(input("ingrese un numero entero: "))
#num2=int(input("ingrese otro numero entero: "))
#n1=num
#n2=num2
#if(num%num2==0):
 #   print("es divisible")
#else:
    #print("no es divisible ")    

#4
num=int(input("nota del alumno parcial 1: "))
num2=int(input("nota del alumno parcial 2: "))
num3=int(input("nota del alumno parcial 3: "))
n1=num
n2=num2
n3=num3
prom=n1+n2+n3
res=prom/3
print("el promedio es: ", res)
if(res>=7):
    print("el alumno promociona")
else:
    if(res<4):
        print("el alumno recursa")
    else:
        print("el alumno va a final")    