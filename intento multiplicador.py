def multiplicador():
    n= input("dime que tabla quieres que escriba")
    print "tabla del ",n
    for cont in range (1,11,1):
        print n,"x",cont,"=",n*cont       
multiplicador()
