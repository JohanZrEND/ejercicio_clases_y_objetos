class Alumno():

    def __init__(self, nombre, turno, correo):
        self.nombre = nombre
        self.turno = turno
        self.correo = correo


    def setNota(self, nota=0):
        self.nota = nota

    def convocarExamen(self):
        if self.nota >= 5:
            print(f"Convocado")
        else:
            print(f"NO Convocado")

    def describe(self):
        print(f"{self.nombre} - {self.turno} -  {self.correo} - {self.nota}")


