class Playlist:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.pista: list[tuple[str, int]] = []

    def agregarPista(self, titulo:str, duracion:float):
        self.pista.append((titulo, duracion))

    def  contarpista(self) -> int:
        return len(self.pista)

    def calcularDuracion(self) -> int:
        duracion = 0
        for pista in self.pista:
            duracion += pista[1]
        return duracion

    def pistaMasLarga(self) -> int|None:

        if len(self.pista) <= 0:
            return None
        else:
            pista: int = 0
            for i in self.pista:
                if i[1] > pista:
                    pista = i[1]
                else:
                    pista = pista + 1
            return f"la cancion mas larga de la playlist {self.nombre} es {pista}"

andro = Playlist("andro")

andro.agregarPista[("Brilloteo", 197), ()]

andro.contarpista()

andro.calcularDuracion()

print(andro.pistaMasLarga())

