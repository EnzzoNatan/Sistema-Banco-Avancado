def menu():
    menu = """"
    ====================MENU====================
    [d] Depositar
    [s] Sacar 
    [e] Extrato 
    [lc] Listar Contas
    [nc] Nova Conta
    [nu] Novo Usuário
    [q] Sair
    """
    return input(menu)

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato +=(f"Depósito: R$ {valor:.2f}\n")
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou, valor informado inválido.")
    return saldo, extrato

def sacar(*, saldo,valor,extrato,limite,numero_saques,LIMITE_SAQUES):
    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou. Você não tem saldo suficiente!")
    elif excedeu_limite:
        print("Operação falhou. O valor excede o limite!")
    elif excedeu_saques:
        print("Operação falhou. Você execeu o limite de saques!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque {valor:.2f}"
        numero_saques =+ 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou. Informe um valor válido")
    
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("====================EXTRATO====================")
    print("Não foram realizados movimentações" if not extrato else extrato)
    print(f"Saldo R$ {saldo:.2f}")
    print("===============================================")

def criar_usuarios(usuarios):
    cpf = input("Informe o cpf (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios) 

    if usuario:
        print("Já existe um usuario com este CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nasci = input("Informe sua data de nascimente (dd/mm/aaaa): ") 
    endereco = input("Informe seu endereço (Logradouro, nmr, bairro, cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nasci": data_nasci, "cpf": cpf, "endereço": endereco})

    print("Usuario criado com sucesso!")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrado = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrado[0] if usuarios_filtrado else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta cirada com sucesso!")
        return{"agencia": agencia, "numero_conta": numero_conta,
        "usuario": usuario}
    print("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
    print("=" * 100)
    print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuarios(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()