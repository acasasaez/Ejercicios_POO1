# Ejercicio diamante de la herencia múltiple

## El problema del diamante surge cuando dos subclases B y C heredan de la superclase superior A, y la subclase
# inferior D hereda de B y C (Con un diagrama podemos observarlo mejor). 
# Entonces el problema empieza cuando un método de D llama a un método en A ya que no se
# sabe si hereda de B o de C. 
# 
# En los diferentes lenguajes de programación hay una resolución diferente. Python da como solución
# una lista de clases que se buscan de izquierda a derecha y de abajo a arriba  y luego elimina todas 
# las apariciones de una clase repetida menos la última.



