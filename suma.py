#se pide un num obtener x pantalla la suma de digitos del numero
def suma():
    num=input('dime  un num')
    cadena=str(num)
    longi=len(cadena)
    suma=0
    for i in range(0,longi,1):
        suma=suma+int(cadena[i:i+1])

        
    print suma
suma()
