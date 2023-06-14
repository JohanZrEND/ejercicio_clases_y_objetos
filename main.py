from alumno import Alumno
from aula import Aula
from profesor import Profesor

contador = 0
aulas = []
profesores = [
    Profesor("Darius", 0, 10),
    Profesor("Mordekaiser", 3, 6),
    Profesor("Miss Fortune", 2, 8),
    Profesor("Garen", 4, 7),
    Profesor("Seraphine", 1, 9)
]

CANTIDAD = {
    "aulas" : 5,
    "alumnos" : 20
}

for i in range(CANTIDAD["aulas"]):
    aulas.append(Aula())

for i in range(CANTIDAD["alumnos"]):
    aulas[i % len(aulas)].add(Alumno())

for i in range(len(profesores)):
    aulas[i % len(aulas)].set_profesor(profesores[i])

for profe in profesores:
    aulas[i % len(aulas)].set_profesor(profe)

for aula in range(len(aulas)):
    try:
        aulas[contador].puntuar()
        aulas[contador].convocar_examenes()
    except Exception as exception:
        print(exception)
