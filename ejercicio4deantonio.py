def sumadedigitos():
    pares=0
    numero=input("dime un numero")
    numero1=numero
    while numero!=0:#IMPORTANTE EL != SIGNIFICA DISTINTO DE 
        cifra=numero%10
        if cifra%2==0:
            pares=pares+1
        numero=numero/10
    print "Tiene ", pares, " pares"
    impares=0
    while numero1!=0:#IMPORTANTE EL != SIGNIFICA DISTINTO DE 
        cifra=numero1%10
        if cifra%2!=0:
            impares=impares+1
        numero1=numero1/10
    print "Tiene ", impares, " impares"

sumadedigitos()
