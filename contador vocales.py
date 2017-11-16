def contadorvocales():
    palabra=raw_input ('dime una palabra')
    a=0
    e=0
    i=0
    o=0
    u=0
    for cont in range (0,len(palabra),1):
        if palabra[cont]=='A' or palabra[cont]=='a':
            a=a+1
        if palabra[cont]=='e' or palabra[cont]== 'E':
            e=e+1
        if palabra[cont]=='i' or palabra[cont]=='I':
            i=i+1
        if palabra[cont]=='o' or palabra[cont]=='O':
            o=o+1
        if palabra[cont]=='u' or palabra[cont]=='u':
            u=+1
    print 'hay',a ,'a',e,'e',i,'i',o,'o',u,'u'
    
contadorvocales()
