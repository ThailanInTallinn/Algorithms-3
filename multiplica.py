def multiplicacao(x, y):
    print("Chama x = {x} e y = {y}")
    #Caso base
    if(x == 1):
        print(f"Retorna {y}")
        return y

    print(f"Retorna x = {x - 1} e y = {y}")
    return y + multiplicacao(x - 1, y)




result = multiplicacao(3, 3)
print(f"Multiplicacao de 3 x 3: {result}")
result = multiplicacao(2, 4)
print(f"Multiplicacao de 2 x 4: {result}")
