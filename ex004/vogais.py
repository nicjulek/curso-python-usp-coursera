def vogal(caractere):
    caractere = caractere.lower()

    if caractere in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


print(vogal("a"))  
print(vogal("b"))  
print(vogal("E"))