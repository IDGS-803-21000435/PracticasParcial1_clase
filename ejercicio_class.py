
#------------EJERCICIO 1-----------------

def ejercicio1():
    num = int(input("De cuantas filas sera la piramide: "))

    for i in range(num):
        for j in range(num - i -1):
            print(" ", end = "")
        for k in range(2 * i + 1):
            print("*", end = " ")
        print()

#-------------EJERCICIO 2----------------
lista = list()

def pedirNumeros():
    numIngreso = int(input("cuantos numeros ingresaras? -> "))

    for i in range(0, numIngreso):
        numLista = int(input("ingresa un numero: "))
        lista.append(numLista)

def ordenarArreglo():
    print(lista)
    lista.sort()
    print(lista)

def listarNumeros():
    for j in lista:
        string = ""
        resultado = j%2
        
        if resultado == 1:
            string = "el numero es impar"
        else:
            string = "el numero es par"
            
        repeticion = lista.count(j)
        if repeticion > 1:          
            print("el numero: {d} se repite: {f} veces y {h} ".format(d=j, f=repeticion, h=string))
        else:
            print("el numero: {d} no se repite y {f} ".format(d=j, f=string))
        
        
        aux = 0

def ejercicio2():
    pedirNumeros()
    ordenarArreglo()
    listarNumeros()
    lista.clear()
    
#-------------------Main-------------------
def main(n):
    if n == 1:
        ejercicio1()
    elif n == 2:
        ejercicio2()
    elif n == 0:
        print("finalizado")

if __name__=="__main__":
    main()