# -*- coding: utf-8 -*-

def adicionar(x, y):
    """Esta função soma dois números"""
    return x + y

def subtrair(x, y):
    """Esta função subtrai dois números"""
    return x - y

def multiplicar(x, y):
    """Esta função multiplica dois números"""
    return x * y

def dividir(x, y):
    """Esta função divide dois números"""
    if y == 0:
        return "Erro! Divisão por zero não é permitida."
    return x / y

# Função principal da calculadora
def calculadora():
    print("--- Calculadora Simples em Python ---")
    
    while True:
        # Menu de opções para o usuário
        print("\nSelecione a operação desejada:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        # Verifica se o usuário quer sair
        if escolha == '5':
            print("Obrigado por usar a calculadora. Até mais!")
            break
            
        # Verifica se a escolha é uma operação válida
        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números.")
                continue # Volta para o início do loop

            if escolha == '1':
                print(f"\nResultado: {num1} + {num2} = {adicionar(num1, num2)}")

            elif escolha == '2':
                print(f"\nResultado: {num1} - {num2} = {subtrair(num1, num2)}")

            elif escolha == '3':
                print(f"\nResultado: {num1} * {num2} = {multiplicar(num1, num2)}")

            elif escolha == '4':
                resultado = dividir(num1, num2)
                print(f"\nResultado: {num1} / {num2} = {resultado}")
        
        else:
            print("Opção inválida. Por favor, escolha uma operação de 1 a 5.")

# Executa a função principal da calculadora quando o script é rodado
if __name__ == "__main__":
    calculadora()