def pizza():
    x=input("dime el diametro de la pizza")
    radio=x/2
    pi=3.1416
    area=(radio*radio)*pi
    precio=input("dime cuanto vale la pizza")
    centrimetro=precio/area
    print centrimetro

    y=input('dime otrto diamtro de pizza')
    radio2=y/2
    area2=(radio2*radio2)*pi
    precio2=input("dime cuanto vale la pizza")
    centrimetro2=precio2/area2
    print centrimetro2

    if centrimetro==centrimetro2:
        print 'son iguales'
        
    if centrimetro<centrimetro2:
        print 'la segunda pizza es + cara'
    else:
        print'la 1 es + cara'

    
    

pizza()
