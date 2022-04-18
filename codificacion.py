import string


def cifrado(digitos_clave: int, clave: string, texto: string):
    texto_cifrado = ""
    alfabeto = list(string.ascii_uppercase)

    if (0 < len(texto) < 10000) and (0 < digitos_clave < 9):
        if digitos_clave == len(clave):
            texto = texto.replace(' ', '')
            texto = str(texto).upper()

            # Partir el texto en partes de tamaño arbitrario
            texto_partido = [texto[i:i + digitos_clave] for i in range(0, len(texto), digitos_clave)]

            for particion in texto_partido:
                n = 0
                while n < digitos_clave:
                    try:
                        if particion[n] in alfabeto:
                            indice_actual = alfabeto.index(particion[n])
                            indice_codificado = (indice_actual + int(clave[n])) % len(alfabeto)
                            texto_cifrado += alfabeto[indice_codificado]
                        else:
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
    print(cifrado(3,"123", "YO HE LOGRADO ENCENDER UNA CERILLA"))
    print(cifrado(2, "", "YO HE LOGRADO ENCENDER UNA CERILLA"))
    print(cifrado(4,"9812","YO HE LOGRADO ENCENDER UNA CERILLA"))
    print(cifrado(2, "23", "YO HE LOGRADO ENCENDER UNA CERILLA"))
