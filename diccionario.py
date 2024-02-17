from io import open
import json


def guardar(palabra, significado):
    
    with open("diccionario.txt", "a+") as archivos:
        
        datos = {}
        
        datos[palabra] = significado
              
        json_str = json.dumps(datos)

        archivos.write("\n" + json_str)
        
        print('guardado...')
    

def buscar_key(claveBuscar):
    
    with open("diccionario.txt", "r+") as archivos:
        
        for linea in archivos.readlines():
            print('  entro valor : '+ linea)            
            
            try:
                data = json.loads(linea)
                print(data)
                
                for clave, val in data.items():
                    print(clave + " y " + val)
                    if val == claveBuscar:
                        print(f"Se encontró la el valor '{val}' con el valor '{claveBuscar}'.")
                        # Puedes hacer algo más aquí, como retornar la clave o realizar otra acción
                        return clave
            except json.JSONDecodeError:
                
                pass
        return "No se encontró la clave '{claveBuscar}' en el archivo."

def buscar_valor(valor_a_buscar):
    
    with open("diccionario.txt", "r+") as archivos:
    
        for linea in archivos.readlines():
            print('entro key')
            try:
                data = json.loads(linea)
                #print(data)
                
                #print("valor a buscar:  "+ valor_a_buscar)
                if valor_a_buscar in data:
                    valor = data[valor_a_buscar]
                    #print(f"Palabra asociada al valor '{valor_a_buscar}': {valor}")
                    return valor
                
            except json.JSONDecodeError:
                
                pass
        
        
        return "No se encontró '{valor_a_buscar}' en el archivo."

    

