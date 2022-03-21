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
    