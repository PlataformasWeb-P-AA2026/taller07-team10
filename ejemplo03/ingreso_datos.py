from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from configuracion import cadena_base_datos
from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Departamentos
archivo = open("01_departamento.csv", "r", encoding="utf-8")
next(archivo)

for linea in archivo:
    datos = linea.strip().split(",")

    departamento = Departamento(
        id=int(datos[0]),
        nombre=datos[1]
    )

    session.add(departamento)

archivo.close()

# Instructores
archivo = open("02_instructor.csv", "r", encoding="utf-8")
next(archivo)

for linea in archivo:
    datos = linea.strip().split(",")

    instructor = Instructor(
        id=int(datos[0]),
        nombre=datos[1]
    )

    session.add(instructor)

archivo.close()

# Cursos
archivo = open("03_curso.csv", "r", encoding="utf-8")
next(archivo)

for linea in archivo:
    datos = linea.strip().split(",")

    curso = Curso(
        id=int(datos[0]),
        titulo=datos[1],
        departamento_id=int(datos[2]),
        instructor_id=int(datos[3])
    )

    session.add(curso)

archivo.close()

# Estudiantes
archivo = open("04_estudiante.csv", "r", encoding="utf-8")
next(archivo)

for linea in archivo:
    datos = linea.strip().split(",")

    estudiante = Estudiante(
        id=int(datos[0]),
        nombre=datos[1]
    )

    session.add(estudiante)

archivo.close()

# Inscripciones
archivo = open("05_inscripcion.csv", "r", encoding="utf-8")
next(archivo)

for linea in archivo:
    datos = linea.strip().split(",")

    inscripcion = Inscripcion(
        estudiante_id=int(datos[0]),
        curso_id=int(datos[1]),
        fecha_inscripcion=datetime.strptime(datos[2], "%Y-%m-%d %H:%M:%S")
    )

    session.add(inscripcion)

archivo.close()

# Tareas
archivo = open("06_tarea.csv", "r", encoding="utf-8")
next(archivo)

for linea in archivo:
    datos = linea.strip().split(",")

    tarea = Tarea(
        id=int(datos[0]),
        curso_id=int(datos[1]),
        titulo=datos[2],
        fecha_entrega=datetime.strptime(datos[3], "%Y-%m-%d %H:%M:%S")
    )

    session.add(tarea)

archivo.close()

# Entregas
archivo = open("07_entrega.csv", "r", encoding="utf-8")
next(archivo)

for linea in archivo:
    datos = linea.strip().split(",")

    entrega = Entrega(
        id=int(datos[0]),
        tarea_id=int(datos[1]),
        estudiante_id=int(datos[2]),
        fecha_envio=datetime.strptime(datos[3], "%Y-%m-%d %H:%M:%S"),
        calificacion=float(datos[4])
    )

    session.add(entrega)

archivo.close()

session.commit()