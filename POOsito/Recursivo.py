
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)

    if valor < raiz.valor:
        raiz.izq = insertar(raiz.izq, valor)
    elif valor > raiz.valor:
        raiz.der = insertar(raiz.der, valor)

    return raiz


def in_order(raiz, lista):
    if raiz is not None:
        in_order(raiz.izq, lista)
        lista.append(raiz.valor)
        in_order(raiz.der, lista)


# Lista original
numeros = [8, 3, 10, 1, 6, 14, 4, 7, 13]

# Crear el árbol
raiz = None
for numero in numeros:
    raiz = insertar(raiz, numero)

# Ordenar mediante In Order
ordenada = []
in_order(raiz, ordenada)

print(ordenada)
