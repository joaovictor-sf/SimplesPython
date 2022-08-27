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
        if opcao == 'done':
            quit()
        elif opcao.isdigit():
            numPrincipal = float(opcao)
            print(numPrincipal)
        elif opcao == '+':
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
        elif opcao == '-':
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
        elif opcao == '*':
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
        elif opcao == '/':
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
