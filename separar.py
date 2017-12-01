def separar():
    frase=raw_input('DIME ALGO')
    frase=str(frase)
    for i in range(0,len(frase),1):
        letra=frase[i:i+1]
        print letra
separar()
