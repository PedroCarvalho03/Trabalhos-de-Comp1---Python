def checartipo1(lista):
    '''Entrada = list
       Saida = list
       Identificar os tipos dos elementos de uma lista '''
    inte = []
    floate = []
    booleano = []
    for elemento in lista:
        if type(elemento) == int :
            inte.append(elemento)
        elif type(elemento) == float :
            floate.append(elemento)
        else :
            booleano.append(elemento)
    return inte,floate,booleano

#print(checartipo1([2,4,6,8]))
#print(checartipo1([2.1,4.0,6.2,8.5]))
#print(checartipo1([True,False]))
#print(checartipo1([2,4.0,True,True,6.2,8.5,False,1]))

def semrepeticao2(lista):
    '''Entrada = list
       Saida = list
       imprimi uma lista sem numeros repetidos'''
    resultado = []
    resultado.append(lista[0])
    for elemento in lista[1:]:
        if elemento in resultado:
            resultado = resultado + []
        else :
            resultado.append(elemento)
             
    return resultado

#print(semrepeticao2([5,2,3,3,2,4,5,6]))
#print(semrepeticao2([7,7,7,7,7,7]))
#print(semrepeticao2([1,2,3]))

def indice3(lista):
    '''Entrada = list
       Saida = list
       Reposiciona um elemento da lista de acordo com seu indice que eh igual a seu valor'''
    resultado = []
    posicao = 0
    for elemento in lista:
        if elemento > (len(lista)-1) or elemento<-len(lista):
            posicao = False
            resultado.append(posicao)
        else:
            posicao = lista[elemento]
            resultado.append(posicao)
    return resultado
       
#print(indice3([0,1,2,3,4]))  
#print(indice3([4,3,2,1,0]))
#print(indice3([2,-1,0]))
#print(indice3([2,-1,0,-3,1,-2]))
#print(indice3([4,-3,2,-5]))

def media4(lista):
    '''Entrada = list
       Saida = list
       Faz a media aritmetica de posicoes anteriores e posteriores a posicao definida'''
    resultado = []
    media = 0
    if len(lista)>= 2:
        resultado.append(lista[1]/2)
    for n in range(1,len(lista)):
        if n == len(lista)-1:
            resultado.append(lista[len(lista)-2]/2)
        else :
            media = (lista[n-1]+lista[n+1])/2    
            resultado.append(media)
    return resultado   
        
        
#print(media4([4,3,9,1]))
#print(media4([0,2,2]))
#print(media4([-10,7,5,-1,-7,12,-3]))
#print(media4([-1.5,4.2,7.7,-3.1,9.4,0.6]))

def questao5(lista,num,n):
    ''' Entrada = list,int,int
        Saida = list
        Faz a lista se deslocar ou para direita ou para esquerda adicionando zeros '''
        
    zeros = []
    andantes = []
    quant = len(lista)
    resultado = []
    if num == 1:
        for i in range(n):
            zeros = zeros +[0]
        lista = zeros + lista
        for i1 in range(quant):
             resultado = resultado + [lista[i1]]
    
        return resultado
    if num == -1:
        for i in range(n):
            zeros = zeros + [0]
        lista = lista + zeros
        for i1 in range(n,len(lista)):
            resultado = resultado + [lista[i1]]
        return resultado
    
    
    
#print(questao5([-1,2,-7,10,3],1,2))
#print(questao5([-1,2,-7,10,3],1,4))
#print(questao5([-1,2,-7,10,3],-1,1))
#print(questao5([-1,2,-7,10,3],-1,3))
#print(questao5([-1,2,-7,10,3],-1,7))

def questao6(lista):
    '''Entrada = list
       Saida = list
       Calcula a media de idade, altura e peso '''
    resultado = []
    n = len(lista)
    mediaId = 0
    mediaAl = 0
    mediaPe = 0
    soma = 0
    for i in range(n):
        soma = (soma + lista[i][0]) 
    mediaId = soma/n
    resultado.append(mediaId)
    soma = 0
    for i1 in range(n):
        soma = (soma + lista[i1][1])
    mediaAl = soma/n
    resultado.append(mediaAl)
    soma = 0
    for i2 in range(n):
        soma = soma + lista[i2][2]
    mediaPe = soma/n
    resultado.append(mediaPe)
    
    return resultado

#print(questao6([[40,1.60,60],[30,1.80,75]]))
#print(questao6([[27,1.82,72.3],[18,1.71,65.2],[61,1.77,83.1],[55,1.91,92]]))
#print(questao6([[25,1.79,64.4],[32,1.88,79.7],[44,1.82,72.9]]))

def questao7(lista1,lista2):
    '''Entrada = list
       Saida = list
       Faz a multiplicacao entre um elemento da lista1 e a lista2'''
    resultado = []
    mult = []
    n1 = len(lista1)
    n2 = len(lista2)
    valor = 1
    for k in range(n1):
        for i in range(n2):
            valor = lista1[k]*lista2[i]
            mult.append(valor)
            valor = 1
        resultado.append(mult)
        mult = []
        
    return resultado

#print(questao7([-2,3],[10,5]))
#print(questao7([1,3,5,7],[5,6]))
#print(questao7([7],[-2,4,3,12]))
#print(questao7([0.2,1.3,-7.8],[4.9,-12.1,8.6]))

def questao8(lista):
    '''Entrada = list
       Saida = list
       Colocar os valores das sublistas em um intervalo entre 0 e 10 '''
    n = len(lista)
    for i in range(n):
        n1 = len(lista[i])
        for i1 in range(n1):
            if lista[i][i1]<0:
                lista[i][i1] = 0
            elif lista[i][i1] > 10:
                lista[i][i1] = 10
                
    return lista

#print(questao8([[-1,0,5,-4],[-3,8,12,20],[1,2,7,10]]))
#print(questao8([[0,1,2,3],[4,5,6,7],[8,9,10,11]]))
#print(questao8([[20,37,25],[62,-3,41],[11,39,40]]))
#print(questao8([[5,2,7,8,2],[9,3,1,4,4],[7,7,6,2,3]]))