from dataclasses import dataclass

from numpy.ma.core import append


@dataclass
class Estudiante:
    codigo:str
    nombre:str
    programaAcademico:str
    def __post_init__(self):
        if self.codigo.strip() == "":
            raise ValueError("no puedes tener un codigo vacio")

        if self.nombre.strip() == "":
            raise ValueError("no puedes tener un nombre vacio")

        if self.programaAcademico.strip() == "":
            raise ValueError("Tienes que pertenecer a algun programa")

class Evento:
    def __init__(self,codigo, nombre:str, tipo: str, fecha:str,lugar:str, cupoMax:int, precioBoleta:float):
        tiposValidos =  ("concierto", "deportivo", "academico")
        if tipo not in tiposValidos:
            raise ValueError("Tienes que pertenecer a un tipo valido")
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.fecha = fecha
        self.lugar = lugar
        self.cupoMax = cupoMax
        self.precioBoleta = precioBoleta
        self.inscritos = []


    def inscribirEstudiante(self, codigo, nombre, programaAcademico):
        if self.cupoMax == 0:
            return False

        e1 = Estudiante(codigo, nombre, programaAcademico)

        for i in self.inscritos:
            if i.codigo == e1.codigo:
                return False

        self.cupoMax -= 1
        self.inscritos.append(e1)

        return True

    def listarEstudiantes(self):
        return self.inscritos

    def calcularRecogido(self):
        return self.precioBoleta * len(self.inscritos)
class Plataforma:
    def __init__(self,nombre):
        self.nombre = nombre
        self.eventos: dict[str, Evento]= {}

    def agregarEvento(self, codigo, nombre, tipo, fecha, lugar, cupoMax, precioBoleta):
        if codigo in self.eventos:
            raise ValueError("Evento ya existe")

        ev1 = Evento(codigo, nombre, tipo, fecha, lugar, cupoMax, precioBoleta)
        self.eventos[codigo] = ev1

    def listarTipo(self, tipo):
        eventos = []

        for i in self.eventos.values():
            if i.tipo == tipo and i.cupoMax > 0:
                eventos.append(i)

        return eventos

    def estanInscrito(self, codigo):
        eventos = []

        for evento in self.eventos.values():
            for estudiante in evento.inscritos:
                if estudiante.codigo == codigo:
                    eventos.append(evento)

        return eventos



    def totalRecogido(self):
        total = 0
        for i in self.eventos.values():
            total += i.calcularRecogido()

        return total




# --- Datos de prueba ---

e1 = Estudiante(
    codigo="001",
    nombre="Ana Torres",
    programaAcademico="Ingeniería de Sistemas"
)

e2 = Estudiante(
    codigo="002",
    nombre="Carlos Rúa",
    programaAcademico="Medicina"
)

e3 = Estudiante(
    codigo="003",
    nombre="Pedro Salas",
    programaAcademico="Derecho"
)

e4 = Estudiante(
    codigo="004",
    nombre="Laura Díaz",
    programaAcademico="Arquitectura"
)


# --- Crear plataforma ---

plataforma = Plataforma("Plataforma UdeM")


# --- Agregar eventos ---

plataforma.agregarEvento(
    "E01",
    "Rock Fest UdeM",
    "concierto",
    "2026-10-15",
    "Auditorio",
    3,
    15000.0
)

plataforma.agregarEvento(
    "E02",
    "Torneo de Fútbol",
    "deportivo",
    "2026-10-20",
    "Cancha Central",
    50,
    0.0
)

plataforma.agregarEvento(
    "E03",
    "Congreso de IA",
    "academico",
    "2026-11-05",
    "Sala A",
    30,
    25000.0
)


# --- Inscripciones ---

# Ana → Rock Fest
i1 = plataforma.eventos["E01"].inscribirEstudiante(
    e1.codigo,
    e1.nombre,
    e1.programaAcademico
)

# Carlos → Rock Fest
i2 = plataforma.eventos["E01"].inscribirEstudiante(
    e2.codigo,
    e2.nombre,
    e2.programaAcademico
)

# Ana → Congreso de IA
i3 = plataforma.eventos["E03"].inscribirEstudiante(
    e1.codigo,
    e1.nombre,
    e1.programaAcademico
)


print(i1)
# True

print(i2)
# True

print(i3)
# True


# --- Consultar cupos ---

print(plataforma.eventos["E01"].cupoMax)
# 1
# Capacidad inicial: 3
# Ana y Carlos inscritos: 2
# Cupos restantes: 1


# --- Consultar eventos por tipo ---

conciertos = plataforma.listarTipo("concierto")

print(len(conciertos))
# 1

print(conciertos[0].nombre)
# Rock Fest UdeM


# --- Consultar inscritos en un evento ---

inscritos_rock = plataforma.eventos["E01"].listarEstudiantes()

print(len(inscritos_rock))
# 2

print(inscritos_rock[0].nombre)
# Ana Torres

print(inscritos_rock[1].nombre)
# Carlos Rúa


# --- Consultar eventos de un estudiante ---

eventos_ana = plataforma.estanInscrito("001")

print(len(eventos_ana))
# 2

print(eventos_ana[0].nombre)
# Rock Fest UdeM

print(eventos_ana[1].nombre)
# Congreso de IA


# --- Calcular ingresos totales ---

print(plataforma.totalRecogido())
# 55000.0

# Rock Fest:
# 2 × 15000 = 30000
#
# Congreso de IA:
# 1 × 25000 = 25000
#
# Total:
# 55000


# --- Probar inscripción duplicada ---

duplicado = plataforma.eventos["E01"].inscribirEstudiante(
    e1.codigo,
    e1.nombre,
    e1.programaAcademico
)

print(duplicado)
# False


# --- Probar último cupo ---

ultimo_cupo = plataforma.eventos["E01"].inscribirEstudiante(
    e3.codigo,
    e3.nombre,
    e3.programaAcademico
)

print(ultimo_cupo)
# True

print(plataforma.eventos["E01"].cupoMax)
# 0


# --- Probar inscripción sin cupo ---

sin_cupo = plataforma.eventos["E01"].inscribirEstudiante(
    e4.codigo,
    e4.nombre,
    e4.programaAcademico
)

print(sin_cupo)
# False


# --- Probar evento con tipo inválido ---

try:
    Evento(
        codigo="E99",
        nombre="Evento de prueba",
        tipo="invalido",
        fecha="2026-12-01",
        lugar="Sala",
        cupoMax=10,
        precioBoleta=0.0
    )
except ValueError as e:
    print("Error esperado:", e)


# --- Probar evento duplicado ---

try:
    plataforma.agregarEvento(
        "E01",
        "Otro Rock Fest",
        "concierto",
        "2026-12-10",
        "Auditorio",
        20,
        10000.0
    )
except ValueError as e:
    print("Error esperado:", e)


# --- Probar estudiante con código vacío ---

try:
    Estudiante(
        codigo="",
        nombre="Estudiante Prueba",
        programaAcademico="Ingeniería"
    )
except ValueError as e:
    print("Error esperado:", e)


# --- Probar estudiante con nombre vacío ---

try:
    Estudiante(
        codigo="005",
        nombre="",
        programaAcademico="Ingeniería"
    )
except ValueError as e:
    print("Error esperado:", e)


# --- Probar estudiante sin programa académico ---

try:
    Estudiante(
        codigo="006",
        nombre="Estudiante Prueba",
        programaAcademico=""
    )
except ValueError as e:
    print("Error esperado:", e)