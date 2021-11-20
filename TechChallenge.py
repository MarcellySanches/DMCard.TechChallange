import time
contador = 0
cont = 0
array_expressoes = []
qtd_expressoes_input = int(input('Digite a quantidade de expressões:\n'))
while (qtd_expressoes_input <= 0):
    print('O número de expressões deve ser maior que 0')
    qtd_expressoes_input = int(input('Digite a quantidade de expressões:\n'))

while(qtd_expressoes_input > 10000) :
    print('A Quantidade de expressões não pode exceder 10.000')
    qtd_expressoes_input = int(input('Digite a quantidade de expressões:\n'))

print('Digite a(s) expressões: ')
# trecho para tratamento da quantidade de caracteres
while(cont < qtd_expressoes_input):
    entrada = input()
    #print(len(entrada))
    if(len(entrada) > 1000):
        print('O número de caracteres deve ser menor ou igual ao mil')
        print('Digite as expressões: ')
    else:
        array_expressoes.append(entrada)
        cont += 1

contador = 0
while (contador < qtd_expressoes_input):
    pilha = []
    flag = False
    for caracter in array_expressoes[contador]:
        if (caracter == '('):
            pilha.append(caracter)
        elif (caracter == ')'):
            if (not pilha):
                flag = True
                contador += 1
                continue
            lastItem = pilha.pop()
            if (lastItem != '('):
                flag = True
                contador += 1
                continue
    #Se flegou como true em algum ponto da execução expressão está incorreta
    if (flag):
        print('incorrect')
        continue
    #Se pilha estiver vazia está correto
    if (not pilha):
        print("correct")
    #se não incorreto
    else:
        print('incorrect')

    contador += 1



