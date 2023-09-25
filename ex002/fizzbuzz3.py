num = int(input("Digite um número inteiro: "))

if(num % 5 == 0):
    if(num % 3 == 0):
        print("FizzBuzz")
else:
    print(num)
