'''
Autor: Bruno Castro Tomaz

                    CALCULADORA IDADE EM SEGUNDOS

    Este mini- projeto é uma calculadora que informa a sua idade aproximada em segundos.
O programa lida apenas datas de 1º de janeiro de 1990 até o presente. Considera as seguintes infomações:
            ** mês (1- 12)
            ** dia (1 -31)
            ** ano (4 dígitos)

'''
from datetime import timedelta, date

print("Por favor, informe sua data de nascimento conforme exemplo: dd/mm/aa ")
nascimento = input("Data: ")
nascimento = nascimento.split("/")
dia, mes, ano = nascimento
dia = int(dia)
mes = int(mes)
ano = int(ano)
'''
while mes < 1 or mes > 12:
    nascimento = input("Por favor, informe uma data válida: ")
    nascimento = nascimento.split("/")
    dia, mes, ano = nascimento
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
while dia < 1 or dia > 31:
    nascimento = input("Por favor, informe uma data válida: ")
    nascimento = nascimento.split("/")
    dia, mes, ano = nascimento
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
while ano < 1990 or ano > 9999:
    nascimento = input("Por favor, informe uma data válida: ")
    nascimento = nascimento.split("/")
    dia, mes, ano = nascimento
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
'''
#TODO: modular código em funções
#TODO: tratar casos omissos: meses com número fixo de dias (fevereiro e meses com 30 dias), ano bissexto, 

dataAtual = date.today()
print(dataAtual)
#TODO: Utilizar a data de nascimento para criar um objeto datetime
#https://docs.python.org/pt-br/3/library/datetime.html#date-objects

'''
year = timedelta(days=365)
month = timedelta(days=31*mes)
day = timedelta(days=dia)
time
timedelta.total_seconds()
IdadeSegundos = dia*24*60*60 + mes*30*24*60*60 + ano*365*24*60*60
'''
