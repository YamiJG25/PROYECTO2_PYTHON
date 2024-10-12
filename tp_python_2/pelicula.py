# pelicula.py

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    # Getter para obtener el nombre de la película
    def obtener_nombre(self):
        return self.__nombre
