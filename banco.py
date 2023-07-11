saldo = 0.0
tot_depositos = 1
extrato = ""

menu = """

Olá! Seja bem-vindo ao Menu de atendimento do Banco Cash

Digite as seguintes opções que desejar:

1 - Operação de Depósito

2 - Operação de Saque

3 - Operação de Extrato

4 - Sair


"""

while True:

    opcao = int(input(menu))

    if opcao == 1:

        print("Digite o valor a ser depositado:")

        valor_deposito = float(input())

        if (valor_deposito <= 0):
            print("Impossível depositar valores negativos ou iguais a zero.")

        else :
            saldo += valor_deposito
            extrato = extrato + f"Depósito de R${valor_deposito:.2f} foi realizado\n"
            print("Operação efetuada!")

    elif opcao == 2:

        if(tot_depositos <= 3):

            valor_saque = float(input("Digite o valor a ser sacado: \n"))

            if(valor_saque > 500):

                print("Impossível realizar saques superiores a R$500,00")

            else:

                if(valor_saque > saldo):

                    print("Impossível sacar este valor, por favor verifique seu extrato.")

                else:

                    saldo -= valor_saque
                    extrato = extrato + f"Saque de R${valor_saque:.2f} foi realizado\n"
                    tot_depositos = tot_depositos + 1
                    print("Operação efetuada")
        else:
            print("Limite de 3 saques diários atingido")
        


    elif opcao == 3:

        if(extrato == ""):
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"\nO saldo atual da sua conta é de R${saldo:.2f}")


    elif opcao == 4:

       print("Operação finalizada, obrigado por ser nosso cliente! Até mais!") 
       break

    else:
        print("Opção inválida, por favor digite novamente")

