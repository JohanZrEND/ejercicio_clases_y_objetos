import random
from user import User

class Profesor(User):
    def __init__(self, nombre, nota_minima, nota_maxima):

        VALID_NOTES = {
            "min": (0.0, 4.0),
            "max": (6.0, 10.0)
        }

        def validar_nota_minima(nota_minima):
            min = VALID_NOTES["min"][0]
            max = VALID_NOTES["min"][1]

            if not str(nota_minima).isnumeric():
                raise Exception("La nota debe ser un número")
            if nota_minima < min:
                raise Exception(f"La nota minima debe estar por encima de {min}")
            if nota_minima > max:
                raise Exception(f"La nota maxima debe estar por debajo de {max}")

            return nota_minima

        def validar_nota_maxima(nota_maxima):
            min = VALID_NOTES["max"][0]
            max = VALID_NOTES["max"][1]

            if not str(nota_minima).isnumeric():
                raise Exception("La nota debe ser un número")
            if nota_maxima < min: 
                raise Exception(f"La nota maxima debe estar por encima de {min}")
            if nota_maxima > max:
                raise Exception(f"La nota maxima debe estar por debajo de {max}")

            return nota_maxima

        self.nombre = nombre
        self.nota_minima = validar_nota_minima(nota_minima) if nota_minima else random.randint(VALID_NOTES["min"][0])
        self.nota_maxima = validar_nota_maxima(nota_maxima)
    
    def __str__(self) -> str:
        return f"{self.nombre} [{self.nota_minima}/{self.nota_maxima}]"


    def generar_nota(self):
        return(random.uniform(self.nota_minima, self.nota_maxima))