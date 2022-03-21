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
