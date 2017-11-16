def sustituiru():
    palabra=raw_input ("dime una palabra")
    mylist=list(palabra)
    for cont in range(0,len(palabra),1):
        if palabra[cont]=='a' or palabra[cont]=='e' or palabra[cont]=='i' or palabra[cont]=='o':
            mylist[cont]='u'
    str1="".join (mylist)
    print str1
sustituiru()
            
