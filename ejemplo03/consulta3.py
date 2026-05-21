from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from clases import Inscripcion

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

inscripciones = session.query(Inscripcion).all()

for inscripcion in inscripciones:
    if inscripcion.curso.departamento.nombre == "Ciencias de la Computación":
        print("Estudiante: %s" % inscripcion.estudiante.nombre)
        print("Curso: %s" % inscripcion.curso.titulo)
        print("Profesor: %s" % inscripcion.curso.instructor.nombre)
        print("-----------------------------")