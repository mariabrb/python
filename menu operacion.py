# -*- coding: cp1252 -*-
def division(num1,num2):
    r=num1/num2
    return r
def multiplicacion(num1,num2):
    r=num1*num2
    return r
def resta(num1,num2):
    r=num1-num2
    
    return r
def suma(num1,num2):
    r=num1+num2
    return r
def menu_operacion():
    seguir="si"
    num1=input("dime un numero")
    num2=input ("dime otro numerico")
    while (seguir =="si"):
        print "que deseas hacer con los numeros"
        print "1.sumarlos"
        print "2.Restarlos"
        print "3.Multiplicarlos"
        print "4.Dividirlos"
        respuesta=input("Que quieres q haga cn ellos")
        if(respuesta==1):
            print num1,"+",num2,"=",suma(num1,num2)
        elif (respuesta==2):
            print num1,"-",num2,"=",resta(num1,num2)
        elif (respuesta==3):
            print num1,"*",num2,"=",multiplicacion(num1,num2)
        elif (respuesta==4):
            print num1,"/",num2;"=",division(num1,num2)
        seguir=raw=input('Dime si quieres continuar')
        #if (respuesta==1)
        #suma=num1+num2
        #print num1,"+",num2,"=",suma
        #esto se sustituirá por la función       
menu_operacion()
