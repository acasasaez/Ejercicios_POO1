# Ejercicio diamante de la herencia múltiple

# El problema del diamante surge cuando dos subclases B y C heredan de la superclase superior A, y la subclase
# inferior D hereda de B y C (Con un diagrama podemos observarlo mejor y vemos porque se conoce como "el problema del diamante"). 
# Entonces el problema empieza cuando un método de D llama a un método en A ya que no se
# sabe si hereda de B o de C. 
# 
# En los diferentes lenguajes de programación hay una resolución diferente. Python da como solución
# una lista de clases que se buscan de izquierda a derecha y de abajo a arriba  y luego elimina todas 
# las apariciones de una clase repetida menos la última. 
#
# Ejercicio resuelto con el método super 


### C L A S E S

# Clase superior o base
class A:
    # Metodo Constructor
    def __init__(self, a):
        self.a = a

# Subclase que hereda de clase A
class B(A):
    # Uso de **kwargs en una función se usa para pasar, de forma opcional, un número variable de argumentos 
    # con nombre. El parámetro recibe los argumentos como un diccionario.
    # Metodo Constructor
    def __init__(self, b, **kwargs):
        # Super nos permite acceder desde la subclase  a metodos  o atributos de la clase base.
        super().__init__(**kwargs)
        self.b = b

# Subclase que hereda de clase A
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
###

# Instanciar
d = D(1, 2, 3)
print(isinstance(d, A), isinstance(d, B), isinstance(d, C)) ## COMPRUEBA si d es una instancia de A,B,C
print(d.a, d.b, d.c) ### Imprimirá 1 ,2 ,3

## Todos los objetoos en Python heredan, en primera instancia, de OBJECT. Y se puede comprobar con el mro() .
#  Orden de Resolución de Métodos. Devuelve una lista de tipos de los que deriva la clase, en el orden en que se buscan los métodos.
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())



