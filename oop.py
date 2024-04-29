class Profesor:
    def __init__(self ,el_nombre, el_gmail):
        self.nombre = el_nombre
        self.gmail = el_gmail
    
    def dame_tu_nombre(self):
        return self.nombre


class Alumno:
    def __init__(self , el_elegido):
        self.nombre = el_elegido
        self.inasistencia = 0
        self.dieta = ""
        self.mentor = None

    def mentoria(self,profesor):
        self.mentor = profesor
    
    def falta(self):
        self.inasistencia +=1

    def elegir_dieta(self ,la_dieta):
        self.dieta = la_dieta

    def es_vegano(self):
        self.dieta = "Vegano"


    def esta_libre(self):
        if self.inasistencia >5:
            return "ESTA LIBRE"
        else:
            return "Esta Ok"
    


profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabi","gabiel@gmail.com")

print(profe_elio.dame_tu_nombre())
print(profe_gabi.dame_tu_nombre())

alumno_gino = Alumno("Gino")
alumno_emma = Alumno("Emmanuel")

alumno_gino.falta()
alumno_gino.falta()
alumno_gino.falta()
alumno_gino.falta()
alumno_gino.falta()
alumno_gino.falta()
print(alumno_gino.esta_libre())

alumno_emma.elegir_dieta("Vegetariano")
print(alumno_emma.dieta)
alumno_gino.es_vegano
print(alumno_gino.dieta)

alumno_gino.mentoria(profe_elio)
print(alumno_gino.mentor)




import ipdb; ipdb.set_trace()