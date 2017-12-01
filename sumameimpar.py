def sumameimpares():
    x=input('dame un numero')
    y=input('dame otro numer')
    suma=0
    for i in range (x,y,1):
        if i%2==0:
            suma=suma+0
        else:
            suma=suma+i
    print suma

sumameimpares()

