from os import system
from time import sleep

system('cls')
saldo = 0
extrato = ''
numero_saques = 0

while True:
    while 0 < (op:= int(input("[1] Depositar\n[2] Sacar\n[3] Extrato\n[0] Sair\n\n--> "))) > 3:
        system('cls')
        print('Operação inválida, por favor selecione novamente a operação desejada.')
        sleep(2)
        system('cls')
    
    match op:
        case 1:
            system('cls')
            if (valor := float(input("Informe o valor do depósito: "))) > 0:
                saldo += valor
                extrato += f'Déposito: R$ {valor:.2f}\n'
            else:
                system('cls')
                print("Operação falhou! O valor informado é inválido.")
                sleep(2)
                system('cls')

        case 2:
            system('cls')
            if (valor := float(input("Informe o valor do saque: "))) > saldo:
                print('Operação falhou! Você não tem saldo suficiente.')
            elif valor > (limite:=500):
                print('Operação falhou! O valor do saque excede o limite.')
            elif numero_saques >= (LIMITE_SAQUES := 3):
                print('Operação falhou! Número máximo de saques excedido.')
            elif valor > 0:
                saldo -= valor
                extrato += f'Saque: R${valor:.2f}\n'
                numero_saques += 1
            else:
                print('Operação falhou! O valor informado é inválido.')
                sleep(2)
                system('cls')

        case 3:
            system('cls')
            print('='*7 + ' EXTRATO ' + '='*7)
            print('Não foram realizadas movimentações' if not extrato else extrato)
            print(f'\nSaldo: R${saldo:.2f}')
            print('='*23)
            sleep(4)
            system('cls')

        case 0:
            break

    system('cls')