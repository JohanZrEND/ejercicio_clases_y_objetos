from alumno import Alumno
from profesor import Profesor

class Aula:
    def __init__(self, profesor = None):
        self.alumnos = list()
        self.profesor = profesor if profesor is not None else profesor

    def add(self, nuevo_alumno: Alumno):
        self.alumnos.append(nuevo_alumno)

    def add_profe(self, nuevo_profe: Profesor):
        self.profesor.append(nuevo_profe)

    def listar(self):
        print(f"PROFESOR: {self.profesor}")
        for alumno in self.alumnos:
            alumno.describe()
        print()

    def convocar_examenes(self):
        if len(self.alumnos) == 0:
            raise Exception("Sin alumnos no hay convocados ----> 0 Convocados")
        
        if not self.profesor:
            raise Exception("No hay profesor")

        print(f"PROFESOR: {self.profesor}")
        if len(self.alumnos) > 0:
            for alumno in self.alumnos:
                alumno.convocar_examen()

    def puntuar(self):
        if not self.profesor:
            raise Exception("Sin profesor no se pueden puntuar examenes")

        print(f"PROFESOR: {self.profesor}")
        for alumno in self.alumnos:
            alumno.setNota(self.profesor.generar_nota())
            alumno.describe()

    def set_profesor(self, profesor):
        self.profesor = profesor