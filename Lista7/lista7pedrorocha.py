def cadastro(): #  1 opcao 
    tuplaTdClientes = () #Tupla com todos os clientes
    Loop = '' #Fazer o loop
    while Loop != 'n':
        tuplaCadastro = () #Tupla com um unico cliente
        NomeCl = input('Digite o nome da cliente: ')
        NomeAn = input('Digite o nome do animal: ')
        Especie = input('Digite a especie do animal: ')
        Idade = int(input('Digite a idade do animal (anos): '))
        Peso = float(input('Digite o peso do animal (kg): '))
        Loop = input('Deseja inserir outro cliente?(s/n) ')
        tuplaCadastro = tuplaCadastro + (NomeCl,) + (NomeAn,) + (Especie,)
        tuplaCadastro = tuplaCadastro + (Idade,) + (Peso,)
        tuplaTdClientes = tuplaTdClientes + (tuplaCadastro,)
    return tuplaTdClientes

def cadastrados(tupla): # 2 opcao
    resultado = ''
    if len(tupla) == 0 :
        print('Nao ha clientes cadastrados')
    else:
        for i in range(len(tupla)):
            nome = tupla[i][0]
            animal = tupla[i][1]
            especie = tupla[i][2]
            idade = tupla[i][3]
            peso = tupla[i][4]
            resultado = resultado + 'Dono: %s ; Animal: %s ; Especie: %s ; Idade: %d ano(s) ; Peso: %.2f kg \n'%(nome,animal,especie,idade,peso)
        
    return resultado

def especie(tupla): # 3 opcao
    resultado = ''
    if len(tupla) == 0:
        print('Nao ha clientes cadastrados')
    else:
        buscaEs = input('Digite a especie que deseja procurar: ')
        buscaEsMin = buscaEs.lower()
        for k in range(len(tupla)):
            especieMinuscula = tupla[k][2].lower()
            if buscaEsMin == especieMinuscula :
                nome = tupla[k][0]
                animal = tupla[k][1]
                idade = tupla[k][3]
                peso = tupla[k][4]
                resultado = resultado + 'Cliente: %s ; Animal: %s ; Idade: %d ano(s)  Peso: %.2f kg \n'%(nome,animal,idade,peso)
            
            else :
                resultado = resultado + 'Especie nao encontrada'
    
    return resultado

def clientes(tupla):# 4 opcao
    resultado = ''
    buscaCl = input('Digite o nome do cliente: ')
    buscaClMin = buscaCl.lower()
    for j in range(len(tupla)):
        if buscaClMin == tupla[j][0].lower() :
            animal = tupla[j][1]
            especie = tupla[j][2]
            idade = tupla[j][3]
            peso = tupla[j][4]
            resultado = resultado + 'Animal: %s ; Especie: %s ; Idade: %d ano(s) ; Peso: %.2f kg \n'%(animal,especie,idade,peso)
            
        else :
            resultado = resultado + 'Cliente nao encontrado'
    
    return resultado

def EliminarClientes(tupla): #5 opcao
    frase1 = ''
    frase2 = ''
    pergunta2 = ''
    tuplaEliminado = ()
    tuplaBuscado = ()
    tuplaResultado = ()
    cont = 0
    boole = True
    while boole == True:
        BuscaCliente = input('Digite o nome do cliente: ')
        for l in range(len(tupla)):
            if BuscaCliente == tupla[l][0]:
                cont = cont + 1
                tuplaBuscado = tuplaBuscado + (tupla[l],)
        if cont == 0:
            print('Cliente nao encontrado')
            boole = False
                
        if cont>0:
            frase1 = frase1 + '%d cliente(s) encontrados'%(cont) 
            print(frase1)
        pos = 0
        while pos<len(tuplaBuscado):
            nome = tuplaBuscado[pos][0]
            animal = tuplaBuscado[pos][1]
            especie = tuplaBuscado[pos][2]
            idade = tuplaBuscado[pos][3]
            peso = tuplaBuscado[pos][4]
            frase2 = 'Cliente: %s ; Animal: %s ; Especie: %s ; Idade: %d ano(s) ; Peso: %.2f kg \n'%(nome,animal,especie,idade,peso)
            print(frase2)
            pergunta1 = input('Deseja excluir este cliente?(s/n) ')
            if pergunta1 == 's' :
                tuplaEliminado = tuplaEliminado + (tuplaBuscado[pos],)
                pos = pos + 1
            elif pergunta1 == 'n':
                pos = pos + 1
        if boole != False:
            pergunta2 = input('Deseja excluir outro cliente?(s/n) ')
        if pergunta2 == 'n':
            boole = False
            
    for l1 in range(len(tupla)):
        if tupla[l1] not in tuplaEliminado :
            tuplaResultado = tuplaResultado + (tupla[l1],)
    tupla = tuplaResultado
    return ''
def questao1():
    tupla = () 
    Opcao = 0
    while Opcao != 6:
        print('1 - Inserir um ou mais cliente(s)')
        print('2 - Mostrar a lista de clientes')
        print('3 - Listar clientes de uma especie')
        print('4 - Listar animais de um cliente')
        print('5 - Remover um ou mais cliente(s)')
        print('6 - Sair')
        Opcao = int(input('Digite uma opcao: '))
        if Opcao == 1 :
            tupla = tupla + cadastro()
        elif Opcao == 2 :
            print(cadastrados(tupla))
        elif Opcao == 3 :
            print(especie(tupla))
        elif Opcao == 4 :
            print(clientes(tupla))
        elif Opcao == 5 :
            print(EliminarClientes(tupla))
    return tupla
#print(questao1())
 