from alumno import Alumno

class Aula:
    def __init__(self):
        self.alumnos = list()
        self.profesor = None

    def add(self, nuevo_alumno: Alumno):
        self.alumnos.append(nuevo_alumno)
    
    def listar(self):
        print(f"PROFESOR: {self.profesor}")
        for alumno in self.alumnos:
            alumno.describe()
        print()

    def convocar_examenes(self):
        print(f"PROFESOR: {self.profesor}")
        for alumno in self.alumnos:
            alumno.convocar_examen()
        print()
        
    def puntuar(self):
        print(f"PROFESOR: {self.profesor}")
        for alumno in self.alumnos:
            alumno.setNota(self.profesor.generar_nota())
            alumno.describe()

    def set_profesor(self, profesor):
        self.profesor = profesor