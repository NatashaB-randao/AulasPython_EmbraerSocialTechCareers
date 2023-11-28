# FUNÇÕES

# def soma(a, b):
#     return a + b

# resultadoSoma = soma(4, 6)
# print("A soma é: ", resultadoSoma)


# Escreva um script em Python que pergunte ao usuário a quantidade de km percorrido por um carro que ele alugou, 
# para a empresa mostrar o quanto ele tem que pagar. 
# O preço do carro alugado por dia é R$60,00 e o preço por km é R$0,15
# preço a pagar: km * precoDoKm + diasCarroAlugado * precoDia

def calcular_preco_aluguel(km, dias):
    precoKm = 0.15  # Preço por km
    precoDia = 60.00  # Preço por dia

    # Cálculo do preço a pagar
    precoTotal = (km * precoKm) + (dias * precoDia)

    return precoTotal

# Solicita a entrada do usuário
kmPercorrido = float(input("Digite a quantidade de km percorridos: "))
diasAluguel = int(input("Digite a quantidade de dias de aluguel: "))

# Calcula o preço a pagar
precoPagar = calcular_preco_aluguel(kmPercorrido, diasAluguel)

# Exibe o resultado
print(f"O preço a pagar pelo aluguel é: R${precoPagar:.2f}")



# Faça um script que exiba as tabuadas de 1 até 10 no formato: "2 x 3 = 6"

# Loop externo para percorrer os números de 1 a 10
# for operador in range(1, 11):
#     # Divisória entre as tabuadas
#     print("-" * 20)
    
#     # Loop interno para calcular e exibir a tabuada para cada número de 1 a 10
#     for multiplicador in range(1, 11):
#         resultado = operador * multiplicador
#         print(f"{operador} x {multiplicador} = {resultado}")



# Fazer um script que inicialize uma lista vazia, solicite ao usuário 10 números ímpares diferentes, um por vez. 
# Caso número digitado seja par, solicite novamente um número, até que o número seja ímpar.
# Depois disso, exiba os 10 números digitados.

# Inicializa uma lista vazia para armazenar os números ímpares
numeros_impares = []

# Loop para solicitar 10 números ímpares ao usuário
for tentativa in range(1, 11):
    while True:
        # Solicitando um número ao usuário
        numero = int(input(f"Tentativa {tentativa}: Digite um número ímpar: "))

        # Verificando se o número é ímpar
        if numero % 2 != 0:
            numeros_impares.append(numero)
            break
        else:
            print("O número digitado não é ímpar. Tente novamente.")

# Exibindo os 10 números ímpares digitados
print("-" * 30)
print("Os 10 números ímpares digitados são:")
for numero_impar in numeros_impares:
    print(numero_impar)

