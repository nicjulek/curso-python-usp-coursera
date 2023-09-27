n = int(input("Digite o valor de n: "))

if n <= 0:
    print("Digite o valor POSITIVO")
else:
    count = 0
    i = 1
    while count < n:
        if i %2 != 0:
            print(i)
            count += 1
        i += 1