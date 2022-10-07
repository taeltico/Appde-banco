nome = input("Digite seu nome ")
saldo = 3000
cheque = 500
limiteCartao = 3500

Opções = int(input("Informe uma opção: [1] Saque\n [2] Extrato \n [3] Investimentos\n [4] Depositar\n [5] Exit\n [6] proxima pagina"))

if Opções == 1:
    valor = float(input("Informe o valor que deseja sacar "))

    if valor<=saldo:
        print("saque autorizado",(nome), "Seu saldo disponivel e ", (saldo-valor))
    else:
        print("Ola",(nome),"Seu saldo e insuficiente", "saldo disponivel",(saldo))

if Opções == 2:
    print (saldo)

if Opções == 3:
    print("sem investimento disponiveis")

if Opções == 4:
    deposito = float(input("valor do deposito "))

    if deposito >= 0:
        print(" Seu deposito foi realizado, seu novo saldo e de ",(saldo+deposito))
    else:
        print("valor insuficiente")

if Opções == 6:
    int(input("Informe uma opção: [1] Cheque especial\n [2] cartoes de credito \n [3] Bitcoins\n [4] Transferencia\n [5] Exit\n [6] retornar pagina"))

    if Opções == 1:
        saqueCheque = float(input("Informe o valor que deseja sacar "))

    if saqueCheque<=cheque:
        print("saque autorizado",(nome), "Seu saldo disponivel e ", (cheque-saqueCheque))
    else:
        print("Ola",(nome),"Seu saldo e insuficiente", "saldo disponivel",(cheque))

if Opções == 2:
    print (limiteCartao)

if Opções == 3:
    print("sem investimento disponiveis")

if Opções == 4:
    transferencia = float(input("valor do deposito "))

    if transferencia >= saldo:
        print(" Seu deposito foi realizado, seu novo saldo e de ",(saldo - transferencia))
    else:
        print("valor insuficiente")


