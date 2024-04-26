# 1Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
def max(num1,num2):
    if  num1>num2:
        return num1
    return num2

print(max(6,3))

#2 Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def max_de_tres(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    return num3
print(max_de_tres(100,2400,2400.5)) 

#3  Definir una función que calcule la longitud de una lista o una cadena dada.
Milista=["Lucía", "María", "Rodríguez", "Maria", "Venegas", "Berrocal"]
def longitud(lista):
    long=0
    for i in lista:
        long=long+1
    return(long)
    
print(longitud(Milista))

#4 Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False
Vocales=["a","e","i","o","u"]
def identificadorVocal(letra, lista):
    letra=letra.lower()
    if letra in lista: 
        return True
    else:
        False
print(identificadorVocal("o", Vocales)) 

#5 Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
listaA=[1,1,2,3,5,8,13]

def sum(lista):
    suma=0
    for i in (lista):
        suma+=i
    return(suma)
def mult(lista):
    multi=1
    for i in lista:
        multi*=i
    return(multi)   
    
print(sum(listaA))  
print(mult(listaA))
        
