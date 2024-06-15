menu = """
Bem vindo ao banco, para seguir com as operações basta digitar o número correspondente a operação que gostaria de realizar:

                                [1] Deposito                     [2] Saque

                                [3] Extrato                      [4] Sair

=>    """

saldo = 0
limite = 500
historico = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("\nDepósito")
        while True:
            try:
                deposito = float(input("\nInsira a quantia que gostaria de depositar: "))
                if deposito <= 0:
                    print("\nPor favor, insira um valor positivo.")

                else:
                    saldo += deposito
                    historico += f"Depósito: +R$ {deposito:.2f}\n"
                    print(f"\nObrigado por utilizar o nosso banco, seu novo saldo é de R$ {saldo:.2f}")
                    break

            except ValueError:
                print("\nEntrada inválida. Por favor insira um valor numérico válido.")

    elif opcao == "2":
        print("\nSaque")
        if numero_saques >= LIMITE_SAQUES:
            print("Operação cancelada, número de saques diários atingido.\n")
            input("\nPressione Enter para voltar ao menu.")
            continue
        while True:
            try:
                saque = float(input("\nInsira a quantia que gostaria de sacar: "))
                if saque <= 0:
                    print("\nPor favor, insira um valor positivo.")

                else:
                    if saque <= saldo:
                        if saque <= limite:
                            historico += f"Saque: -R$ {saque:.2f}\n"
                            saldo -= saque
                            numero_saques += 1
                            print(f"""
                                Por favor, retire o seu dinheiro

                                Obrigado por utilizar o nosso banco.                            
                            """)
                            break
                        else:
                            print("\nValor excede o limite diário de saque")
                            break
                    else:
                        print("\nNão foi possível realizar a operação. Motivo: Saldo insuficiente.")
                        break
            except ValueError:
                print("\nEntrada inválida. Por favor insira um valor numérico válido.")
    elif opcao == "3":
        if historico == "":
            print("\nNão foram realizadas movimentações.")
        else:
            print("\nExtrato\n")
            print(historico)
            print(f"Saldo: R${saldo:.2f}")

    elif opcao == "4":
        print("\nSair")
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")