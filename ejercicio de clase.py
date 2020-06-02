class Robot:
      nombre = ''
      altura = ''
      peso = ''
      cantidad_de_circuitos = ''
      fecha_de_creacion = ''

      isCaminando = False
      isEncendido = False
      isSentado = False

      def encender(self):
          self.isEncendido = True
          print("El robot", self.nombre, " se ha encendido")

      def apagar(self):
          self.isEncendido = False
          print("El robot", self.nombre, " se ha apagado")

      def show_statuss(self):
          if self.isCaminando == True:
             print("El robot", self.nombre, " se encuentra caminando")
          else:
              print("El robot", self.nombre, " se encuentra detenido")

          if self.isEncendido == True:
              print("El robot", self.nombre, "  se encuentra encendido")
          else:
              print("El robot", self.nombre, " se encuentra apagado")

          if self.isSentado == True:
              print("El robot", self.nombre, "  se encuentra sentado")
          else:
              print("El robot", self.nombre, "se encuentra parado")

      def poner_a_caminar(self):
          self.isCaminando = True
          print("El robot", self.nombre, " se ha puesto a caminar")

      def detener(self):
          self.isCaminando = False
          print("El robot", self.nombre, " se ha detenido")

      def sentar(self):
          self.isSentado = True
          print("El robot", self.nombre, " se ha sentado")

      def parar(self):
          self.isSentado = False
          print("El robot", self.nombre, " se ha parado")


      def __init__(self, nombre = "", altura = "", peso = "", cantidad_de_circuitos = "", fecha_de_creacion = ""):
          self.nombre = nombre
          self.altura = altura
          self.peso = peso
          self.cantidad_de_circuitos = cantidad_de_circuitos
          self.fecha_de_creacion = fecha_de_creacion

      def show_attributes(self):
          print(self.nombre, " mide ", self.altura, " centímetros")
          print(self.nombre, " pesa ", self.peso, " kilos")
          print(self.nombre, " posee ", self.cantidad_de_circuitos, "circuitos")
          print(self.nombre, " fue creado el ", self.fecha_de_creacion)

alpha1 = Robot("Pedro", "160", "40", "2000", "8/12/2016")
alpha2 = Robot("Andrés", "180", "60", "2500", "17/09/2018")

alpha1.encender()
alpha1.poner_a_caminar()
alpha2.encender()
alpha2.sentar()

alpha1.show_attributes()
alpha2.show_attributes()







