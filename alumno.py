from user import User

class Alumno(User):

    def __init__(self):
        print("randomuser...")
        super().__init__()
        self.nota = None
        self.turno = "A"
    
    def setNota(self, nota = 0):
        self.nota = nota

    def convocar_examen(self):
        if self.nota and self.nota >= 5:
            print(f"{self.correo} - {self.nombre} - CONVOCADO ☻")

    def describe(self):
        print(f"{self.nombre} - {self.turno} - {self.correo} -> Nota : {self.nota}")

if __name__ == "__main__":
    alumno = Alumno()
    alumno.setNota(6.12)
    print(alumno)
