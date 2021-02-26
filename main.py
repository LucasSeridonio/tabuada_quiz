import csv
import datetime
import random
import time

pontuacao = 0
acertos = 0
erros = 0

fieldnames=['nome', 'pontos', 'acertos', 'erros', 'data']

jogador = input("Nome do Jogador: > ")
print()

with open('./pontuacao.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, fieldnames = fieldnames)
    for registro in csv_reader:
        if jogador.lower() == str(registro['nome']).lower():
            pontuacao = int(registro['pontos'])
            acertos = int(registro['acertos'])
            erros = int(registro['erros'])

print('Comecando o jogo com:')
print(f' - Acertos: {acertos}')
print(f' -- Erros: {erros}')
print(f' --- Pontos: {pontuacao}\n')

while True:
	x = random.randint(0,10)
	y = random.randint(0,10)
	print(f'Quanto é {x} x {y}?')

	resultado = input('Resultado: ')

	if resultado == 'sair':
		print()
		break

	resultado = int(resultado)

	if resultado == x*y:
		pontuacao += 1
		acertos +=1
		print(f'Voce acertou e ganhou 1 ponto! Sua pontuacao é de: {pontuacao}')

	else:
		pontuacao -= 2
		print(f'Voce errou e perdeu 2 pontos! Sua pontuacao é de: {pontuacao}')
		print(f'{x} x {y} = {x*y}')
		erros +=1

	print('\n')

print('Seu resultado foi:')
print(f' - {acertos} acertos')
print(f' -- {erros} erros')
print(f' --- {pontuacao} PONTOS!')

with open('./pontuacao.csv', 'a') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writerow({'nome': str(jogador), 'pontos': int(pontuacao), 
           'acertos': int(acertos), 'erros': int(erros), 'data': datetime.datetime.today()})

print('Salvando resultados ... ')

time.sleep(5)

















