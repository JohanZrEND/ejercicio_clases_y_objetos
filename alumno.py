from user import User

class Alumno(User):

    def __init__(self):
        print("randomuser...")
        super().__init__()
    

    def setNota(self, nota = 0):
        self.nota = nota

    def convocar_examen(self):
            if self.nota >= 5:
                print(f"{self.correo} - {self.nombre} - CONVOCADO ☻")

    def describe(self):
        print(f"{self.nombre} - {self.turno} - {self.correo} -> Nota : {self.nota}")
