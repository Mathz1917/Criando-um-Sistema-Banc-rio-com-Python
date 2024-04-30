import time
saldo = float(1000)
n_saques = 0
MAX_SAQUES = 3
extratos = ''
nome = input('Qual o seu nome?\nR= ')
msg = f'''
    ============== MENU ==============

    1 - Depósito
    2 - Saque
    3 - Extrato
    4 - Sair

    ==================================
    '''
while True:
    print(msg)

    escolha = input('Digite uma das opções acima: ')

    match escolha :
        case '1':
            dep = float(input('Qual o valor do depósito: R$'))
            if dep > 0:
                saldo+= dep
                print(f'Operação concluída!')
                
                time.sleep(2)
                input('\nAperte qualquer tecla para retornar ao menu.')
                extratos += f'Depósito: R$ {dep:.2f}\n'
            else:
                print('Não é possível depositar valores negativos!')
                time.sleep(3)
                input('\nAperte qualquer tecla para retornar ao menu e tentar novamente.')
        case '2':
            saque = float(input('Digite o valor do saque: R$'))
            if saque > 0:
                if saque <= saldo:
                    if saque <= 500: 
                        if n_saques < MAX_SAQUES:
                            saldo -= saque 
                            n_saques += 1
                            print('Saque concluído com sucesso!')
                            time.sleep(2)
                            print(f'{n_saques} de 3 saques diários realizados.')
                            time.sleep(2)
                            input('\nAperte qualquer tecla para retornar ao menu.')
                            extratos += f'Saque: R$ {saque:.2f}\n'
                        else:
                            print(f'{nome}, você atingiu o número máximo de saques diários.')
                            time.sleep(3)
                            input('\nAperte qualquer tecla para retornar ao menu.')
                    else:
                        print('O limite para saques é de R$ 500!')
                        time.sleep(3)
                        input('\nAperte qualquer tecla para retornar ao menu.')
                else:
                    print(f'{nome}, você não tem saldo suficiente!')
                    time.sleep(3)
                    input('\nAperte qualquer tecla para retornar ao menu.')
            else:
                print('\nNão é possível realizar um saque negativo!')
                time.sleep(3)
                input('\nAperte qualquer tecla para retornar ao menu.')
        case '3':
            print(extratos)
            print(f'Saldo: R$ {saldo:.2f}')
            time.sleep(2)
            input('\nAperte qualquer tecla para retornar ao menu.')
        case '4':
            break
        case _:
            print('Opção inválida, por favor digite novamente o nº da opção desejada!')
            time.sleep(3)

print(f'\nObrigado, tenha um bom dia {nome}!\n')
