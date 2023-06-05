from alumno import Alumno
from aula import Aula

aula = Aula()

aula.add(Alumno("Sofia", "B", "sofia@hotmail.com"))
aula.add(Alumno("Marco", "A", "marco@gmail.com"))
aula.add(Alumno("Pedro", "C", "pedro@hotmail.com"))
aula.add(Alumno("Miguel", "A", "miguel@hotmail.com"))
aula.add(Alumno("Hugo", "B", "hugo@gmail.com"))
aula.add(Alumno("Raquel", "A", "raquel@gmail.com"))
aula.add(Alumno("Pepe", "C", "pepe@gmail.com"))

aula.listar()
turno = input("Que grupo vamos a convocar? ").upper()
aula.convocarExamen(turno)
