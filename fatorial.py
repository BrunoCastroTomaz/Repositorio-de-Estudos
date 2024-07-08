# create a program that takes a number and prints the factorial of that number
# crie um programa que recebe um número e imprime o fatorial daquele número

number = int(input("Enter a number: "))
if number < 0:
	print("Numero inválido!")
elif number == 0:
	print(f"Fatorial de {number} é 1!")
else:
	factorial = 1
	for i in range(1, number+1):
		factorial *= i
	print(f"Fatorial de {number} é {factorial}!")
