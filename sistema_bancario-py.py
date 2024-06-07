# header
nome = "Banco Py"
print(nome.center(50, "-"))

msg = "Informações da sua conta"

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

# => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  if opcao == "1":
    valor = float(input("Informe o valor do depósito: R$ "))

    if valor <= 0:
      print("Valor inválido, por favor informe um valor maior que zero.")
      continue
    
    saldo += valor
    extrato += f"Depósito: R${valor:.2f}\n"
    print("Depósito realizado com sucesso.")
    
    print(msg.center(50, "-"))

  elif opcao == "2":
    if numero_saques >= LIMITE_SAQUES:
      print("Limite de saques atingido.")
      continue

    valor = float(input("Informe o valor do saque: "))

    if valor <= 0:
      print("Valor inválido, por favor informe um valor maior que zero.")
      continue

    if saldo < valor:
      print("Saldo insuficiente.")
      continue

    if valor > limite:
      print("Valor acima do limite permitido.")
      continue

    saldo -= valor
    extrato += f"Saque: R${valor:.2f}\n"
    numero_saques += 1
    print("Saque realizado com sucesso.")
    print(msg.center(50, "-"))

  elif opcao == "3":
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print(extrato)
    print(msg.center(50, "-"))


  elif opcao == "4":
    print("Finalizando operação...")
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
