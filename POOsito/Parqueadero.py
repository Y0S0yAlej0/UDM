class Vehiculo:

    def __init__(self, modelo, placa) -> None:
        self.modelo = modelo
        self.placa = placa

class Tiquete:
    id = 0
    def __init__(self, vehiculo: Vehiculo) -> None:
        Tiquete.id += 1
        self.id = Tiquete.id
        self.vehiculo = vehiculo
        self.estado = "activo"
        self.valor = 0

class Parqueadero:
    def __init__(self, capacidad, tarifa):
        self.capacidad = capacidad
        self.tarifa = tarifa
        self.tiquetes = []

    def autosEstacinados(self):
        estacionados = []

        for i in self.tiquetes:
            if i.estado == "activo":
                estacionados.append(i)

        return estacionados

    def registarEntrada(self, placa, tipo):
        if len(self.autosEstacinados()) == self.capacidad:
            return "Parqueadero lleno"

        tiquete = Tiquete(Vehiculo(placa, tipo))
        self.tiquetes.append(tiquete)

        return f"Entrada registrada. ID del tiquete: {tiquete.id}"

    def registrarSalida(self, id, horas) -> None:
        for i in self.tiquetes:
            if i.id == id:
                if i.estado == "cerrado":
                    return "Ya se cerro este tiquete"

                i.valor = horas*self.tarifa
                i.estado= "cerrado"
                return f"El vehiculo ({i.vehiculo.placa}) con placa {i.vehiculo.modelo} debe pagar un total de: {i.valor}"

        return f"No se encontro este tiquete"

    def buscar(self, id):
        for i in self.tiquetes:
            if i.id == id:
                return f" {i.estado} | {i.vehiculo.modelo} | {i.vehiculo.placa} "
        return None

    def desocupados(self):
        desocupados = self.capacidad - len(self.autosEstacinados())
        return f"Desocupados: {desocupados}"


p = Parqueadero(2, 5000)

while True:
    print("""
        1) Registrar entrada
        2) Regitrar salida 
        3) Buscar por tiquete
        4) Desocupados
        5) Salir"""
    )
    opcion = int(input("Ingresa la opcion que desees: "))

    if opcion == 1:
        placa = input("Ingresa el placa del vehiculo")
        tipo = input("Ingresa el tipo del vehiculo")
        print(p.registarEntrada(placa, tipo))

    elif opcion == 2:
        id = int(input("Ingresa el id del vehiculo"))
        horas = int(input("Ingresa la horas del vehiculo"))
        print(p.registrarSalida(id, horas))

    elif opcion == 3:
        id = int(input("Ingresa el id del vehiculo"))
        print(p.buscar(id))

    elif opcion == 4:
        print(p.desocupados())

    elif opcion == 5:
        print("Gracias por usar nuestro servicios")




