from alumno import Alumno
from aula import Aula
from profesor import Profesor

aulas = [Aula(), Aula(), Aula(), Aula(), Aula()]

contenedor = [
    {
        "aula": Aula(),
        "profesor": Profesor("Victor", 0, 10),
        "alumnos": [    
            Alumno("Sortilegio", "A", "shorty@hotmail.com"),
            Alumno("Marco", "A", "marco@gmail.com")
        ]
    },
    {
        "aula": Aula(),
        "profesor": Profesor("Antonio", 2, 8),
        "alumnos": [    
            Alumno("Pedro", "A", "pedro@hotmail.com"),
            Alumno("Raquel", "A", "raquel@gmail.com"),
        ]
    },
    {
        "aula": Aula(),
        "profesor": Profesor("Nuria", 0, 6),
        "alumnos": [    
            Alumno("Persefone", "A", "perse@gmail.com"),
            Alumno("Paula", "A", "paula@hotmail.com"),
            Alumno("Pepito", "A", "pepitoco@gmail.com"),
        ]
    },
    {
        "aula": Aula(),
        "profesor": None,
        "alumnos": [    
            Alumno("Johan", "A", "johan@hotmail.com"),
            Alumno("Jack", "A", "jack@gmail.com"),
            Alumno("Paula", "A", "sofia@hotmail.com"),
            Alumno("Pepito", "A", "marco@gmail.com")
        ]
    },
    {
        "aula": Aula(),
        "profesor": Profesor("Agustino", 3, 7),
        "alumnos": []
    }
]

for item in contenedor:
    item["aula"].set_profesor(item["profesor"])
    for alumno in item["alumnos"]:
        item["aula"].add(alumno)

    print("-----------------------------------------------------------------------")
    try:
        item["aula"].puntuar()
    except Exception as e:
        print(e)

    print()

    try:
        item["aula"].convocar_examenes()
    except Exception as e:
        print(e)
    print("-----------------------------------------------------------------------")

