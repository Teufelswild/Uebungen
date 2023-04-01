#uebung-3
##aufgabe-1
import math

class Figur:
    def __init__(self):
        self.name = "Figur"

    def Umfang(self):
        return 0
    
    def __str__(self):
        return self.name



class Point:
    def __init__(self,ost=0,nord=0):
        
        self._ost=ost
        self._nord=nord

    def __str__(self):
        return 'POINT ('+str(self._ost)+','+str(self._nord)+')'
    
    def getOst(self):
        return self._ost

    def getNord(self):
        return self._nord
    
class Dreieck(Figur):
    def __init__(self,A,B,C):
    
        self.A=A
        self.B=B
        self.C=C
        
    def name(self):
        return 'Dreieck'
    
    def __str__(self):
        return 'DREIECK ('+str(self.A)+', '+str(self.B)+', '+str(self.C)+')'
    
    def Umfang(self):
        a=((B.getOst()-C.getOst())**2+(B.getNord()-C.getNord()**2))**0.5
        b=((A.getOst()-C.getOst())**2+(A.getNord()-C.getNord()**2))**0.5
        c=((A.getOst()-B.getOst())**2+(A.getNord()-B.getNord()**2))**0.5
        
        return a+b+c

class Rechteck(Figur):
    def __init__(self,A,B):
        
        self.A=A
        self.B=B
        
    def name(self):
        return 'Rechteck'
    
    def __str__(self):
        return 'RECHTECK ('+str(self.A)+', '+str(self.B)+')'
    
    def Umfang(self):
        a=B.getOst()-A.getOst()
        b=B.getNord()-A.getNord()
        return 2*a+2*b
    
class Kreis(Figur):
    def __init__(self,mittelpunkt,radius):
        
        self.mittelpunkt=mittelpunkt
        self.radius=radius
        
    def name(self):
        return 'KREIS'
    
    def __str__(self):
        return 'KREIS ('+str(self.mittelpunkt)+', '+str(self.radius)+')'
    
    def Umfang(self):
        return 2*math.pi*self.radius
    
class Polygon(Figur):
    def __init__(self,A,B,C,*D):
        
        self.A=A
        self.B=B
        self.C=C
        self.D=D
        
    def __str__(self):
        
        text = 'POLYGON ({}, {}, {}'.format(self.A, self.B, self.C)
        for point in self.D:
            text += ', {}'.format(point)
        text += ')'
        
        return text
    
    
    def name(self):
        return 'POLYGON'
    
    def Umfang(self):
        
        a = ((self.B.getOst() - self.A.getOst()) ** 2 + (self.B.getNord() - self.A.getNord()) ** 2) ** 0.5
        b = ((self.C.getOst() - self.B.getOst()) ** 2 + (self.C.getNord() - self.B.getNord()) ** 2) ** 0.5
        c = ((self.A.getOst() - self.C.getOst()) ** 2 + (self.A.getNord() - self.C.getNord()) ** 2) ** 0.5
        
        if not self.D:
            return a+b+c
        
        x = 0
    
        for i in range(len(self.D) - 1):
              x += ((self.D[i + 1].getOst() - self.D[i].getOst()) ** 2 + (self.D[i + 1].getNord() - self.D[i].getNord()) ** 2) ** 0.5
        x += ((self.D[-1].getOst() - self.A.getOst()) ** 2 + (self.D[-1].getNord() - self.A.getNord()) ** 2) ** 0.5
    
        return a + b + c + x

