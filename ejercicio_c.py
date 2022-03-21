# Ejercicio diamante de la herencia múltiple

## El problema del diamante surge cuando dos subclases B y C heredan de la superclase superior A, y la subclase
# inferior D hereda de B y C (Con un diagrama podemos observarlo mejor). 
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


# Subclase
class B(A):
    # Uso de **kwargs en una función se usa para pasar, de forma opcional, un número variable de argumentos 
    # con nombre. El parámetro recibe los argumentos como un diccionario.
    # Metodo Constructor
    def __init__(self, b_param, **kwargs):
        # Super nos permite invocar y conservar un método o atributo de una clase base 
        # desde una subclase sin necesidad de nombrarla explícitamente.
        super().__init__(**kwargs)
        self.b = b_param



# Subclase 
class C(A):
    
## Subclase inferior
class D(B, C):
    
###
# I N I C I O   P R O G R A M A
#
