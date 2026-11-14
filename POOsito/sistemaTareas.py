def F(n):
    # Casos base:
    if n == 0:
        return -1
    elif n == 1:
        return 1
    elif n == 2:
        return 3
        # Llamada recursiva:
    return F(n - 1) + F(n - 2) + F(n - 3)


def mostrar(i, cantidad):

    if i == cantidad:
        return i

    if i == 0:
        print(F(i), end="")
    else:
        print(",", F(i), end="")

    mostrar(i + 1, cantidad)


cantidad = int(input("¿Cuántos términos desea mostrar? "))
mostrar(0, cantidad)

