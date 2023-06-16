from random import randint
from alumno import Alumno
from aula import Aula
from profesor import Profesor

aulas = []
profesores = []

CANTIDAD = {
    "aulas" : randint(2, 10),
    "alumnos" : randint(10, 40),
    "profes" : randint (3, 5)
}

CANTIDAD = {
    "aulas" : 1,
    "alumnos" : 10,
    "profes" : 1
}


for i in range(CANTIDAD["profes"]):
    profesores.append(Profesor(randint(0,4), randint(6,10)))
   
for i in range(CANTIDAD["aulas"]):
    aulas.append(Aula())

for i in range(CANTIDAD["alumnos"]):
    aulas[i % len(aulas)].add(Alumno())

i = 0
for aula in aulas:
    aula.set_profesor(profesores[i])
    i += 1
    if i == len(profesores):
        i = 0

for aula in aulas:
    aula.listar()
    aula.convocar_examenes()

# for aula in aulas:
#     try:
#         print("\nPUNTUAR ------------------------------")
#         aula.puntuar()
#         print("\nCONVOCAR AULA ------------------------")
#         aula.convocar_examenes()
#     except Exception as exception:
#         print(exception)
