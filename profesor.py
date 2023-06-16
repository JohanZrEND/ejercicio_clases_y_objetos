from random import randint, uniform
from user import User

class Profesor(User):

    VALID_NOTES = {
        "min": (0.0, 4.0),
        "max": (6.0, 10.0)
    }

    def __init__(self, nota_minima, nota_maxima):
        super().__init__()

        def validar_nota_minima(nota_minima):
            min = self.VALID_NOTES["min"][0]
            max = self.VALID_NOTES["min"][1]

            if not str(nota_minima).isnumeric():
                raise Exception("La nota debe ser un número")
            if nota_minima < min:
                raise Exception(f"La nota minima debe estar por encima de {min}")
            if nota_minima > max:
                raise Exception(f"La nota maxima debe estar por debajo de {max}")

            return nota_minima

        def validar_nota_maxima(nota_maxima):
            min = self.VALID_NOTES["max"][0]
            max = self.VALID_NOTES["max"][1]

            if not str(nota_minima).isnumeric():
                raise Exception("La nota debe ser un número")
            if nota_maxima < min: 
                raise Exception(f"La nota maxima debe estar por encima de {min}")
            if nota_maxima > max:
                raise Exception(f"La nota maxima debe estar por debajo de {max}")

            return nota_maxima

        self.nota_minima = validar_nota_minima(nota_minima) 
        self.nota_maxima = validar_nota_maxima(nota_maxima)
    
    def __str__(self) -> str:
        return f"{super().__str__()} [{self.nota_minima}/{self.nota_maxima}]"

    def generar_nota(self):
        return(uniform(self.nota_minima, self.nota_maxima))

if __name__ == "__main__":
    profe = Profesor(randint(0,4), randint(6,10))
    print(profe)
