from generador_nombre import GeneradorDeNombre

class Alumno:

    def __init__(self):
        gen = GeneradorDeNombre()
        self.nombre = gen.get_name()
        self.turno = "A"
        self.correo = gen.get_email()

    def setNota(self, nota=0):
        self.nota = nota

    def convocar_examen(self):
            if self.nota >= 5:
                print(f"{self.correo} - {self.nombre} - CONVOCADO ☻")

    def describe(self):
        print(f"{self.nombre} - {self.turno} - {self.correo} -> Nota : {self.nota}")
