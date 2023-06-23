def uniaoTupla1(tupla1,tupla2,tupla3,tupla4):
    resultado = ()
    for pos in range(len(tupla1)):
        resultado = resultado + (tupla1[pos],)
        resultado = resultado + (tupla2[pos],)
        resultado = resultado + (tupla3[pos],)
        resultado = resultado + (tupla4[pos],)
        
    return resultado

#print(uniaoTupla1(('Harry Poter',),('J K Rowling',),(223,),(1997,)))
#print(uniaoTupla1(('Harry Poter','Percy Jackson'),('J K Rowling','Rick Riordan'),(223,337),(1997,2005)))
# print(uniaoTupla1(('Harry Poter','Percy Jackson','A Arma Escalate'),('J K Rowling','Rick Riordan','Renata Ventura'),(223,337,667),(1997,2005,2012)))

def localizacao2(tupla1,tupla2,tupla3,sensor):
    resultado = ()
    if sensor in tupla3:
        for pos in range(len(tupla3)):
            if sensor == tupla3[pos]:
                resultado = resultado + ((tupla1[pos],tupla2[pos]),)
        return resultado
    else:
        return resultado
    
#print(localizacao2((1.0,3.4,-3.2),(5.6,10.2,20.1),('S1','S2','S1'),'S1'))
#print(localizacao2((1.0,3.4,-3.2),(5.6,10.2,20.1),('S1','S2','S1'),'S2'))
#print(localizacao2((1.0,3.4,-3.2),(5.6,10.2,20.1),('S1','S2','S1'),'S3'))
#print(localizacao2((7.77,1.54,-9.82,22.38,-17.43),(11.27,-42.39,-28.75,-31.15,37.44),('S3','S1','S4','S4','S2'),'S4'))
    
def string3(st1,st2,st3):
    i = 0
    num1= len(st1)
    num2= len(st2)
    if st2 in st1:
        while i<num1:
            num1 = len(st1)
            if st1[0:num2] == st2  :
                st1 = st3 + st1[num2:num1]
                   
            elif st1[i:(i+num2)] == st2:
                st1 = st1[0:i] + st3 + st1[(i+num2):num1]
            
                        
            i = i+1
        return st1
    
    else :
        return st1
            
        
        
#print(string3(('Este eh um teste'),('um'),('o')))
#print(string3(('Este eh um teste'),('te'),('aeiou')))
#print(string3(('aaaa'),('aa'),('b')))
#print(string3(('áááá'),('aa'),('b')))
#print(string3(('aaaa'),('aaaaaaaa'),('b')))
#print(string3(('DDdDDdddD'),('dD'),('StrINGtesTE')))
#print(string3(('Saida esta incorreta!'),('in'),('')))
#print(string3(('Retorno errado?'),('errado'),('certo')))
    
def dentroMedia4a(tupla):
    resultado = ()
    media = 0
    for i in tupla:
        media = media + i/len(tupla)
        
    for pos in range(len(tupla)):
        if media > tupla[pos] :
            resultado = resultado + (pos,)
            
    return resultado

#print(dentroMedia4a((1,5,9)))
#print(dentroMedia4a((20,15,9,6)))
#print(dentroMedia4a((10.5,8.5,30.3,25,12.7)))

def abaixoMedia4b(tupla):
    resultado = ()
    quant = len(tupla) # len da tupla
    quant1 = len(tupla[0]) # len da subtupla
    tuplaFM = ()
    tuplaPs = ()
    tuplaQFm = ()
    n1 = 0
    cont = 0
    for i in range(quant):
        tuplaFM= tuplaFM + dentroMedia4a(tupla[i])
        
    while n1<quant1:
        if n1 in tuplaFM:
            for i1 in range(len(tuplaFM)):
                if n1 == tuplaFM[i1]:
                    cont = cont + 1
            tuplaQFm = tuplaQFm + (cont,)
        else :
            tuplaQFm = tuplaQFm + (0,)
        n1 = n1 + 1
        cont = 0
    for pos in range(quant1+1):
        if pos > 0 :
            x = 'Jogador{0}'.format(pos) 
            tuplaPs = tuplaPs + (x,)
            
    for pos1 in range(len(tuplaQFm)):
        resultado = resultado + ((tuplaPs[pos1],tuplaQFm[pos1]),)
        
    return resultado
        
        
#print(abaixoMedia4b(((1,0,1,0,1),(1,1,0,0,1),(1,1,0,0,0),(1,1,1,0,0))))
#print(abaixoMedia4b(((25,32,20,40,27,35,22),)))
#print(abaixoMedia4b(((10,7,6,6),(2.3,6.7,5.1,3.4),(100,74.32,50.95,40.79))))