def divisiveis1(lista,n):
    '''Entrada = list,int
       Saida = list
       Descobre os numeros da lista divisiveis por n'''
    div = []
    pos = 0
    while pos<len(lista):
        if lista[pos]%n == 0 :
            div.append(lista[pos])
        pos = pos + 1
    return div

#print(divisiveis1([4,1,7,10,15],2))
#print(divisiveis1([-6,-2,3,1,9,12],3))
#print(divisiveis1([5,10,15,20,25,30,35],10))

def intercaladas2(lista1,lista2):
    '''Entrada = list
       Saida = list
       Intercalar os elementos de duas listas de mesmo tamanho
       com a ordem dos elementos da segunda lista de tras para
       frente '''
    res = []
    n = 0
    pos1 = 0
    pos2 = -1
    lista3 = lista1 + lista2
    while n<len(lista3):
        if n == 0 or n%2 == 0 :
            res.append(lista1[pos1])
            pos1 = pos1 + 1
        else :
            res.append(lista2[pos2])
            pos2 = pos2 - 1
        n = n + 1
    return res
       
#print(intercaladas2([1,3,5,7,9],[10,8,6,4,2]))
#print(intercaladas2([-2,3,4,0],[5,1,4,-7]))
#print(intercaladas2([7.2,-5.3],[1.9,3.5]))
#print(intercaladas2(['a',-1,12.5],[52,'teste',10.75]))

def operacoes3(lista1,lista2,lista3):
    '''Entrada = lis
       Saida = list
       Faz operacoes entre elementos de mesma posicao das
       3 listas '''
    res = []
    pos = 0
    calculo = 0
    while pos<len(lista1):
        calculo = (lista1[pos]+lista2[pos])*lista3[pos]
        res.append(calculo)
        pos = pos + 1
        
    return res

#print(operacoes3([1,2],[3,4],[5,6]))
#print(operacoes3([1,1,1],[2,2,2],[1,1,1]))
#print(operacoes3([1,1,1],[2,2,2],[3,3,3]))
#print(operacoes3([1,10,2,4],[3,5,4,2],[0.5,0.2,2,1]))


def questao4(lista):
    '''Entrada = list
       Saida = int
       Calcula a soma das multiplicacoes entre os valores da lista'''
    soma = 0
    pos = 0
    quant = len(lista)
    while pos<len(lista):
        if pos == 0 :
            while quant>0:
                soma = soma + lista[pos]*lista[quant-1]    
                quant = quant - 1
        elif lista[pos-1]<lista[pos] and pos != 0:
            quant = len(lista)
            while quant>pos:
                soma = soma + lista[pos]*lista[quant-1]    
                quant = quant - 1
                
        pos = pos + 1
                
            
    return soma

#print(questao4([1,2,3]))
#print(questao4([2,3,4,5,6]))
#print(questao4([-3,-1,0,2]))
#print(questao4([-7,-4,-3,-1,2,5,8,9]))
        
def perfil5(lista):
    '''Entrada = list
       Saida = booleano
       Verifica se a lista tem o perfil de escher'''
    pos = 0
    n = len(lista)
    res = False
    k = 1
    while pos<len(lista) and n-k>0:
        if lista[pos] + lista[n-k] == lista[pos+1] + lista[n-(k+1)]:
            res = True
            pos = pos + 1
            k = k + 1
        else:
            res = False
            pos = len(lista)
        
    return res

#print(perfil5([1,2]))
#print(perfil5([2,3,5]))
#print(perfil5([2,3,4]))
#print(perfil5([2,1,9,13,12]))
#print(perfil5([3,6,6,4,3,2,8,7,6,4,4,7]))
def fatorial(n):
    fatorial = 1
    mult = 1
    if n == 0 :
        fatorial = 1
    else :
        while mult<=n:
            fatorial = fatorial*mult
            mult = mult + 1
    return fatorial

def combinacao(n,k):
    comb = fatorial(n)/(fatorial(k)*fatorial(n-k))
    return comb

def pascal6(n):
    '''Entrada = int
       Saida = list
       Calcula uma linha n do triangulo de pascal'''
    res = []
    x = 0
    coef = 1
    while x<=n:
        coef = coef*combinacao(n,x)
        res.append(coef)
        coef = 1
        x = x + 1
    return res 
        
#print(pascal6(0))
#print(pascal6(1))
#print(pascal6(2))
#print(pascal6(3))
#print(pascal6(5))
#print(pascal6(10))
    
    

             