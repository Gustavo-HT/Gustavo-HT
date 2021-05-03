from datetime import datetime, timedelta

vdd = 1
while vdd == 1:
	print('=============== PYSTAR ===============')
	print('[1] Cadastro')
	print('[2] Login')
	opcao = int(input('Digite a opção: '))
	# foi preciso criar esta variavel aqui para dar certo o loop de login e senha errado
	login = ''
	senha = ''

	while opcao == 1:
		cont = 1
		print(5 * '\n')
		print('=============== MENU CADASTRO ===============')
		login = input('Cadastre o Login: ')
		senha = input('Cadastre a Senha: ')
		nome = input('Cadastre o seu nome completo: ')
		#str = string caracter
		telefone = (input('Cadastre o seu telefone: '))
		CPF = (input('Cadestre o seu CPF: '))
		carro1 = (input('Digite modelo do veículo 1: ')).upper()
		placa1 = (input('Digite placa do veículo 1: ')).upper()
		carro2 = (input('Digite modelo do veículo 2: ')).upper()
		placa2 = (input('Digite placa do veículo 2: ')).upper()
		opcao = opcao +1

	while opcao == 2:
		print(5 * '\n')
		print('=============== MENU LOGIN ===============')
		login2 = input('digite o login: ')
		if login2 == login:
			senha2 = input('digite a senha: ')
			if senha2 == senha:
				break
			else:
				print('Senha errada, volte para o login')
				opcao = 1
		else:
			print('login errado')
			opcao = 1
	break

print( f'Bem vindo(a) {nome}')
#usar o for count
saldo = 0
app = 1

while app == 1:
	# inicia as variáveis para não ter problema quando printar o histórico
	cont = 1
	print(5 * '\n')
	print('=============== MENU PRINCIPAL ===============')
	print('Escolha uma das opções: ')
	print('[1] Colocar creditos')
	print('[2] Vizualizar creditos')
	print('[3] Controlar uso')
	print('[4] Vizualizar histórico de utilização')
	print('[5] Encerrar')
	escolha= int(input('Digite a sua opção aqui: '))

	if escolha == 1:
		print('=============== MENU ADICIONAR CREDITOS ===============')
		saldo = float(input('Adicione creditos (ex: 53.50): '))

	elif escolha == 2:
		print('=============== MENU VISUALIZAR CRÉDITOS ===============')
		print(f'Seu saldo é de R${saldo:.2f}')

	elif escolha == 3:
		print('=============== MENU CONTROLE DE USO ===============')
		print('Escolha em qual carro irá utilizar')
		print('[1] Carro 1')
		print('[2] Carro 2')
		opcao_carro = int(input('Digite a opção aqui: '))

		print('====================================================')
		print('Qual a data será utilizada')
		print('[1] Agora')
		print('[2] Agendar data e horário')
		opcao_data = int(input('Digite a opção aqui: '))
		# Se a opção for 1, sera chamada a biblioteca datetime e utilizaremos a data e horário de agora
		# Para obter a informação de data e hora, é preciso formatar para string, passando uma mascara %d/%m%y para obter a data formatada 03/04/21
		# o mesmo se aplica para o horário inicial
		# para o horário final, utilizamos o método timedelta para somar uma hora
		if opcao_carro == 1:
			if opcao_data == 1:
				data_de_utilizacao1 = datetime.now()
				data1 = data_de_utilizacao1.strftime('%d/%m/%y')
				horario_inicial1 = data_de_utilizacao1.strftime('%H:%M')
				horario_final1 = data_de_utilizacao1 + timedelta(hours=1)
				horario_final1 = horario_final1.strftime('%H:%M')
			elif opcao_data == 2:
				data1 = input('digite aqui a data (ex: 05/03/21): ')
				horario_inicial1 = input('digite o horario inicial (ex: 15:49): ')
				horaio_final1 = input('digite o horario final (ex: 16:49): ')

		elif opcao_carro == 2:
			if opcao_data == 1:
				data_de_utilizacao2 = datetime.now()
				data2 = data_de_utilizacao2.strftime('%d/%m/%y')
				horario_inicial2 = data_de_utilizacao2.strftime('%H:%M')
				horario_final2 = data_de_utilizacao2 + timedelta(hours=1)
				horario_final2 = horario_final2.strftime('%H:%M')

			elif opcao_data == 2:
				data2 = input('digite aqui a data (ex: 05/03/21): ')
				horario_inicial2 = input('digite o horario inicial (ex: 15:49): ')
				horaio_final2 = input('digite o horario final (ex: 16:49): ')


		
	elif escolha == 4:
		# vamos validar se as variáveis de data e horário existem no escopo da aplicação
		if not 'data1' in locals():
			data1 = ''
			horario_inicial1 = ''
			horario_final1 = ''
		
		if not 'data2' in locals():
			data2 = ''
			horario_inicial2 = ''
			horario_final2 = ''

		print('=============== HISTÓRICO DE UTILIZAÇÃO ===============')
		print('CARRO   |   PLACA   |   DATA   |   HORÁRIO INICIAL  |  HORÁRIO FINAL')
		print(f'{carro1} |   {placa1} | {data1} |    {horario_inicial1}    |    {horario_final1}')
		print(f'{carro2} |   {placa2} | {data2} |    {horario_inicial2}    |    {horario_final2} ')

	elif escolha == 5:
		print('Para encerrar digite 1')
		print('para continuar digite 2')
		encerrar= int(input('Deseja encerrar o programa?'))
		if encerrar == 1:
			break
		elif encerrar == 2:
			print('programa voltará ao menu')
			cont == 1
		else:
			print('opção inválida, voltará ao menu')
			cont == 1
	else:
		print('opção inválida')

(print('fim do programa, obrigado por usar'))