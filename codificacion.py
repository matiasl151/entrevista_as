import string 

def cifrado(digitos_clave : int, clave : string, texto : string):
    
    texto_cifrado = ""
    alfabeto = list(string.ascii_uppercase)

     if (len(texto) > 0 and len(texto) < 10000) and (digitos_clave < 9 and digitos_clave > 1) :
        if digitos_clave == len(clave):
            texto = texto.replace(' ', '')
            texto = str(texto).upper()
            
            # Partir el texto en partes de tamaño arbitrario
            texto_partido = [texto[i:i + digitos_clave] for i in range(0, len(texto), digitos_clave)]

            for particion in texto_partido:
                n=0
                while n < (digitos_clave):
                    try:
                        if particion[n] in alfabeto:
                            indice_actual = alfabeto.index(particion[n])
                            indice_codificado = (indice_actual + int(clave[n])) % len(alfabeto)
                            texto_cifrado += alfabeto[indice_codificado]
                        else:
                            # QUE HAGO CON LA Ñ???
                            texto_cifrado += particion[n]
                    except:
                        break

                    n += 1       
        else:
            print("No coincide el numero de digitos de la clave con la clave ingresada")
    else:
        print("Error en el texto ingresado")
    return texto_cifrado
    

if __name__ == "__main__":

    # print(cifrado(3,"123", "Chau idiotas"))
    # print(cifrado(2,"","Nope"))
    # print(cifrado(2,"98","Que bien que bien ya todo esta bien"))
    print(cifrado(2,"23","YO HE LOGRADO ENCENDER UNA CERILLA"))
