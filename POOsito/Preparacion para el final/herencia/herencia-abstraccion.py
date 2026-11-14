from excepciones import *
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, placa:str, marca:str, modelo:str, año:int):
        if placa.strip() == "":
            raise ValueError("La placa no puede estar vacia")

        if marca.strip() == "":
            raise ValueError("La marca no puede estar vacia")

        if modelo.strip() == "":
            raise ValueError("El modelo no puede estar vacio")

        if not año >= 2000 and año <= 2026:
            raise ValueError("El año debe de estar entre 2000 y 2026")

        self.placa = placa.upper()
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.disponible:bool = True

    @abstractmethod
    def costo_por_dia(self) -> int :
        ...
    @abstractmethod
    def tipo(self) -> str :
        ...

    def calcular_costo_total(self, dias:int):
        return self.costo_por_dia()* dias

    def resumen(self):
        return f"[{self.tipo()}] {self.placa} - {self.modelo} {self.año} | {self.costo_por_dia()}/Dia | {self.disponible}"

class Auto(Vehiculo):
    def __init__(self, placa:str, marca:str, modelo:str, año:int, num_puertas):
        super().__init__(placa, marca, modelo, año)
        if num_puertas not in (2, 4):
            raise ValueError("Numero de purtas no valido")
        self.num_puertas = num_puertas


    def costo_por_dia(self) -> int:
        precio_base = 85000
        if self.num_puertas == 4:
            return precio_base + 5000
        return precio_base

    def tipo(self) -> str:
        return "Auto"

class Camioneta(Vehiculo):
    def __init__(self, placa:str, marca:str, modelo:str, año:int, capacidad_carga_kg):
        super().__init__(placa, marca, modelo, año)
        if capacidad_carga_kg <= 0:
            raise ValueError("La carga no puede ser 0 o negativa")
        self.capacidad_carga_kg = capacidad_carga_kg


    def costo_por_dia(self) -> int:
        precio_base = 120000
        carga = self.capacidad_carga_kg //  100
        return precio_base + (carga*500)

    def tipo(self):
        return "Camioneta"

class Moto(Vehiculo):
    def __init__(self, placa:str, marca:str, modelo:str, año:int, cilindrada):
        super().__init__(placa, marca, modelo, año)
        if cilindrada <= 0:
            raise ValueError("El cilindraje no puede ser negativo o 0")

        self.cilindrada = cilindrada

    def costo_por_dia(self) -> int:
        if self.cilindrada <= 200:
            return 35000
        elif self.cilindrada > 200 and self.cilindrada <= 600:
            return 50000
        elif self.cilindrada >600:
            return 70000

    def tipo(self) -> str:
        return "Moto"


class CatalogoRental:
    def __init__(self):
        self._catalogo: dict[str, Vehiculo] = {}
        self._historial: list[str] = []

    def agregar(self, vehiculo: Vehiculo) -> None:
        if vehiculo.placa in self._catalogo:
            raise PlacaDuplicada("Este vehiculo ya fue agregado")
        self._catalogo[vehiculo.placa] = vehiculo

    def buscar(self, placa:str) -> Vehiculo:
        vehiculo = self._catalogo[placa]
        if vehiculo == None:
            raise VehiculoNoEncontrado("No se encontro el vehiculo")
        return vehiculo

    def alquilar(self, placa:str, dias:int)-> int:
        if dias <= 0:
            raise DiasInvalidos("Los dias no pueden ser 0 o negativos")
        if placa not in self._catalogo:
            raise VehiculoNoEncontrado("No se encontro vehiculo con esa placa")
        if self._catalogo[placa].disponible == False:
            raise VehiculoNoDisponible("El vehiculo no esta disponible para ser alquilado")
        self._catalogo[placa].disponible = False
        self._historial.append(f"ALQUILER | {self._catalogo[placa]} | {dias} dias | {self._catalogo[placa].calcular_costo_total(dias)}")
        return self._catalogo[placa].calcular_costo_total(dias)

    def devolver(self, placa:str):
        if placa not in self._catalogo:
            raise VehiculoNoEncontrado("No se encontro vehiculo con esa placa")
        if self._catalogo[placa].disponible == True:
            raise VehiculoNoDisponible("El vehiculo no estaba alquilado")
        self._historial.append(
            f"DEVOLUCION | {self._catalogo[placa]} ")
        self._catalogo[placa].disponible = True

    def listar_disponibles(self) -> list[Vehiculo]:
        vehiculos = [i for i in self._catalogo.values() if i.disponible == True]
        return vehiculos
    def resumen_catalogo(self)-> str:
        vehiculos = [i for i in self._catalogo.values()]
        for v in vehiculos:
            print(v.resumen())

    def ver_historial(self) -> list[str]:
        copia = [i for i in self._historial]
        return copia
if __name__ == "__main__":
    catalogo = CatalogoRental()

    # 1. Agregar vehículos
    catalogo.agregar(Auto("ABC-123", "Toyota", "Corolla", 2022, num_puertas=4))
    catalogo.agregar(Camioneta("DEF-456", "Ford", "Ranger", 2021, capacidad_carga_kg=800))
    catalogo.agregar(Moto("GHI-789", "Honda", "CB500", 2020, cilindrada=500))

    # 2. Ver catálogo completo
    print("=== Catálogo ===")
    print(catalogo.resumen_catalogo())

    # 3. Alquilar un auto
    costo = catalogo.alquilar("ABC-123", 3)
    print(f"Alquiler Toyota Corolla por 3 días → ${costo:,}")

    # 4. Ver solo disponibles (quedan 2)
    print("\n=== Disponibles ===")
    for v in catalogo.listar_disponibles():
        print(f"  {v.resumen()}")


    # 5. Intentar alquilar el mismo (ya reservado)
    try:
        catalogo.alquilar("ABC-123", 1)
    except RentalError as e:
        print(f"\nError esperado → {e}")

    # 6. Devolver el auto
    catalogo.devolver("ABC-123")
    print(f"Devolución. Disponible ahora: {catalogo.buscar('ABC-123').disponible}")
    print("\n===HISTORIAL===")
    print(catalogo.ver_historial())
    # 7. Días inválidos
    try:
        catalogo.alquilar("DEF-456", 0)
    except RentalError as e:
        print(f"Error esperado → {e}")

    # 8. Placa inexistente
    try:
        catalogo.buscar("ZZZ-000")
    except RentalError as e:
        print(f"Error esperado → {e}")

