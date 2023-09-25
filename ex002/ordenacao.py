num1 = int(input('Digite a primeiro numero: '))
num2 = int(input('Digite a segundo numero: '))
num3 = int(input('Digite a terceiro numero: '))

if (num1<num2):
    if(num2<num3):
        print("crescente")
    else:
        print("não está em ordem crescente")
else:
    print("não está em ordem crescente")