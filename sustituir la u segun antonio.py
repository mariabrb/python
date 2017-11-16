def pig_latin():
    texto= raw_input ("dime un texto entero")
    for cont in range(o,len(texto),1):
        if texto[cont]=='a' or texto[cont]=='A' or texto[cont]=='e' or texto[cont]=='E' or texto[cont]=='i' or texto[cont]=='I' or texto[cont]=='o' or texto[cont]=='O':
            print'u'
        else:
            print texto[cont],
pig_latin()
