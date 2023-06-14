from alumno import Alumno
from aula import Aula
from profesor import Profesor

aulas = [Aula(Profesor("profe", 0, 10)), Aula()]

CANTIDAD = {
    "alumnos": 7
}

for i in range(CANTIDAD["alumnos"]):
    aulas[0].add(Alumno())

try:
    aulas[0].puntuar()
    aulas[0].convocar_examenes()
except Exception as exception:
    print(exception)
