def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
    


def main():
    x=input('dime un numero')
    print factorial(x)






    
main()
