# Ejercicios_POO1

Ejercicio 2:
```
  class Base: 

      def __init__(self): 
          self.a = "a" 
          self.b = "b" 
          self.c = "c" 

      def A(self): 
          print(self.a) # Imprime "a"
          
      def B(self): 
          print(self.b) #Imprime "b"

      def C(self): 
          print(self.c) #Imrime "c"

  class Derivada(Base): # La clase derivada hereda los métodos y atributos de la clase Base

      def __init__(self): 
          self.a = "aa" #Self.a toma el valor "aa"
-         super().__init__() #Con el método super().__init__ estamos accediendo a los atributos del contructor de la clase Base (clase padre), por lo tanto self.a,               self.b y self.c recuperan el valor que le habíamos atribuído ("a","b","c"; respectivamente)
          self.c = "cc" #Ahora self.c cambia su valor a "cc"

      def A(self): 
          print(self.a) #Imprime "a" 

      def B(self): #Imprime 2 veces self.b, una en la llamada del método B de la clase padre y otra por el print dentro del propio método
          self.b = "bb" #self.b toma el valor "bb"
          super().B() #accedemos al método B en la Clase base, recordemos que tenía como resultado imprimir self.b, que ahora toma el valor "bb"
          print(self.b) #Imprime "bb"

  base = Base() 
  derivada = Derivada() 

  base.A() Resultado: a
  derivada.A() Resultado: a
  print() Resultado: Espacio en blanco 
  base.B() Resultado: b
  derivada.B() Resultado: bb
                          bb
  base.C() Resultado: c
  derivada.C() Resltado: cc
  derivada = base # ahora derivada pasa a ser un objeto de tipo Base 
  derivada.C() Resultado:c



Ejercicio 4:
```
class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        slf.ventanas = []

class Ventana:
    def __init__(self, pared, superficie, proteccion):
        self.pared = pared
        self.superficie = superficie
        self.pared.ventanas.append(self)
        if proteccion in None:
            raise Exception("Protección obligatoria")
        self.proteccion = proteccion

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes
    def superficie_cristal(self):
        superficie = 0
        for pared in self.paredes:
            for ventana in pared.ventanas:
                superficie += ventana.superficie
        return superficie

pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = Pared("SUR") 
pared_este = Pared("ESTE") 

# Instanciación de las ventanas 
ventana_norte = Ventana(pared_norte, 0.5, "persiana") 
ventana_oeste = Ventana(pared_oeste, 1, "persiana") 
ventana_sur = Ventana(pared_sur, 2, "store venitien") 
ventana_este = Ventana(pared_este, 1, "persiana") 

# Instanciación de la casa con las 4 paredes 
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
print(casa.superficie_cristal()) 

class ParedCortina(Pared, Ventana):
    def __init__(self, orientacion, superficie):
        Pared.__init__(self, orientacion)
        Ventana.__init__(self, self, superficie, "Ninguna")
    

pared_cortina = ParedCortina("SUR", 10)
casa.paredes[2] = pared_cortina 
print(casa.superficie_cristal()) 
```
