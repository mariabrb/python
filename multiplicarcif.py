def multiplicar():
    numero=input("DIME UN NUMERO")
    numero=str(numero)
    longitud=len(numero)
    total=1
    
    for i in range (0,longitud,1):
       total=total*int(numero[i:i+1])


    print total

multiplicar()

