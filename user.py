from generador_nombre import GeneradorDeNombre

class User:
    def __init__(self):
        gen = GeneradorDeNombre()
        self.nombre = gen.get_name()
        self.turno = "A"
        self.correo = gen.get_email()
    
    def __str__(self):
        return f"{self.nombre} - {self.turno} - {self.correo}"

