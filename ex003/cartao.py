meuCartao = int(input("Digite o número do seu cartão de crédito: "))

cartaoLido = 1
encontreimeucartao = False

while cartaoLido != 0 and not encontreimeucartao:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        encontreimeucartao = True

if encontreimeucartao:
    print("Eba! Meu cartão está na lista!!")
else:
    print("Xi,meu catão não está lá...")