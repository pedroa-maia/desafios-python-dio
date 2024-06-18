menu = """
Bem vindo ao banco, para seguir com as operações basta digitar o número correspondente a operação que gostaria de realizar:

                                [1] Deposito                     [2] Saque

                                [3] Extrato                      [4] Sair

=>    """


def validar_input(numero):
    if numero.isdigit():  # Verifica se é um número inteiro
        return True
    elif numero.count('.') == 1:  # Verifica se contém exatamente um ponto decimal
        try:
            float_numero = float(numero)
            if float_numero >= 0:  # Verifica se pode ser convertido para float não-negativo
                return True
        except ValueError:
            pass
    return False


def deposito(saldo, valor_deposito, historico):
    if not validar_input(valor_deposito):
        print("\nEntrada inválida. Por favor, insira um valor numérico positivo.")
        return saldo, historico

    deposito = float(valor_deposito)
    saldo += deposito
    historico += f"Depósito: +R$ {deposito:.2f}\n"
    print(f"\nObrigado por utilizar o nosso banco, seu novo saldo é de R$ {saldo:.2f}")

    return saldo, historico


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    try:
        saque = float(valor)
        if saque <= 0:
            print("\nPor favor, insira um valor positivo.")
            return saldo, extrato, False

        if saque > saldo:
            print("\nNão foi possível realizar a operação. Motivo: Saldo insuficiente.")
            return saldo, extrato, False

        if saque > limite:
            print("\nValor excede o limite diário de saque.")
            return saldo, extrato, False

        extrato += f"Saque: -R$ {saque:.2f}\n"
        saldo -= saque
        numero_saques += 1
        print(f"""
            Por favor, retire o seu dinheiro

            Obrigado por utilizar o nosso banco.                            
        """)
        return saldo, extrato, True

    except ValueError:
        print("\nEntrada inválida. Por favor insira um valor numérico válido.")
        return saldo, extrato, False


def extrato(saldo, *, historico):
    if historico == "":
        return f"Não foram realizadas movimentações.", saldo
    else:
        return historico, saldo


def main():
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
                    valor_deposito = input(
                        "\nInsira a quantia que gostaria de depositar (ou '0' para voltar ao menu): ")
                    if valor_deposito == "0":
                        break
                    saldo, historico = deposito(saldo, valor_deposito, historico)
                except ValueError:
                    print("\nEntrada inválida. Por favor insira um valor numérico válido.")

        elif opcao == "2":
            print("\nSaque")
            if numero_saques >= LIMITE_SAQUES:
                print("Operação cancelada, número de saques diários atingido.\n")
                input("\nPressione Enter para voltar ao menu.")
                continue

            valor_saque = input("\nInsira a quantia que gostaria de sacar: ")
            saldo, historico, sucesso = saque(saldo=saldo, valor=valor_saque, extrato=historico, limite=limite,
                                              numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            if sucesso:
                numero_saques += 1

        elif opcao == "3":
            historico_str, saldo_atual = extrato(saldo, historico=historico)
            print("\nExtrato\n")
            print(historico_str)
            print(f"Saldo: R${saldo_atual:.2f}")

        elif opcao == "4":
            print("\nSair")
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()