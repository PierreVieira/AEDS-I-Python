"""
 * Autor: Pierre Vieira
 * Data atual do sistema: 15/08/2019
 * Clion ------> JetBrains IDE
 * Observação: esse programa foi inicialmente feito na sexta-feira 09/08/2019
 * Foram úteis para o desenvolvimento de raciocínio dessa questão os seguintes links abaixo
 * https://www.ime.usp.br/~pf/algoritmos/aulas/aloca.html
 * https://www.ime.usp.br/~fmario/mac2166/challenge/fatorial.html
 * https://youtu.be/ECIvoHU67Q4
 * Acesse meu canal no Youtube: https://www.youtube.com/channel/UCGF4Ag9zGp6newv-tkSkTcA/videos
""" 
def solveThis(numero_em_questao, lista_resultado, tamanho):
    resultado = 0
    counter = 0
    for c in range(tamanho+1):
        op = lista_resultado[c]*numero_em_questao + resultado
        resultado = op//10
        lista_resultado[c] = op%10
        counter += 1
    while resultado != 0:
        lista_resultado.append(resultado%10)
        resultado //= 10
        counter += 1
    counter -= 1
    return counter

lista_resultado = []
tamanho = 0
numero = int(input('Digite um numero inteiro: '))
if numero == 1 or numero == 0:
    print(1)
else:
    lista_resultado.append(1)
    for c in range(numero+1):
        if c > 1:
            tamanho = solveThis(c, lista_resultado, tamanho)
    print("Resultado: ")
    for c in reversed(lista_resultado):
        print(c, end='')
