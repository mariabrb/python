import math


def segundogrado(a,b,c):
    raiz=math.sqrt((b*b)-(4*a*c))
    soluno=(-b+raiz)/2*a
    soldos=(-b-raiz)/2*a
    print'soluciones: ',soluno,' y ',soldos

def principal():
    x=input('dime la a')
    y=input('dime la b')
    z=input('dime la c')
    segundogrado(x,y,z)



principal()

    
    



