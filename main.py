def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        print(f"Saldo atual: R${saldo:.2f}")
        extrato_temp = f"Depósito: R${deposito:.2f}"
        extrato.append(extrato_temp)
    else:
        print("Valor do depósito inválido.")

    return saldo, extrato


def sacar(*, valor_saque, qtd_saques, limite_saque, saldo, extrato):
    if valor_saque > 0:
        if valor_saque <= limite_saque:
            if saldo >= valor_saque:
                saldo -= valor_saque
                qtd_saques += 1
                print(f"Saque realizado com sucesso! Saldo atual: R${saldo:.2f}")
                extrato_temp = f"Saque: R${valor_saque:.2f}"
                extrato.append(extrato_temp)
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor do saque excede o limite de R$500,00.")
    else:
        print("Valor do saque inválido.")

    return saldo, extrato, qtd_saques


def extrato_func(saldo, /, extrato):
    if extrato:
        for i in extrato:
            print(i)
        print("================================================================")
        print(f"Saldo atual da conta: R${saldo:.2f}")
        print("================================================================")
    else:
        print("Não foram realizadas movimentações.")


def cadastrar_usuario(cliente):
    cpf = input("Digite o CPF: ")
    confirma_cpf = cpf in cliente
    if not confirma_cpf:
        nome = input("Digite o nome: ")
        data_nascimento = input("Digite a data de nascimento: ")
        logradouro = input("Digite o logradouro: ")
        numero = input("Digite o número: ")
        bairro = input("Digite o bairro: ")
        cidade = input("Digite a cidade: ")
        sigla_estado = input("Digite a sigla do estado: ")

        endereco = f"{logradouro}, {numero} - {bairro} - {cidade} / {sigla_estado}"

        cliente.update(
            {
                cpf: {
                    "nome": nome,
                    "data_nascimento": data_nascimento,
                    "endereco": endereco,
                    "contas": [],
                }
            }
        )
        print(f"Cliente {nome} cadastrado com sucesso!")
    else:
        print("Cliente já cadastrado.")
    return cliente


def cadastrar_conta(cliente, numero_conta):
    cpf_conta = input("Digite o CPF: ")

    if cpf_conta in cliente.keys():
        # Criando uma nova conta para o cliente
        numero_conta += 1
        nova_conta = [AGENCIA, numero_conta]

        # Adicionando a conta à lista de contas do cliente
        cliente[cpf_conta]["contas"].append(nova_conta)
        print(cliente)
    else:
        print("CPF não cadastrado.")
    return cliente, numero_conta


menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Usuário
[5] Cadastrar Conta
[0] Sair
=> """

saldo = 0
limite = 500
extrato = []
extrato_temp = ""
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0
valor_saque = 0
cliente = {}
AGENCIA = "0001"
numero_conta = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        deposito = float(input("Digite o valor a ser depositado: "))
        saldo, extrato = depositar(deposito, saldo, extrato)

    elif opcao == "2":
        print("Saque")
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            saldo, extrato, numero_saques = sacar(
                valor_saque=valor_saque,
                qtd_saques=numero_saques,
                limite_saque=limite,
                saldo=saldo,
                extrato=extrato,
            )

        else:
            print("Você atingiu o limite de saques diários.")

    elif opcao == "3":
        print("Extrato")
        extrato_func(saldo, extrato=extrato)

    elif opcao == "4":
        cliente = cadastrar_usuario(cliente)

    elif opcao == "5":
        cliente, numero_conta = cadastrar_conta(cliente, numero_conta)

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
