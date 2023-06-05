import random
from alumno import Alumno

class Aula:
    def __init__(self):
        self.alumnos = list()

    def add(self, nuevo_alumno: Alumno):
        self.alumnos.append(nuevo_alumno)
    
    def listar(self):
        for alumno in self.alumnos:
            alumno.setNota(random.randint(0, 10))
            alumno.describe()
        print()

    def convocarExamen(self, turno):
        for alumno in self.alumnos:
            alumno.convocarExamen(turno)
        print()