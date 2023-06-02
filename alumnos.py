from clases import Alumno

alumnos = [
    Alumno("Sofia", "B", "sofia@hotmail.com"),
    Alumno("Marco", "A", "marco@gmail.com"),
    Alumno("Pedro", "C", "pedro@hotmail.com"),
    Alumno("Miguel", "A", "miguel@hotmail.com")
]

alumnos[0].setNota(10)
alumnos[1].setNota(5)
alumnos[2].setNota(3)
alumnos[3].setNota()

for alumno in alumnos:
    alumno.describe()
    alumno.convocarExamen()