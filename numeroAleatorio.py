'''
Write a program that, when started, generates a random value from 1 to 10 and allows
the user guesses a number until the random value generated at the beginning of the program
is kicked correctly. The program mus inform whether the kick was above, below or equal to
the random value generated at the beginning of the program.
'''

'''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que
o usuário chute um número até que o valor aleatório gerado no início do programa seja
chutado corretamente. O programa deve informar se o chute foi acima, abaixo ou igual ao
valor aleatório gerado no início do programa.
'''

import random

number = random.randint(1,10)

kick = int(input("Arrisque um valor: "))
while kick != number:
    if kick > number:
        print("Valor do chute é muito alto!")
        kick = int(input("Arrisque outro valor: "))
    if kick < number:
        print("Valor do chute é muito baixo!")
        kick = int(input("Arrisque outro valor: "))
        

print("Você acertou o numero!")

