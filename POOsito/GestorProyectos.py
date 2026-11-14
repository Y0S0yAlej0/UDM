from dataclasses import dataclass
@dataclass
class Colaborador:
    nombreUsuario: str
    correo: str

class Proyecto:
    def __init__(self,nombre: str, lenguaje:str ) -> None:
        self.nombre = nombre
        self.lenguaje = lenguaje
        self.colaboradores: list[Colaborador] = []

    def agregarColaborador(self, colaborador: Colaborador) -> None:
        if colaborador not in self.colaboradores:
            self.colaboradores.append(colaborador)


    def listarColaborados(self) -> list[Colaborador]:
        return self.colaboradores

    def buscarColaborador(self, nombre: str) -> Colaborador:
        for i in self.colaboradores:
            if i.nombreUsuario.lower() == nombre.lower():
                return i
        else:
            return "Ese colaborador no existe"

    def __str__(self):
        return f"el proyecto {self.nombre} con el lenguaje {self.lenguaje}, tiene estos colaboradores,{self.colaboradores}"


class Gestor:
    def __init__(self) -> None:
        self.proyectos: list[Proyecto] = []

    def agregarProyecto(self, proyecto: Proyecto) -> None:
        if proyecto not in self.proyectos:
            self.proyectos.append(proyecto)

    def listarProyectos(self) -> list[Proyecto]:
        proyectos = []
        for i in self.proyectos:
            proyectos.append(i)
        return proyectos



    def buscarProyecto(self, nombre: str) -> Proyecto:
        for i in self.proyectos:
            if i.nombre.lower() == nombre.lower():
                return i
        else:
            return "Ese proyecto no existe"



# Colaboradores
ana   = Colaborador(nombreUsuario="ana_dev", correo="ana@mail.com")
luis  = Colaborador(nombreUsuario="luis99",  correo="luis@mail.com")
sofia = Colaborador(nombreUsuario="sofiaml", correo="sofia@mail.com")

# Proyectos
p1 = Proyecto(nombre="InventarioApp", lenguaje="Python")
p1.agregarColaborador(ana)
p1.agregarColaborador(luis)
p1.agregarColaborador(ana)   # aviso: ya existe

p2 = Proyecto(nombre="WebStore", lenguaje="JavaScript")
p2.agregarColaborador(sofia)

# __str__
print(p1)  # Proyecto: InventarioApp [Python] — 2 colaborador(es)
print(p2)  # Proyecto: WebStore [JavaScript] — 1 colaborador(es)

# tiene_colaborador
print(p1.buscarColaborador("ana_dev"))  # True
print(p1.buscarColaborador("sofiaml"))  # False

# Gestor
gestor = Gestor()
gestor.agregarProyecto(p1)
gestor.agregarProyecto(p2)
gestor.agregarProyecto(p1)  # aviso: ya existe

encontrado = gestor.buscarProyecto("WebStore")
print(encontrado)  # Proyecto: WebStore [JavaScript] — 1 colaborador(es)

no_existe = gestor.buscarProyecto("OtroProyecto")
print(no_existe)   # None

print(len(gestor.listarProyectos()))  # 2
print(gestor.listarProyectos())
