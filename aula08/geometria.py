#region Área
def areatriangulo(b,a):
    return (b * a) / 2

def areaquadrado(lado):
    return lado ** 2

def arearetangulo(b,a):
    return b * a

def areacirculo(r):
    return  (r**2) * 3.14

def areatrapezio(B,b,a):
    return ((B + b) * a)  / 2
#endregion
#region Perímetro
def perimetrotriangulo(l1,l2,l3):
    return l1 + l2 + l3

def perimetroquadrado(lado):
    return lado * 4

def perimetroretangulo(b,a):
    return (b + a) * 2

def perimetrocirculo(r):
    return 3.14 * r * 2

def perimetrotrapezio(B,b,l1,l2):
    return B + b + l1 + l2
#endregion
#region volume
def volumepiramide(b,a,A):
    return ((b * a) / 2 ) * A

def volumecubo(lado):
    return lado ** 3

def volumeparalele(c,l,a):
    return c * l * a 

def volumecilindro(r,a):
    return 3.14 * (r ** 2) * a

def volumeprisma(B,b,a,A):
    return (((B + b) * a )/ 2) * A
#endregion
