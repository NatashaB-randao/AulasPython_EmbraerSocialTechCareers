
# idade = int(input("Digite a sua idade: "))

# if idade >= 18:
#     print("No Brasil, voce e maior de idade")

# else:
#     print("Voce e menor de idade")


nota = 75

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota <= 20:
    print("Reprovado")
else:
    print("Nota abaixo de C")


# Loops

frutas = ["uva", "banana", "laranja", "pera"]
# for fruta in frutas:
#     print(frutas)

# for i in frutas:
#     print(frutas)

# for i in range(5):
#     print(i)

for fruta in frutas:
    if fruta == "laranja":
        break
    print(frutas)



# WHILE

contador = 0

while contador < 5:
    print(contador)
    contador += 1 