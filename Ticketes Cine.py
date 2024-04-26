print("BIENVENIDOS AL CINE DE LUCI")
Lista_A = []
for i in range(0, 10):
    Lista_B = []
    for j in range(0,10):  
        Lista_B.append([])
    Lista_A.append(Lista_B)
ticketes=0
#imprime la matriz
Finalizar="No"
def pantalla():
     print("*****************PANTALLA***************")  
def imprimir():      
        for filas in Lista_A:
            print(filas)
        print("\n")
pantalla()       
imprimir()          
while Finalizar:      
    fila=(int(input("selecione la fila que desea: ")))
    columna=(int(input("selecione el asiento que desea: ")))
    Lista_A[fila][columna]="*"
    Salir=input("desea continuar comprando: ")
    ticketes=ticketes+1
    pantalla()
    imprimir()

    if Salir=="no":
        Finalizar=False
total=ticketes*2500
print("eL total a pagar es de", total, "colones")     

    
   







