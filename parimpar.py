def imparpar():
    n=input ("dime un numero ")
    y= input ("dime otro numero ")
    if n%2==0 and y%2==0:
        print "los dos son pares"
    if n%2!=0 and y%2!=0:
        print "los dos son impares"
    if n%2==0 and y%2!=0:
        print n ,  " es par y " , y, " es impar"
    if n%2!=0 and y%2==0:
        print n, " ES IMPAR Y ", y, " es par"
        
imparpar()
