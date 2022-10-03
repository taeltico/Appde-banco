nome = input("Digite seu nome ")
saldo = 3000

Opções = int(input("Informe uma opção:[1]Saque\n [2] Extrato \n [3] Investimentos\n [4]Depositar:"))
if Opções == 1:
    valor = float(input("Informe o valor que deseja sacar "))

    if valor<=saldo:
        print("saque autorizado", (nome), "Seu saldo disponivel e ", (saldo-valor))
    else:
        print("Ola {name} Seu saldo e insuficiente", "saldo disponivel",(saldo))

if Opções == 2:
    print (saldo)

if Opções == 3:
    print("sem investimento disponiveis")

if Opções == 4:
    deposito = float(input("valor do deposito "))

    if deposito >= 0:
        print(" Seu deposito foi realizado, seu novo saldo e de "(saldo+deposito))
    else:
        print("valor insuficiente")