import random

PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32, ]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

S1 = [[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
      [0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
      [4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
      [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]]

S2 = [[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
      [3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
      [0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
      [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]]

S3 = [[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
      [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
      [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
      [1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]]

S4 = [[7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
      [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
      [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
      [3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]]

S5 = [[2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
      [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
      [4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
      [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]]

S6 = [[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
      [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
      [9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
      [4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]]

S7 = [[4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
      [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
      [1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
      [6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]]

S8 = [[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
      [1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
      [7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
      [2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]]

# IP^-1 ou Inverso da Permutação inicial ou Permutação final
PF = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]


def mostrarAjuda():
    print("\nFormate a entrada em uma linha, separando cada parametro com o caractere \"|\"\n")
    print("Primeiro parametro: Informe o texto a ser cifrado em hexadecimal")
    print("Segundo parametro:  Informe a primeira chave (64 bits em hexadecimal)")
    print("Terceiro parametro: Informe a segunda chave caso queira utilizar o 3-DES ou;")
    print("                    Não informe este parâmetro caso queria utilizar o DES simples")
    print("Ultimo parametro:   Informe o caractere \"D\" caso queira decifrar, deixe em branco caso queira cifrar\n")
    print("Caso precise gerar uma chave, digite \"chave\"")
    print("Caso precise traduzir o texto claro para hexadecimal, digite \"hex\" e em seguida digite o texto claro")


def gerarChave():
    chave = ''
    # Passa pelo processo abaixo 8 vezes, gerando 8 bits em cada iteração para construir uma chave de 64 bits
    for _ in range(8):
        # Gera um número aleatório em decimal que vai de 0000000 até 1111111 em binário
        numero = random.randint(0, 127)

        if debug:
            print('Chave - Inteiro aleatório:', numero)

        # Converte o número gerado para binário e preeche os zeros a esquerda caso necessário
        binario = bin(numero)[2:]
        binario = '0000000'[len(binario):] + binario

        # Conta a quantidade de bits '1' no número
        quantidade = 0
        for c in binario:
            if c == '1':
                quantidade += 1

        # Caso a quantidade de bits '1' seja par adiciona o bit '0' no final, caso contrário adiciona '1'
        if quantidade % 2 == 0:
            binario += '0'
        else:
            binario += '1'

        if debug:
            print('Chave - Digito em binário com pariedade:', binario)

        # Adiciona os 8 bits na chave
        chave += binario
    print(hex(int(chave, 2))[2:])


def traduzirTexto():
    t = input()

    # Processo de converter caractere ascii para hexadecimal
    hexa = ""
    for caracter in t:
        hexa += hex(ord(caracter))[2:]

    if debug:
        print(bin(int(hexa, 16))[2:])
    print(hexa)


def permutacaoInicial(bloco):
    # Declaração de váriaveis que são utilizadas para garantir as regras da permutação
    incial = 6
    contador = incial
    esquerda = ''

    # Itera sobre os 32 primeiros bits (esquerda do bloco) permutando eles para produzir a saída desejada
    for _ in range(32):
        esquerda += bloco[63-contador]
        contador += 8
        if contador > 64:
            incial -= 2
            contador = incial

    # Declaração de váriaveis que são utilizadas para garantir as regras da permutação
    incial = 7
    contador = incial
    direita = ''

    # Itera sobre os 32 ultimos bits (direita do bloco) permutando eles para produzir a saída desejada
    for _ in range(32):
        direita += bloco[63-contador]
        contador += 8
        if contador > 64:
            incial -= 2
            contador = incial

    return esquerda, direita


def obterSubchave(round, chaveE, chaveD):
    # Implementação das regras de rotação
    qnt = 2
    if round == 1 or round == 2 or round == 9 or round == 16:
        qnt = 1

    # Aplicando a rotação a esquerda
    chaveE = chaveE[qnt:]+chaveE[: qnt]
    chaveD = chaveD[qnt:]+chaveD[: qnt]

    chave = chaveE+chaveD

    # Permutação da chave utilizando "Permuted choice 2" ignorando 8 bits
    chavePermutada = ''
    for i in range(48):
        chavePermutada += chave[PC2[i]-1]

    if debug:
        print(f'Chave - Subchave #{round}:', chavePermutada)

    return chaveE, chaveD, chavePermutada


def obterSubchaveInverso(round, chaveE, chaveD):
    # Implementação das regras de rotação inversas
    qnt = 2
    if round == 1 or round == 8 or round == 15 or round == 16:
        qnt = 1

    # Aplicando a rotação a esquerda
    chaveE = chaveE[qnt:]+chaveE[:qnt]
    chaveD = chaveD[qnt:]+chaveD[:qnt]

    chave = chaveE+chaveD

    # Permutação da chave utilizando "Permuted choice 2" ignorando 8 bits
    chavePermutada = ''
    for i in range(48):
        chavePermutada += chave[PC2[i]-1]

    if debug:
        print(f'Chave - Subchave #{round}:', chavePermutada)

    return chaveE, chaveD, chavePermutada


def e(texto):
    resultado = ''

    # Permutação do texto usando a tabela "e"
    for i in range(48):
        resultado += texto[E[i]-1]

    return resultado


def s(texto, s):
    # linha recebe o primeiro e o ultimo bit
    linha = texto[0]+texto[-1]
    # coluna recebe os bits do meio
    coluna = texto[1:5]

    # conversão de binário para decimal
    linha = int(linha, 2)
    coluna = int(coluna, 2)

    # recebendo o resultado da função em binário
    decimal = s[linha][coluna]

    # Convertendo o resultado para binário com 0 à esquerda
    binario = bin(decimal)[2:]
    binario = '0000'[len(binario):] + binario

    return binario


def p(texto):
    resultado = ''

    # Permutação do texto usando a tabela "p"
    for i in range(32):
        resultado += texto[P[i]-1]

    return resultado


def cifraDeFistel(texto, chave):
    # Realizando a permutação "e" no texto, passando de 32 bits para 48
    texto = e(texto)

    resultadoXOR = ''
    # Agora é realizado XOR entre o texto permutado e a chave
    for i in range(48):
        resultadoXOR += str(int(texto[i]) ^ int(chave[i]))

    resultadoS = ''
    # Realizando todos os 8 "S" no resultado do XOR
    resultadoS += s(resultadoXOR[:6], S1)
    resultadoS += s(resultadoXOR[6:12], S2)
    resultadoS += s(resultadoXOR[12:18], S3)
    resultadoS += s(resultadoXOR[18:24], S4)
    resultadoS += s(resultadoXOR[24:30], S5)
    resultadoS += s(resultadoXOR[30:36], S6)
    resultadoS += s(resultadoXOR[36:42], S7)
    resultadoS += s(resultadoXOR[42:], S8)

    # Realizando a permutação final e retornando o resultado
    return p(resultadoS)


def realizarRound(round, textoE, textoD, chaveE, chaveD):
    # Função que retorna a subChave que vai ser utilizada no round atual
    if cifra:
        chaveE, chaveD, subChave = obterSubchave(round, chaveE, chaveD)

        # Função que retorna o resultado de F(R,K)
        resultado = cifraDeFistel(textoD, subChave)
    else:
        if len(listaChaves) == 0:
            for i in range(1, 17):
                chaveE, chaveD, subChave = obterSubchave(i, chaveE, chaveD)
                listaChaves.append(subChave)

        resultado = cifraDeFistel(textoD, listaChaves.pop())

    # É realizado o XOR com o resultado da cifra de Fistel com o lado esquerdo do bloco
    novoTextoD = ''
    for i in range(32):
        novoTextoD += str(int(resultado[i]) ^ int(textoE[i]))

    # Permutação
    novoTextoE = textoD

    if debug:
        print(f'Round {round} - Esquerda do bloco:', novoTextoE)
    if debug:
        print(f'Round {round} - Direita do bloco :', novoTextoD)

    return novoTextoE, novoTextoD, chaveE, chaveD


def DES(parametros):
    texto, chave = parametros
    texto = texto.lower()
    chave = chave.lower()

    blocos = []
    bloco = ''

    # Iteração por todos os caracteres presentes no texto
    for i, numero in enumerate(texto, start=1):
        # transformando o numero em binário de 4 bits (com zeros a esquerda)
        binCaractere = bin(int(numero, 16))[2:]
        binCaractere = '0000'[len(binCaractere):] + binCaractere

        # Adiciona o caractere, em binário no bloco
        bloco += binCaractere

        # A cada 16 caracteres você tera 64 bits, então o bloco é salvo e um bloco novo é criado
        if i % 16 == 0:
            blocos.append(bloco)
            bloco = ''

    # Caso o ultimo bloco tenha algo por que o texto não é multiplo de 8, realiza padding usando método "Bit padding"
    if bloco != '':
        bloco = bloco + \
            '1000000000000000000000000000000000000000000000000000000000000000'[
                len(bloco):]
        blocos.append(bloco)

        if debug:
            print("Texto - Ultimo bloco com padding em hex:",
                  hex(int(bloco, 2))[2:])

    if debug:
        print('Texto - Lista de blocos:', blocos)

    # Realizando a permutação inicial em todos os blocos
    blocosEsquerda = []
    blocosDireita = []
    for bloco in blocos:
        blEsquerda, blDireita = permutacaoInicial(bloco)
        blocosEsquerda.append(blEsquerda)
        blocosDireita.append(blDireita)

    if debug:
        print('Texto - Blocos esquerda', blocosEsquerda)
    if debug:
        print('Texto - Blocos direita ', blocosDireita)

    # Conversão de hex para binário na chave informada
    chaveBin = bin(int(chave, 16))[2:]
    chaveBin = '0000000000000000000000000000000000000000000000000000000000000000'[
        len(chaveBin):] + chaveBin

    # Permutação da chave utilizando "Permuted choice 1" e os bits de pariedade são ignorados
    chavePermutada = ''
    for i in range(56):
        chavePermutada += chaveBin[PC1[i]-1]

    if debug:
        print('Chave - Chave permutada:', chavePermutada)

    # Separando a chave em duas metades
    chEsquerda = chavePermutada[:28]
    chDireita = chavePermutada[28:]

    # Realizando os 16 rounds
    for i in range(len(blocos)):
        if debug:
            print('Blocos - Bloco numero', i+1)
        for j in range(1, 17):
            blocosEsquerda[i], blocosDireita[i], chEsquerda, chDireita = realizarRound(
                j, blocosEsquerda[i], blocosDireita[i], chEsquerda, chDireita)

    # Realizando Permutação final
    final = []
    for i in range(len(blocos)):
        # Revertendo a ordem dos blocos uma última vez
        final.append(blocosDireita[i]+blocosEsquerda[i])

        tmp = ''
        for j in range(64):
            tmp += final[i][PF[j]-1]
        final[i] = tmp

    if debug:
        print("Blocos versão final:", final)

    # Convertendo os blocos para uma variável de texto
    resultado = ''
    for bloco in final:
        resultado += bloco

    # Caso foi selecionado o 3-DES, retorna o valor ao invés de printal
    if triple:
        return hex(int(resultado, 2))[2:]

    # Mostrando o resultado para o usuário
    print("Resultado (bin):", resultado)
    print("Resultado (hex):", hex(int(resultado, 2))[2:])


def tripleDES(parametros):
    texto, chave1, chave2 = parametros

    global triple 
    triple = True

    global cifra

    # Verificação do modo cifrar ou decifrar
    if cifra:
        if debug:
            print("3-DES - Encriptação com chave 1")

        # Executa o algoritmo DES com o texto e a chave 1 e retorna o resultado
        texto = DES([texto, chave1])

        if debug:
            print("3-DES - Resultado (bin):", bin(int(texto, 16))[2:])
        if debug:
            print("3-DES - Resultado (hex):", texto)

        # Muda para o modo decifrar
        cifra = False

        if debug:
            print("3-DES - Decriptação com chave 2")

        # Executa o algoritmo DES com o texto e a chave 2 e retorna o resultado
        texto = DES([texto, chave2])

        if debug:
            print("3-DES - Resultado (bin):", bin(int(texto, 16))[2:])
        if debug:
            print("3-DES - Resultado (hex):", texto)

        # Muda devolta para o modo cifrar
        cifra = True

        if debug:
            print("3- DES - Encriptação com a chave 1")

        # Executa o algoritmo DES com o texto e a chave 1 e retorna o resultado
        hexa = DES([texto, chave1])

        # Mostra o resultado final
        print("Resultado (bin)", bin(int(hexa, 16))[2:])
        print("Resultado (hex)", hexa)
    else:
        if debug:
            print("3-DES - Decriptação com chave 1")

        # Executa o algoritmo DES com o texto e a chave 1 e retorna o resultado
        texto = DES([texto, chave1])

        if debug:
            print("3-DES - Resultado (bin):", bin(int(texto, 16))[2:])
        if debug:
            print("3-DES - Resultado (hex):", texto)

        # Muda para o modo cifrar
        cifra = True

        if debug:
            print("3-DES - Encriptação com chave 2")

        # Executa o algoritmo DES com o texto e a chave 2 e retorna o resultado
        texto = DES([texto, chave2])

        if debug:
            print("3-DES - Resultado (bin):", bin(int(texto, 16))[2:])
        if debug:
            print("3-DES - Resultado (hex):", texto)

        # Muda devolta para o modo decifrar
        cifra = False

        if debug:
            print("3- DES - Decriptação com a chave 1")

        # Executa o algoritmo DES com o texto e a chave 1 e retorna o resultado
        hexa = DES([texto, chave1])

        # Mostra o resultado final
        print("Resultado (bin)", bin(int(hexa, 16))[2:])
        print("Resultado (hex)", hexa)


# Váriavel de controle para mostrar partes do processo do algoritmo
debug = True

# Váriavel que controla o modo de execução do programa, cifra ou não
cifra = True
# Váriavel de controle para caso ser triple DES, executar uma porção do código diferente
triple = False

# Cria uma lista de chaves para poder usa-las na ordem inversa, caso precisar decifrar
listaChaves = []

entrada = input()

if (entrada.lower() == "ajuda"):
    mostrarAjuda()

if (entrada.lower() == "chave"):
    gerarChave()

if (entrada.lower() == "hex"):
    traduzirTexto()

else:
    entrada = entrada.split("|")
    print()

    if entrada[-1].lower() == "d":
        entrada.pop()
        cifra = False

    # Caso entrada tenha 2 partes, seleciona método DES (Texto + Chave)
    if (len(entrada) == 2):
        if debug:
            print("Método: DES")

        if len(entrada[1]) == 16:
            DES(entrada)
        else:
            print("Chave com formato errado")

    # Caso entrada tenha 3 partes, seleciona método 3-DES (Texto + 2 Chaves)
    elif (len(entrada) == 3):
        if debug:
            print("Método: 3-DES")
        if len(entrada[1]) == 16 and len(entrada[2]) == 16:
            tripleDES(entrada)
        else:
            print("Chave com formato errado")

input()