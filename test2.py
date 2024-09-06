# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre 
# será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que 
# desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
# pertence ou não a sequência.

num = float(input('\nDigite um numero: '))
seq2 = 1
seq1 = 0
aux = 0
vetor =[seq1, seq2]

while seq2<num:
    aux= seq1+seq2
    seq1 = seq2
    seq2 = aux
    vetor.append(seq2)
    

if num in vetor:
    print('\nO numero faz parte da seqência')
else:
    print('\nO numero não faz parte da sequência')