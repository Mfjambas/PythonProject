A = int(input("informe um valor da variavel A: "))
B = int(input("infome um valor para variavel B:"))

if A > B:
    aux=A
    A=B
    B=aux

print("O valor da variavel A é:", A)
print("O valor da variavel B é:", B)