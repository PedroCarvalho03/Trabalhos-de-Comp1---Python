def multiplicacao1(x,y):
    ''' Entrada = int
        Saida = int
        Calcula a multiplicacao de x por y sem usar o * '''
    m = 0
    x0 = 0 
    while m<y:
        mult = x0 + x
        m = m + 1
        x0 = mult
    return mult

# print(multiplicacao1(2,3))
# print(multiplicacao1(10,5))

def somaconj2(x):
    '''Entrada = int
       Saida = float
       Calcula o somatorio de subconjuntos de um conjunto maior'''
    m = 0
    st= 0
    while m <= x  :
        st = st + ((1+m)*m)/2
        m = m + 1
        
    return st        
        
#print(somaconj2(2))
#print(somaconj2(5))
#print(somaconj2(10))
#print(somaconj2(500))
        
def fatorial(x):
    m = 0
    fat = 1
    while m <= x:
        fat= fat*x
        x = x-1
        m = m + 1
    return fat

def questao3a(n,k):
    '''Entrada = int
       Saida = float
       Calcula o arranjo entre dois numeros '''
    if n-k == 0:
        arranjo = fatorial(n)/1
    else:
        arranjo = fatorial(n)/fatorial((n-k))
    return arranjo

# print(questao3a(3,2))
# print(questao3a(3,3))
# print(questao3a(4,2))
        
def questao3b(n,k):
    '''Entrada = int
       Saida = float
       Calcula a combinacao entre dois numeros'''
    comb = questao3a(n,k)*(1/fatorial(k))
    return comb

#print(questao3b(3,2))
#print(questao3b(3,3))
#print(questao3b(4,2))
    
def primo4a(num):
    '''Entrada = int
       Saida = booleano
       Infere se um numero eh primo ou nao'''
    primo = False
    m = 0
    while m < num :
        if m>1 and num%m == 0:
            primo = False
            m = num + 1
        elif  num ==2 or (m>1 and num%m != 0):
            primo = True
        m = m + 1
    return primo

#print(primo4a(1))
#print(primo4a(2))
#print(primo4a(9))
#print(primo4a(11))
 
def questao4b(n):
    '''Entrada = int
       Saida = int
       Encontra o numero primo sucessor do numero indicado '''
    if primo4a(n) == True:
        return n
    while primo4a(n) == False:
        n= n + 1
        if primo4a(n) == True:
            return n
        
#print(questao4b(3))
#print(questao4b(9))
#print(questao4b(12))
#print(questao4b(32))

def caixadagua5(x0,y):
    '''Entrada = int,float
       Saida = int
       Calcula quantos dias leva ate uma caixa d agua enche completamente'''
    dia = 0
    x = 0
    y0 = 0
    while x < x0:
        y0 = y + x
        x = y0/2
        y = y + y*(0.2)
        dia = dia + 1
    return dia

#print(caixadagua5(2,1))
#print(caixadagua5(2,0.5))
#print(caixadagua5(3,2))
#print(caixadagua5(100,10))
        