from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from clases import Entrega

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

entregas = session.query(Entrega).all()

for entrega in entregas:
    print("Estudiante: %s" % entrega.estudiante.nombre)
    print("Tarea: %s" % entrega.tarea.titulo)
    print("Profesor: %s" % entrega.tarea.curso.instructor.nombre)
    print("-----------------------------")