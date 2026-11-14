

class Estudiante:
    def __init__(self, nombreCompleto, codigo) -> None:
        self.nombreCompleto = nombreCompleto
        self.codigo = codigo
        self.cantidadMaterias = 0
        self.materias = []
        self.calificaciones: list[tuple] = []
        self.promedio = 0.0

    def cantidadM(self) -> None|str:
        cantidaM = int(input("Cuantas materias tienes"))

        if cantidaM < 1:
            cantidaM = 0
            return f"la cantidad de materias debe de ser igual o mayor a 1 ({cantidaM}) "
        else:
            self.cantidadMaterias = cantidaM
            return f"la cantidad de materias se ha guardado correctamente ({self.cantidadMaterias}) )"

    def agregarM(self) -> None:

        for i in range(self.cantidadMaterias):
            materia = input(f"cual es tu materia numero {i+1}")
            self.materias.append(materia)


    def agregarCalificacion(self) -> str:
        for i in range(self.cantidadMaterias):
            notas = []
            print(f"digita las notas de la materia {self.materias[i]}")
            for j in range(5):
                while True:
                    calificacion = float(input(f"Calificacion {j+1} de {self.materias[i]} (0.0 hasta 5.0): "))
                    if calificacion < 0 or calificacion > 5:
                        print("la calificacion no puede ser menor a 0 o mayor a 5, intenta de nuevo")
                    else:
                        break
                notas.append(calificacion)
            self.calificaciones.append(tuple(notas))



    def mostrarCalificacion(self) -> None:
        print(f"El estudiante {self.nombreCompleto} ha sacado estas calificaciones")
        for i in range(self.cantidadMaterias):
            print(self.materias[i])
            for j in range(5):
                print(self.calificaciones[i][j])

    def promedioGeneral(self):
        promedioGeneral = 0.0
        for i in range(self.cantidadMaterias):
            print(self.materias[i])
            promedioPorMateria = 0
            for j in range(5):
                promedioPorMateria += self.calificaciones[i][j]
            promedioPorMateria = promedioPorMateria / 5
            promedioGeneral += promedioPorMateria

        self.promedio = promedioGeneral / self.cantidadMaterias
        return self.promedio

    def resumen(self):
        return f"El estudiante {self.nombreCompleto}, ha obtenido un promedio de {self.promedioGeneral()} con un codigo de {self.codigo}"


juanito = Estudiante("Juanito", 1)
print(juanito.cantidadM())

print(juanito.agregarM())

juanito.agregarCalificacion()
print(juanito.mostrarCalificacion())
print(juanito.resumen())
