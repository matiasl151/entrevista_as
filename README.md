# Desafio de entrevista laboral

Objetivo: Desarrollar una aplicación que resuelva el siguiente problema, utilizando cualquier lenguaje de programación.





PROBLEMA: MENSAJE CODIFICADO

Un científico ha hecho un brillante descubrimiento, y quiere comunicárselo a sus colegas. Temiendo que el mensaje sobre el descubrimiento pueda caer en manos inescrupulosas, decide codificarlo utilizando una variante del cifrado César, que codifica por sustitución haciendo que cada letra en el texto original sea reemplazada por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto. 

Por ejemplo, con un desplazamiento de 3 posiciones, la "A" sería sustituida por la "D", la "B" por la "E", etc. Se considera que el alfabeto es circular o sea que a continuación de la Z está la A. 

Para complicar un poco el código y hacer menos descubrible su decodificador, decide utilizar como clave de cifrado una secuencia de N dígitos a repetir las veces que haga falta. Cada dígito de su expresión decimal especificaría la magnitud del corrimiento cíclico. Así por ejemplo, si el científico pensó que las letras en posiciones impares se reemplacen por las que están a distancia 2, y que para las que están en posiciones pares el desplazamiento sea 3, su mensaje cifrado usaría la clave 23, que tiene N=2 dígitos. En el mensaje cifrado los blancos no se incluyen, y sus posiciones no se tienen en cuenta (por ejemplo la H está en la posición 3). 

Así si el mensaje fuera: 

YO HE LOGRADO ENCENDER UNA CERILLA 

la codificación utilizando N=2 y clave 23 sería 

ARJHNRIUCGQHPFGQFHTXPDEHTLNOC 

El mismo mensaje con N=3 y clave 012 resultaría en: 

YPJEMQGSCDPGNDGNEGRVPADGRJNLB  



Para ayudar a los expertos se te pide que escribas un programa/función que permita codificar el texto de los mensajes de científico. 

Datos de Entrada:

- la cantidad N de dígitos de la clave de cifrado  ( 1 ≤ N ≤ 9 ) 

- la clave de cifrado

- el texto a cifrar, de largo T  ( 1 ≤ T ≤ 10.000 ) 

Datos de Salida: El mensaje cifrado, sin los blancos. 

Ejemplo: Para N=2, Clave=23, T=34, texto="YO HE LOGRADO ENCENDER UNA CERILLA", la salida será "ARJHNRIUCGQHPFGQFHTXPDEHTLNOC".
