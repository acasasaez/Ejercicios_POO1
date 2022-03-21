# Ejercicios_POO1

Ejercicio 2:
```
  class Base: 

      def __init__(self): 
          self.a = "a" 
          self.b = "b" 
          self.c = "c" 

      def A(self): 
          print(self.a) 

      def B(self): 
          print(self.b) 

      def C(self): 
          print(self.c) 

  class Derivada(Base): 

      def __init__(self): 
          self.a = "aa" 
          super().__init__() 
          self.c = "cc" 

      def A(self): 
          print(self.a) 

      def B(self): 
          self.b = "bb" 
          super().B() 
          print(self.b) 

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
  derivada = base 
  derivada.C() Resultado:c
