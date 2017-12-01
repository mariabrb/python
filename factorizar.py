def factorizar(num):
    if num%2==0:
        print '2,'
        factorizar(num/2)
    elif num%3==0:
        print'3,'
        factorizar(num/3)
    elif num%5==0:
        print '5,'
        factorizar(num/5)
    elif num%7==0:
        print'7,'
        factorizar(num/7)
    elif num%11==0:
        print'11,'
        factorizar(num/11)
    elif num%13==0:
        print'13,'
        factorizar(num/13)
    elif num%17==0:
        print'17,'
        factorizar(num/17)
    elif num%21==0:
        print'21,'
        factorizar(num/21)
    else:
        print num
#ifnumm!=1:print num

        
def main():
    num=input('dime algo')
    factorizar(num)


    
main()
        
