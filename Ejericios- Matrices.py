#Matriz 1 unidimensional (6) Vertical
for i in range(1,7):
    print(i)

print('\n')

#Matriz 1 bidimensional (6) horizontal 
for i in range(1,7):
    print(0, end="  ")

print('\n')    

#Matriz 3 bidimensional 6x6
for i in range(1,7):
    for j in range(1,7):
        print(0, end=" ")
    print(" ")    
print('\n') 

#Ahora voy a imprimir las coordenas 
for i in range(1,7): 
    for j in range(1,7):
        print( (i,j), end=" ") # Importante:aquí imprime dos dígitos por campo
    print(" ")

#Ejercicio 1 colocar 1s en vetical  
for i in range(1,7):
    for j in range(1,7):
        if i==j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print(" ")    
print('\n')  

#Ejercicio 2, 1 al 36
for i in range(1,7):
    for j in range(1,7):
        print( ((i-1)*6+j), end=" ")   #Necesité ayuda de chatgpt para esta parte
    print(" ")
print('\n')   

#Ejercicio 3, 1 al 6 y 6 al 1
for i in range(1,7):
    for j in range(1,7):
        if i % 2!=0:            
            print( j, end=" ")
        else:     
            print( 7-j, end=" ")
    print(" ")        
print('\n')

#Ejercicio 4 colocar 1s que formen una línea vertical de iz a derecha
for i in range(1,7):
    for j in range(1,7):
        if j+i== 7:           
            print( 1, end=" ")
        else:     
            print( 0, end=" ")
    print(" ")   
print('\n')  

#Ejercicio 5  poner unos en la mitad de la matriz
for i in range(1,7):
    for j in range(1,7):
        if i>= j:      
            print( 1, end=" ")
        else:     
            print( 0, end=" ")
    print(" ")
print('\n')               
#Ejercicio 6 como arriba pero inverso
for i in range(1,7):
    for j in range(1,7):
        if j>= i:      
            print( 1, end=" ")
        else:     
            print( 0, end=" ")
    print(" ")               
print('\n')    
#Ejercicio 7 cada columna debe ir sumando hasta llegar a 36
for i in range(1,7):
    for j in range(1,7): 
        print((j-1)*6+i, end=" ")  #no puedon decir que lo hice yo porque es
    print(" ")    #el inverso de la fórmula que me dio chatgpt en el ejercicio anterior
print('\n') 
    
#Ejercicio 7: As t Bs 
for i in range(1,7):
    for j in range(1,7):
        if i>= j and j%2!=0:       
            print( "A", end=" ")
        elif i>= j and j%2==0:
            print( "B", end=" ")
        else:     
            print( "", end=" ")
    print(" ")
print('\n')               
        