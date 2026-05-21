from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from clases import Curso

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

cursos = session.query(Curso).all()

for curso in cursos:
    if "Zam" in curso.instructor.nombre:
        print("Curso: %s" % curso.titulo)
        print("Profesor: %s" % curso.instructor.nombre)
        print("-----------------------------")