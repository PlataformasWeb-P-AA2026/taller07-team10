from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from clases import Curso

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

cursos = session.query(Curso).all()

for curso in cursos:
    print("Curso: %s" % curso.titulo)

    for tarea in curso.tareas:
        print("  Tarea: %s" % tarea.titulo)

    print("-----------------------------")