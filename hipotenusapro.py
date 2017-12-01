import math
def hipotenusa(a,b):
    return math.sqrt((a*a)+(b*b))

def main():
    cateto1=input('dime un cateto')
    cateto2=input('dime el otro cateto')
    print ('la hipotenusa es: '),hipotenusa(cateto1,cateto2)

main()
