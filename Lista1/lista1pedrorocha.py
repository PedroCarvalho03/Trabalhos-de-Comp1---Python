def gorjeta1(item1,item2,item3,item4,item5) :
    ''' Entrada = int, float
       Saida = int, float 
       Calcula o valor total de 5 itens de um restaurante
       com a gorjeta'''
    valorItens = item1+item2+item3+item4+item5
    valorTotal = valorItens+valorItens*0.1
    return valorTotal

#print(gorjeta1(1,2,3,4,5))
#print(gorjeta1(5,5,4,6,10))
#print(gorjeta1(10,10,10,10,10))

def progressaogeometrica2(a1,razao,numtermos):
    ''' Entrada = int, float
        Saida = float 
        Calcula a soma de uma PG de n termos '''
    somaPG = (a1*(razao**numtermos-1))/(razao-1)
    return somaPG

#print(progressaogeometrica2(2,2,7))
#print(progressaogeometrica2(1,0.5,10))
#print(progressaogeometrica2(0.2,3,5))
#print(progressaogeometrica2(0.1,1.5,20))

def conversorMpes3(tamanhoM):
    ''' Entrada = int, float
        Saida = float
        Conversor de metro(M) para pes(FT) ''' 
    tamanhoFT = (1*tamanhoM)/0.3048
    return tamanhoFT

#print(conversorMpes3(10))
#print(conversorMpes3(1.8))
#print(conversorMpes3(0.5))

def funcao4(x):
    ''' Entrada = int, float
        Saida = float
        Calcula uma funcao matematica de y em funcao de x '''
    y1 = (( x**(4/5)+9*x)/3+(7*x**2-100))/(2*x**3+10*x+3)
    y2 = (8*x*(12*x**(2/3)-x**4))/(20*x+7)
    y = y1-y2
    return y 

#print(funcao4(1))
#print(funcao4(2))
#print(funcao4(5))
#print(funcao4(8))
#print(funcao4(0.1))
#print(funcao4(0.278))

def Centena5(numero):
    ''' Entrada = int
        Saida = float
        Descobre a quantidade de centenas de um numero 
        de ate 4 digitos '''
    unidade = numero%10
    dezena = ((numero - unidade)/10)%10
    centena = ((numero - (dezena*10 + unidade))/100)%10
    return centena

#print(Centena5(22))
#print(Centena5(857))
#print(Centena5(3219))

def variancia6(valor1,valor2,valor3,valor4):
    ''' Entrada = inte, float
        Saida = float
        Calcula a variancia de 4 valores '''
    media = (valor1 + valor2 + valor3 + valor4)/4
    variancia = ((valor1-media)**2+(valor2-media)**2+(valor3-media)**2+(valor4-media)**2)/4
    return variancia

#print(variancia6(5,0,1,2))
#print(variancia6(5,1,1,-3))
#print(variancia6(4.5,1.5,2,3))
#print(variancia6(4,2,4,-0.5))

def exponencial7(x):
    ''' Entrada = int, float
        Saida = float
        Calcular a exponcial natural ate 6 termos '''
    exponencial = x**0/1 + x**1/1 + x**2/2 + x**3/6 + x**4/24 + x**5/120
    return exponencial

#print(exponencial7(0.5))
#print(exponencial7(1))
#print(exponencial7(2))
