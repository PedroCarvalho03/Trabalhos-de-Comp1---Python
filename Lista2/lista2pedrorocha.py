def sinal1(n1,n2):
    '''Entrada : int,float
        Saida : int
        Mostra se dois numeros possuem o mesmo sinal ou nao '''
    if n1>=0 and n2>=0 :
        sinal = 1
    elif n1<0 and n2<0:
        sinal=1
    else :
        sinal =2
    return sinal
        
#print(sinal1(2,5))
#print(sinal1(-4,1))
#print(sinal1(-7,-9))
#print(sinal1(16,-8))

def redeneural2(x):
    '''Entrada : int,float
       Saida : int,float
       Calcular o valor de y em funcao de x de um grafico de uma rede neural'''
    if x<=-1:
        y = -1
    elif -1<x<=1:
        y = x
    else :
        y = 1
    return y

#print(redeneural2(0.5))
#print(redeneural2(-0.5))
#print(redeneural2(1))
#print(redeneural2(2))
#print(redeneural2(-2))

def conversorTemp3(temp,sinalcont):
    '''Entrada: int,float
       Saida: float
       Conversor de unidade de temperatura Celsius, Fahrenheit, Kelvin'''
    if sinalcont == 1:
        tempconv = (9*temp)/5 + 32
    elif sinalcont == 2:
        tempconv = temp + 273
    elif sinalcont == 3:
        tempconv = (5*(temp-32))/9
    elif sinalcont == 4:
        tempconv = (5*(temp-32))/9 + 273
    elif sinalcont == 5:
        tempconv = temp - 273
    elif sinalcont == 6:
        tempconv = (9*(temp-273))/5 + 32
    return tempconv

#print(conversorTemp3(40,1))
#print(conversorTemp3(40,2))
#print(conversorTemp3(104,3))
#print(conversorTemp3(104,4))
#print(conversorTemp3(313,5))
#print(conversorTemp3(313,6))
 
def vetor4(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    if a9 == 1 and (a1+a2+a3+a4+a5+a6+a7+a8)%2 == 0:
        mensagem = True
    elif a9 == 1 and (a1+a2+a3+a4+a5+a6+a7+a8)%2 == 1:
        mensagem = False
    elif a9 == 0 and (a1+a2+a3+a4+a5+a6+a7+a8)%2 == 1:
        mensagem = True
    else :
        mensagem = False
    return mensagem
        
#print(vetor4(1,1,1,1,1,1,1,1,1))
#print(vetor4(1,1,1,1,1,1,1,1,0))
#print(vetor4(1,1,0,0,1,0,0,0,1))
#print(vetor4(0,1,0,1,1,1,0,1,0))

def distancia5(p1,p2,p3):
    '''Entrada : int,float
       Saida : float
       Calcular a maior distancia 2 a 2 entre 3 pontos distintos numa reta real '''
    d1 = ((p1-p2)**2)**(1/2)
    d2 = ((p1-p3)**2)**(1/2)
    d3 = ((p2-p3)**2)**(1/2)  
        
    if d1>d2 and d1>d3 :
        return d1
    elif d2>d1 and d2>d3:
        return d2
    else :
        return d3
    
#print(distancia5(-1,-2,-3))
#print(distancia5(5,10,1))
#print(distancia5(2,-4,7))
#print(distancia5(1,3,-1))
#print(distancia5(9,9,15))

def ContaAgua6(cons):
    ''' Entrada = int
        Saida = float
        Calcula o valor da conta de agua e o valor de 2 faixas de cobrancas '''
    if 0<=cons<=15:
        valorconta = 10
        faixa2 = 0
        faixa3 = 0
    elif 15<cons<=40:
        valorconta = 10 + (cons-15)*1.2
        faixa2 = (cons-15)*1.2
        faixa3 = 0
    elif cons>40:
        valorconta = 10 + 25*(1.2) + (cons-40)*3
        faixa2 = 25*(1.2)
        faixa3 = (cons-40)*3
    return valorconta,faixa2,faixa3

#print(ContaAgua6(12))
#print(ContaAgua6(15))
#print(ContaAgua6(20))
#print(ContaAgua6(40))
#print(ContaAgua6(45))

def entrega7(d1,d1p,dp2,cons,l0,lr):
    '''Entrada : int,float
       Saida: float
       retorna se as entregas em um determinado trajeto foram realizadas, a quantidade de\
       entregas e a gasolina restante no tanque ao final das entregas'''
    if type(d1)!=int and type(d1)!=float\
    or type(d1p)!=int and type(d1p)!=float\
    or type(dp2)!=int and type(dp2)!=float:
        return -1
    elif d1<0 or d1p<0 or dp2<0:
        return -1
    elif type(cons)!=int and type(cons)!=float\
         or type(l0)!=int and type(l0)!=float\
         or type(lr)!=int and type(lr)!=float:
        return -2
    elif cons<0 or l0<0 or lr<0 :
        return -2
    elif l0>60:
        return -3
    #Gasolina
    lparte1 = 0
    lrestante = 0
    if (l0+lr) - (d1+d1p)*cons<=60:
        lparte1 = (l0+lr) - (d1+d1p)*cons
    elif (l0+lr) - (d1+d1p)*cons>60:
        lparte1 = 60
        
    if (lparte1+lr) - (2*dp2)*cons<=60  :
        lrestante = ((lparte1+lr) - (2*dp2)*cons) - (d1+d1p)*cons
    elif (lparte1+lr) - (2*dp2)*cons>60  :
        lrestante = 60 - (d1+d1p)*cons
    #Entrega
    entrega = False
    quantentrega = 0
    if (l0+2*lr)*(1/cons)>2*(d1+d1p+dp2):
        entrega = True
        quantentrega = 2
         
    elif l0*(1/cons)<d1 :
        entrega = False
        quantentrega = 0
        lrestante = 0
    elif l0*(1/cons)<(d1+d1p) or (l0+lr)*(1/cons)<(d1+d1p+dp2) :
        entrega = False
        quantentrega = 1
        lrestante = 0
    elif (l0+lr)*(1/cons)>=(d1+d1p+dp2):
        entrega = False
        quantentrega = 2
        lrestante = 0
    return entrega,quantentrega,lrestante
        
     
#print(entrega7('100',-200,35.7,0.05,20,15))
#print(entrega7(200,100,300,-0.003,20,'25'))
#print(entrega7(137.5,42,225.71,0.08,70,20))
#print(entrega7(200,100,100,0.05,20,15))
#print(entrega7(200,100,400,0.05,60,20))
#print(entrega7(200,100,100,0.05,20,40))
#print(entrega7(200,100,300,0.05,20,15))
#print(entrega7(200,300,100,0.05,25,15))
#print(entrega7(200,100,200,0.05,10,15))
#print(entrega7(200,100,200,0.05,15,5))
#print(entrega7(200,100,200,0.05,8,15))