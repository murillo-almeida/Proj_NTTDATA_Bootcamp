menu = """
Digite um nmero abaixo para selecionar a operacao:

[1] depositar
[2] sacar
[3] extrato
[4] sair
=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  if opcao == "1":
      valor = float(input("DEPOSITO SELECIONADO\n\nInforme o valor do deposito: \n"))

      if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"

      else:
        print("Operacao falhou! O valor de deposito informado e invalido.")

  elif opcao == "2":
      valor = float(input("SAQUE SELECIONADO\n\nInforme o valor do saque: "))

      excedeu_saldo = valor > saldo

      excedeu_limite = valor > limite

      excedeu_saques = numero_saques >= LIMITE_SAQUES

      if excedeu_saldo:
        print("Operacao falhou! Voce nao tem saldo suficiente.")

      elif excedeu_limite:
        print("Operacao falhou! O valor do saque excede o limite.")

      elif excedeu_saques:
        print("Operacao falhou! Numero maximo de saques excedido.")

      elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

      else:
        print("Operacao falhou! O valor de saque e invalido.")

  elif opcao == "3":
      print("EXTRATO SELECIONADO\n\n**************** EXTRATO ****************")
      print("Nao foram realizadas movimentacoes." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("************************************************")

  elif opcao == "4":
    print("SAIR SELECIONADO\n\nSaindo do sistema...")
    break

  else:
      print("Operacao invalida, por favor selecione uma operacao presente no menu.")

