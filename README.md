# Ejercicios_POO1

Ejercicio 1:
```
class Punto2D:
    x = int(input("Introduce la coordenada inicial del eje x: "))
    y = int(input("Introduce la coordenada inicial del eje y: "))
    print("El punto incicial P = {}, {}".format(x,y))
    def punto():
        global a
        global b
        a = int(input("Introduce la coordenada del segundo punto del eje x: "))
        b = int(input("Introduce la coordenada del segundo punto del eje y: "))

    punto()   
    def traslacion(x, y):
        x = x + a
        y = y + b
        print("Después de la traslación el punto T = {}, {}".format(x,y))
        return x, y
    traslacion(x, y)
Punto2D

class Punto3D:
    x = int(input("Introduce la coordenada inicial del eje x: "))
    y = int(input("Introduce la coordenada inicial del eje y: "))
    z = int(input("Introduce la coordenada inicial del eje z: "))
    print("El punto incicial P = {}, {}, {}".format(x,y, z))
    def punto():
        global a
        global b
        global c
        a = int(input("Introduce la coordenada del segundo punto del eje x: "))
        b = int(input("Introduce la coordenada del segundo punto del eje y: "))
        c = int(input("Introduce la coordenada del segundo punto del eje z: "))

    punto()   
    def traslacion(x, y, z):
        x = x + a
        y = y + b
        z = z + c
        print("Después de la traslación el punto T = {}, {}, {}".format(x,y,z))
        return x, y, z
    
    traslacion(x, y, z)
Punto3D
```

Ejercicio 2: En este apartado se nos pide que resultado mostrarán en pantalla el sieguiente programa:
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
```
Ejercicio 3:
```
# Ejercicio diamante de la herencia múltiple

## El problema del diamante surge cuando dos subclases B y C heredan de la superclase superior A, y la subclase
# inferior D hereda de B y C (Con un diagrama podemos observarlo mejor y vemos porque se conoce como "el problema del diamante"). 
# Entonces el problema empieza cuando un método de D llama a un método en A ya que no se
# sabe si hereda de B o de C. 
# 
# En los diferentes lenguajes de programación hay una resolución diferente. Python da como solución
# una lista de clases que se buscan de izquierda a derecha y de abajo a arriba  y luego elimina todas 
# las apariciones de una clase repetida menos la última. 


### C L A S E S

# Clase superior o base
class A:
    # Metodo Constructor
    def __init__(self, a):
        self.a = a


# Subclase que hereda de clase base
class B(A):
    # Uso de **kwargs en una función se usa para pasar, de forma opcional, un número variable de argumentos 
    # con nombre. El parámetro recibe los argumentos como un diccionario.
    # Metodo Constructor
    def __init__(self, b, **kwargs):
        # Super nos permite invocar y conservar un método o atributo de una clase base 
        # desde una subclase sin necesidad de nombrarla explícitamente.
        super().__init__(**kwargs)
        self.b = b


# Subclase que hereda de clase base
class C(A):
    # Metodo constructor 
    def __init__(self, c, **kwargs):
        super().__init__(**kwargs)
        self.c = c # Nuevo atributo para la subclase

## Subclase inferior que hereda de B y C
class D(B, C):
    # Metodo constructor
    def __init__(self, a1, b1, c1):
        super().__init__(a = a1, b= b1, c = c1)
    
###
# I N I C I O   P R O G R A M A
#
```

Ejercicio 4:

```
class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        slf.ventanas = []

class Ventana:
    def __init__(self, pared, superficie):
        self.pared = pared
        self.superficie = superficie

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
ventana_norte = Ventana(pared_norte, 0.5) 
ventana_oeste = Ventana(pared_oeste, 1) 
ventana_sur = Ventana(pared_sur, 2) 
ventana_este = Ventana(pared_este, 1) 

# Instanciación de la casa con las 4 paredes 
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
print(casa.superficie_cristal()) 

class ParedCortina(Pared, Ventana):
    def __init__(self, orientacion, superficie):
        Pared.__init__(self, orientacion)
        Ventana.__init__(self, self, superficie)
    

pared_cortina = ParedCortina("SUR", 10)
casa.paredes[2] = pared_cortina 
print(casa.superficie_cristal()) 

```
