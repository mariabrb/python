import math
def ecuacion():
    a=input('dime la x^2')
    b=input('dime la x')
    c=input('dime el numero sin x')
    raiz=math.sqrt((b*b)-(4*a*c))
    denominador=2*a
    unasol=(-b+raiz)/denominador
    print ('la primera soluciones es'),unasol
    dosol=(-b-raiz)/denominador
    print ('la segunda solucion es'),dosol
    
    
ecuacion()
