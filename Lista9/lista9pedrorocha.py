def estatistica1(lista,string = 'media'):
    media = 0
    soma = 0
    mediana = 0
    posicao = 0
    posicao1 = 0
    somatorio = 0
    variancia = 0
    if string == 'media':
        for valores in lista:
            soma = soma + valores
        media = soma/len(lista)
        return media
    elif string == 'mediana':
        if len(lista)%2 == 1 :
            posicao = int(((len(lista)+1)/2)-1)
            mediana = lista[posicao]
        else:
            posicao = int((len(lista)/2) - 1)
            posicao1 = int(len(lista)/2)
            mediana = (lista[posicao] + lista[posicao1])/2
        return mediana
    elif string == 'variancia':
        for valores in lista:
            soma = soma + valores
        media = soma/len(lista)
        for x in lista :
            somatorio = somatorio + (x - media)**2
        variancia = somatorio/len(lista)
        return variancia
    else :
        return -1

#print(estatistica1([-1.1, -0.5, 2.3]))
#print(estatistica1([-1.1, -0.5, 2.3], 'media'))
#print(estatistica1([-10, -5, -2, 0, 3, 4, 9, 10, 15], 'mediana'))
#print(estatistica1([3.25, 6.45, 7.31, 8.39, 9.61, 10.42, 12.75, 15.11], 'mediana'))
#print(estatistica1([1, 2, 3, 4], 'variancia'))
#print(estatistica1([-10, -7, -3, -1, 3, 6, 10], 'variancia'))
#print(estatistica1([5.6, 7.7, 10.9, 13.4, 16.0], 'media aritmetica'))

def divisao2(listaNum,listaDiv):
    resultado = []
    pos = 0
    pos1 = 0
    while pos < len(listaNum):
        try:
            x = float(listaNum[pos])
            y = float(listaDiv[pos1])
            k = x/y
            resultado.append(k)
        except ValueError:
            pos = len(listaNum)
            resultado = - 1
        except ZeroDivisionError:
            resultado.append('inf')
        except IndexError:
            pos = len(listaNum)
        pos = pos + 1
        pos1 = pos1 + 1
    return resultado
    
#print(divisao2([3, 5, 4, 1], [2, 5, 2, 10]))
#print(divisao2(['10.5', '4', 2.5, 3, '9.1'], ['5', 10, '8', 4.3, '7.8']))
#print(divisao2([3, 4, 5], [1, 2, 'a']))
#print(divisao2([2.3, 4.1], [6.8, 1.9, 3.5, 2.7]))
#print(divisao2([1, 2, 5, 6, 3, 2], [2, 5, 8]))

def dicionario3(dicionario):
    frase = 'Modificando o produto'
    frase1 = 'Criando o produto'
    frase2 = 'Valores Cadastrado: preço =  ,peso =  ,preco/grama =  '
    produto = input('Digite o nome do produto: ')
    boole = False
    lista = []
    try:

        lista = dicionario[produto]
        frase = 'Modificando o produto '+produto+'.'
        print(frase)
        frase2 = 'Valores Cadastrado: preço = '+str(lista[0])+' ,peso = '+str(lista[1])+' ,preco/grama = '+str(lista[2])+''
        print(frase2)
        while boole != True:
            try:
                valor = float(input('Digite o preço desse produto: '))
                if not 0<valor<100:
                    raise ValueError
                else:
                    boole = True
            except ValueError:
                print('Valor invalido, digite um valor maior que 0 e menor que 100.')
        while boole !=False :
            try:
                peso = float(input('Digite o peso: '))
                if not peso>=0:
                    raise ValueError
                elif not peso != 0 :
                    raise ZeroDivisionError
                else:
                    boole = False
            except ValueError:
                print('Valor invalido, digite um numero nao negativo.')
            except ZeroDivisionError:
                print('O peso nao pode ser igual a zero.')   
        lista[0] = valor
        lista[1] = peso
        lista[2] = valor/peso
        dicionario[produto] = lista
    except KeyError:
        frase1 = 'Criando o produto '+produto+'.' 
        print(frase1)
        while boole != True:
            try:
                valor = float(input('Digite o preço desse produto: '))
                if not 0<valor<100:
                    raise ValueError
                else:
                    boole = True
            except ValueError:
                print('Valor invalido, digite um valor maior que 0 e menor que 100.')
        while boole !=False :
            try:
                peso = float(input('Digite o peso: '))
                if not peso>=0:
                    raise ValueError
                elif not peso != 0 :
                    raise ZeroDivisionError
                else:
                    boole = False
            except ValueError:
                print('Valor invalido, digite um numero nao negativo.')
            except ZeroDivisionError:
                print('O peso nao pode ser igual a zero.')
        lista.append(valor)
        lista.append(peso)
        lista.append(valor/peso)
        dicionario[produto] = lista
    return dicionario


#print(dicionario3({'Cookie Bauducco':[3.79, 100, 0.379], 'Oreo':[3.49, 90, 0.038778]}))
        
def questao4(arquivo):
    dicionario = {}
    m1 = ()
    m2 = ()
    m3 = ()
    horas = []
    saida = 1
    pos1 = 0
    pos2 = 1
    pos3 = 2
    ho1 = 0
    ho2 = 0
    ho3 = 0
    dia1 = 0
    dia2 = 0
    dia3 = 0
    try:
        arq= open(arquivo,'r')
        texto = arq.read()
        linhas = texto.split('\n')
        arq.close()
        for ind in range(len(linhas)):
            horas = horas + linhas[ind].split(',')
        while saida <=len(linhas):
            try:
                h1 = float(horas[pos1])
                ho1 = ho1 + h1
                pos1 = pos1 + 3
                dia1 = dia1 + 1

            except ValueError:
                print('tempo indisponivel para a maquina 1')
                pos1 = pos1 + 3
            try:
                h2 = float(horas[pos2])
                ho2 = ho2 + h2
                pos2 = pos2 + 3
                dia2 = dia2 + 1
            except ValueError:
                print('tempo indisponivel para a maquina 2')
                pos2 = pos2 + 3
            try:
                h3 = float(horas[pos3])
                ho3 = ho3 + h3
                pos3 = pos3 + 3
                dia3 = dia3 + 1
            except ValueError:
                print('tempo indisponivel para a maquina 3')
                pos3 = pos3 + 3
            saida = saida + 1
        por1 = 100*(ho1/(dia1*24))
        por2 = 100*(ho2/(dia2*24))
        por3 = 100*(ho3/(dia3*24))
        m1 = m1 + (dia1,por1)
        m2 = m2 + (dia2,por2)
        m3 = m3 + (dia3,por3)
        dicionario['M1'] = m1
        dicionario['M2'] = m2
        dicionario['M3'] = m3
        return dicionario
    except FileNotFoundError:
        print('Arquivo nao encontrado.')
        return -1
        
#print(questao4('exemplo0.txt'))
#print(questao4('texto1.txt'))
#print(questao4('texto2.txt'))        