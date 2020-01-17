#Clase base
class Persona:
    def __init__(self,nombre):
        self.nombre = nombre
        print("Hola soy una persona")
        print ("Mi nombre es "+nombre)
    
    def saludar(self) :
        print("Buenos dias ",self.nombre) 

#La clase estudiante era de la clase persona
#Par mantener el metodo de inicio de Persona debemos invocarlo en el init de Estudiante y pasa los parametros
class Estudiante():
    def __init__(self,nombre,nota):
        Persona.__init__(self,nombre)
        print("Hola soy un estudiante")
        self.nota = nota

    def estudiar(self):
        print("Mi deber es estudiar y mi nota es ",self.nota)

#Vemos que Docente hereda de Persona los atributos pero no respeta el init
#pero heredara todos los atributos de persona y usamos el atributo herado nombre para mostar el apellido
class Docente(Persona):
    def __init__(self,apellido):
        print("Hola soy un docente")
        self.nombre = apellido
        

    def evaluar(self):
        print("Yo pongo la nota y mi apellido es", self.nombre)
