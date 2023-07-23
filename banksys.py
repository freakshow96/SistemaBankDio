menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
       
    if opcao == "d":
        valor = float(input("Informa o valor do deposito: "))
        
        if valor > 0 : ## Realiza a validação referente ao valor do depósito, tendo esse que ser maior que 0.
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else: 
            print("Por favor insira um valor maior que 0")

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))
   
        execedeu_saldo = valor > saldo ## Realiza a validação entre o valor a ser sacado e o saldo atual da conta

        execedeu_limite = valor > limite 

        execeu_saques = numero_saques >= LIMITE_SAQUES ## Realiza validação referente a quantidade de saques realizados

        if execedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        
        elif execedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif execeu_saques:
            print("Operação falhou! Número máximo de saques execedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")             

    elif opcao == "e":
        print("\n================= Extrato =================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo}")
        print("==================================") 
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")