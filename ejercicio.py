import ejercicio_class

def ejecucion():
    num = 1

    while num != 0:
        num1 = int(input("----------------------------------------------\n"+
                    "seleccione el ejercicio a ejecutar \n"+
                    "1- Ejercicio de piramide \n"+
                    "2- Ejercio lista \n"+
                    "0- finalizar \n" +
                    "respuesta: "))
        
        ejercicio_class.main(num1)
        
        num = num1

