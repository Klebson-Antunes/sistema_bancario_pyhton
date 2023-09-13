menu = '''
    Selecione qual operação deseja realizar:
    
    (1) Depósito
    (2) Saque
    (3) Extrato
    (4) Saldo
    (5) Sair

'''
saldo = 0
limite = 500
limite_de_saque = 3
quantidade_de_saque_realizado = 0
extrato = ""

acesso_a_conta = True


while acesso_a_conta:
    print(menu)
    operacao = int(input("Qual operação deseja realizar: "))
    if operacao == 1:
        
        print("\n**** Deposito ****\n")
        operacao_atual = "Depósito"
        valor_do_desposito = float(input("Digite o valor do depósito: "))
        saldo += valor_do_desposito

        extrato_deposito = f"Depósito: R${valor_do_desposito:.2f} Reais"
        extrato += f"{extrato_deposito}\n"
        
    elif operacao == 2:
        
        print("**** Saque ****\n")
        if quantidade_de_saque_realizado != 3:
            
            valor_do_saque = float(input("Digite o valor do saque: "))
            if not valor_do_saque > 500:
                
                if saldo == 0:
                    print("Saque negado! Você está sem saldo.")
                elif valor_do_saque <= saldo:
                    saldo -= valor_do_saque
                    quantidade_de_saque_realizado += 1
                    
                    extrato_saque = f"Saque:    R${valor_do_saque:.2f} Reais"
                    extrato += f"{extrato_saque}\n"
                else:
                    print("Saque negado! saldo Insuficiente.")
                    
            else:
                print(f"\nVocê so pode sacar R${limite} Reais!")
                print("tente novamente!")
                
        else:
            print("Você atingiu o limite diario de saque!")
        
            
    elif operacao == 3:
        
        if extrato != "":
            print("**** Extrato ****\n")
            print(extrato)
            print("\n*****************")
        else:
            print("**** Extrato ****\n")
            print("Nenhuma operação realizada!")
            print("\n*****************")
        
    elif operacao == 4:
        
        print("**** Saldo ****\n") 
        print(f"Saldo: R${saldo:.2f} reais")
        
    elif operacao == 5:
        
        print("Operação finalizada! Volte sempre.")
        acesso_a_conta = False
        
    else:
        
        print("\nOpção invalida! Tente novamente.\n")
    
    saldo
        




