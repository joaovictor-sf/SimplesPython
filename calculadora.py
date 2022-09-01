print("Calculadora simples, digite um número, depois +,-,/,*, depois outro número. Escreva 'done' quando quiser finalizar")
numPrincipal = input("Digite um número inicial\n")
while True:
    try:
        numPrincipal = float(numPrincipal)
    except:
        print("Digito inválido")
        numPrincipal = input()
        continue
    while True:
        opcao = input("Escolhar a operação que deseja(+, -, *, /) ou escolha outro número\n")
        if opcao.isdigit():
            numPrincipal = float(opcao)
            print(numPrincipal)
            continue
        match opcao:
            case 'done':
                quit()
            case '+':
                numSecundario = input()
                if numSecundario == 'done':
                    quit()
                try:
                    numSecundario = float(numSecundario)
                except:
                    print("Digito Inválido")
                    continue
                numPrincipal += numSecundario
                print(numPrincipal)
            case '-':
                numSecundario = input()
                if numSecundario == 'done':
                    quit()
                try:
                    numSecundario = float(numSecundario)
                except:
                    print("Digito Inválido")
                    continue
                numPrincipal -= numSecundario
                print(numPrincipal)
            case '*':
                numSecundario = input()
                if numSecundario == 'done':
                    quit()
                try:
                    numSecundario = float(numSecundario)
                except:
                    print("Digito Inválido")
                    continue
                numPrincipal *= numSecundario
                print(numPrincipal)
            case '/':
                numSecundario = input()
                if numSecundario == 'done':
                    quit()
                try:
                    numSecundario = float(numSecundario)
                except:
                    print("Digito Inválido")
                    continue
                numPrincipal /= numSecundario
                print(numPrincipal)
            case _:
                print("Digito Inválido")