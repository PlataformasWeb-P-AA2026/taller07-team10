from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Club, Jugador
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Lectura de clubes
archivo = open("data/datos_clubs.txt", "r", encoding="utf-8-sig")

for linea in archivo:
    datos = linea.strip().split(";")

    club = Club(
        nombre=datos[0],
        deporte=datos[1],
        fundacion=int(datos[2])
    )

    session.add(club)

archivo.close()

session.commit()

# Lectura de jugadores
archivo = open("data/datos_jugadores.txt", "r", encoding="utf-8-sig")

for linea in archivo:
    datos = linea.strip().split(";")

    club = session.query(Club).filter_by(
        nombre=datos[0]
    ).one()

    jugador = Jugador(
        posicion=datos[1],
        dorsal=int(datos[2]),
        nombre=datos[3],
        club=club
    )

    session.add(jugador)

archivo.close()

session.commit()