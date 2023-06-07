from alumno import Alumno
from aula import Aula
from profesor import Profesor

aula = Aula()

mi_profe = Profesor("javier", 0, 10)
aula.set_profesor(mi_profe)

aula.add(Alumno("Sofia", "A", "sofia@hotmail.com"))
aula.add(Alumno("Marco", "A", "marco@gmail.com"))
aula.add(Alumno("Pedro", "A", "pedro@hotmail.com"))
aula.add(Alumno("Miguel", "A", "miguel@hotmail.com"))
aula.add(Alumno("Hugo", "A", "hugo@gmail.com"))
aula.add(Alumno("Raquel", "A", "raquel@gmail.com"))
aula.add(Alumno("Pepe", "A", "pepe@gmail.com"))

aula.puntuar()
print()
aula.convocar_examenes()
