'''
Projeto - Medidor de Velocidade

Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que
representa a velocidade e com base nessa velocidade diga se ele tomou um multa leve, grave ou gravíssima. Levando em consideração que se a
pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve",
caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima,
exiba: "levou multa gravíssima".
'''

velocidadeMaxima = 80.0

velocidadeUsuario = float(input("Digite a velocidade: "))
if velocidadeUsuario <= velocidadeMaxima:
    print("Não houve multa!")
elif velocidadeUsuario > velocidadeMaxima and velocidadeUsuario <= (velocidadeMaxima+10):
    print("Levou multa leve!")
elif velocidadeUsuario >= (velocidadeMaxima+11) and velocidadeUsuario <= (velocidadeMaxima+20):
    print("Levou multa grave!")
elif velocidadeUsuario > (velocidadeMaxima+20):
    print("Levou multa gravíssima!")
