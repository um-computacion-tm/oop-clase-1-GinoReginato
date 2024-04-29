class  Persona:

    def __init__(self, nombre: str = "Gino", apellido: str = "reginato",dni: str = "46396875"):
        __atributo1__= 0
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__dni__ = dni

    def mostrar_datos(self):
        print(f'Mis datos son nombre = {self.__nombre__} apellido = {self.__apellido__} documento = {self.__dni__}')