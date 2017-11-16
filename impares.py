def impares():
    numero=input("dime un numero")
    impares=0
    while numero!=0:#IMPORTANTE EL != SIGNIFICA DISTINTO DE 
        cifra=numero%10
        if cifra%2!=0:
            impares=impares+1
        numero=numero/10
    print "Tiene ", impares, " impares"
impares()

