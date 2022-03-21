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
