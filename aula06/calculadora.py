def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    else:
        return a / b

while True:
    print("Escolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = int(input())

    if opcao == 0:
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = soma(num1, num2)
    elif opcao == 2:
        resultado = subtracao(num1, num2)
    elif opcao == 3:
        resultado = multiplicacao(num1, num2)
    elif opcao == 4:
        resultado = divisao(num1, num2)
    else:
        print("Opção inválida")

    print("Resultado: ", resultado)
