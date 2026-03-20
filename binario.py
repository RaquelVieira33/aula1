while True:
    print("1- Decimal para Binário")
    print("2- Binário para Decimal")
    print("3- Decimal para Octal")
    print("4- Octal para Decimal")
    print("5- Decimal para Hexadecimal")
    print("6- Hexadecinal para Decimal")
    print("7- Hexadecimal para Binário")
    print("8- Hexadecimal para Octal")
    print("9- Binário para Hexadecimal")
    print("10- Octal para Hexadecimal")
    print("0- Sair")

    op = input("Escolha uma opção: ")

    try:
        if op == "1":
            n = int(input("Digite um número decimal: "))
            if n == 0:
                print("Resultado: 0")
            else:
                binario = ""

                while n > 0:
                    resto = n % 2
                    binario = str(resto) + binario
                    n = n // 2

                print("Resultado:", binario)

        elif op == "2":
            b = input("Digite um número binário: ")
            print("Resultado:", int(b, 2))

        elif op == "3":
            n = int(input("Digite um número decimal: "))
            print("Resultado:", oct(n)[2:])

        elif op == "4":
            o = input("Digite um número octal: ")
            print("Resultado:", int(o, 8))

        elif op == "5":
            n = int(input("Digite um número decimal: "))
            print("Resultado:", hex(n)[2:].upper())

        elif op == "6":
            h = input("Digite um número hexadecimal: ")
            print("Resultado:", int(h, 16))

        elif op == "7":
            h = input("Digite um número hexadecimal: ")
            print("Resultado:", bin(int(h, 16))[2:])

        elif op == "8":
            h = input("Digite um número hexadecimal: ")
            print("Resultado:", oct(int(h, 16))[2:])

        elif op == "9":
            b = input("Digite um número binário: ")
            print("Resultado:", hex(int(b, 2))[2:].upper())

        elif op == "10":
            o = input("Digite um número octal: ")
            print("Resultado:", hex(int(o, 8))[2:].upper())

        elif op == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")

    except ValueError:
        print("Erro: valor inválido!")

    continuar = input("\nDeseja fazer outra conversão? (s/n): ").lower()

    if continuar != 's':
        print("Encerrando...")
        break    