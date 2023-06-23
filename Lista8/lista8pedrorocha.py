def numRomanos1(num):
    dic = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'}
    resultado = ''
    if num in dic:
        resultado = dic[num]
    else:
        resultado = "''"
    return resultado

#print(numRomanos(1))
#print(numRomanos(10))
#print(numRomanos(13))

def moda2(lista):
    resultado = []
    listaquant = []
    dic = {}
    cont = 0
    quant = 0
    valor0 = 1
    for ind in range(len(lista)):
        quant = 0
        cont = 0
        while cont<len(lista):
            if lista[ind] == lista[cont]:
                quant = quant + 1   
            cont = cont + 1
        dic[lista[ind]] = quant
    for chave in dic:
        listaquant.append(dic[chave])
        valor0 = dic[chave]
    while valor0 != 0:
        if valor0 in listaquant:
            valor0 = valor0+1
        elif valor0 not in listaquant:
            valor0 = valor0 - 1
            for chave1 in dic :
                if valor0 == dic[chave1]:
                    resultado.append(chave1)
            valor0 = 0
              
    return resultado
#print(moda2([1, 1, 2, 3, 4, 1, 4]))
#print(moda2([2.3, 5.1, 7.6, -2.3, 3.9, 5.1]))
#print(moda2(['H01', 'E23', 'A59', 'B72', 'E23', 'O84', 'O84', 'C21']))
#print(moda2([1, 2, 3, 3, 2,1]))

import random

def questao3(num,lista):
    resultado = {}
    for chave in range(1,num+1):
        resultado[chave] = ''
    for chave1 in resultado:
        resultado[chave1]= random.choice(lista)
    return resultado
#random.seed(0)
#print(questao3(5, ['a', 'b', 'c']))
#print(questao3(5, ['a', 'b', 'c','d']))
#print(questao3(10, ['a', 'b', 'c','d','e']))
#print(questao3(15, ['a', 'b', 'c']))


def RPG4(tupla1,tupla2):
    turnos = 1
    resultado = ()
    ataque = 0
    DanoCritico = 0
    Pv1 = tupla1[0]
    Pv2 = tupla2[0]
    dano = 0
    boole = True
    while boole != False:
        ataque = random.randint(tupla1[1],tupla1[2])
        DanoCritico = random.randint(0,100)
        if DanoCritico < tupla1[4]:
            ataque = ataque*2
        dano = ataque - tupla2[3]
        if dano > 0 :
            Pv2 = Pv2 - dano
        
        if Pv2 > 0 :
            ataque = random.randint(tupla2[1],tupla2[2])
            DanoCritico = random.randint(0,100)
            if DanoCritico < tupla2[4]:
                ataque = ataque*2
            dano = ataque - tupla1[3]
            if dano > 0 :
                Pv1 = Pv1 - dano
            if Pv1 <= 0:
                resultado = resultado + (2,Pv2,turnos)
                boole =False
        else :
            resultado = resultado + (1,Pv1,turnos)
            boole = False
        turnos = turnos + 1   
        
    return resultado
#random.seed(0)
#print(RPG4( (10, 5, 6, 8, 0), (5, 1, 2, 0, 5) ))
#print(RPG4( (30, 8, 10, 8, 60), (10, 2, 4, 0, 20) ))
#print(RPG4( (6, 9, 12, 0, 5), (15, 3, 4, 15, 95) ))
#print(RPG4( (20, 3, 10, 0, 10), (20 ,1, 3, 5, 40) ))
#print(RPG4( (20, 7, 15, 5, 10), (10, 3, 8, 5, 30) ))
#print(RPG4( (40, 10, 15, 10, 60), (100, 20, 30, 0, 0)))

def Cr5(dic1,dic2):
    resultado = 0
    totalCred = 0
    totalNota = 0
    for chave in dic1:
        for chave1 in dic2:
            if chave == chave1:
                totalCred = totalCred + dic2[chave1]
                totalNota = totalNota + dic1[chave]*dic2[chave1]
    resultado = totalNota/totalCred
    return resultado
        
#print(Cr5({'Calculo I': 8.0,'Computacao I': 9.5, 'Quimica': 4}, {'Quimica': 2,'Calculo I': 5,'Computacao I': 4, 'Fisica Experimental': 3}))
#print(Cr5({'Calculo I': 8.0,'Computacao I': 9.5, 'Quimica': 4,'Fisica I': 5.1}, {'Fisica I': 5,'Quimica': 2,'Calculo I': 5,'Computacao I': 4, 'Fisica Experimental': 3}))
#print(Cr5({'Quimica': 9.5,'Fis Exp II': 10,'Calculo II': 7.1,'Computacao II':5.5,'Fisica II': 0}, {'Calculo I': 5, 'Fisica II': 4,'Fisica I': 4,'Quimica': 2,'Calculo II':5,'Computacao II': 6, 'Fis Exp II': 1}))

def questao6(tupla):
    resultado = {}
    colocacoes = []
    intervalo = len(tupla[0])
    for ind in range(len(tupla)):
        for ind1 in range(4):
            if tupla[ind][ind1] not in resultado:
                resultado[tupla[ind][ind1]] = []
    for chave in resultado:
        for pos in range(len(tupla)):
            for pos1 in range(4):
                if chave in tupla[pos]:
                    if chave == tupla[pos][pos1]:
                        colocacoes.append(pos1+1)
            if chave not in tupla[pos]:
                colocacoes.append('-')
        resultado[chave] = colocacoes
        colocacoes = []
                                
    return resultado

#print(questao6((('PAL', 'SAN', 'FLA', 'CAM'), ('COR', 'PAL', 'SAN', 'GRE'), ('PAL', 'FLA','INT', 'GRE'),('FLA', 'SAN', 'PAL', 'GRE'), ('FLA', 'INT', 'CAM', 'SAO'), ('CAM', 'FLA','PAL', 'FOR'))))
#print(questao6( (('Bucks', 'Raptors', '76ers', 'Celtics'), ('Bucks', 'Raptors', 'Celtics','Pacers'), ('76ers', 'Nets', 'Bucks', 'Knicks'), ('Heat', 'Celtics', 'Bucks', '76ers')) ))
#print(questao6( (('Warriors', 'Nuggets', 'Trail Blazers', 'Rockets'), ('Lakers', 'Clippers','Nuggets', 'Rockets'), ('Jazz', 'Suns', 'Nuggets', 'Clippers'), ('Suns', 'Grizzlies','Warriors', 'Mavericks')) ))