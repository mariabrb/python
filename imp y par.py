def sumadedigitos():
    pares=0
    numero=input("dime un numero")
    impares=0
    while numero!=0:#IMPORTANTE EL != SIGNIFICA DISTINTO DE 
        cifra=numero%10
        if cifra%2==0:
            pares=pares+1
        else:
            impares=impares+1
        numero=numero/10
    print "Tiene ", pares, " pares"
    print "Tiene ", impares, " impares"
    impares=0
sumadedigitos()
