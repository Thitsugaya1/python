year = int(raw_input("Ingrese anio: "))

# Calculo de los valores para determinar el dia de pascua
a = year % 19
b = year % 4
c = year % 7
d = (19*a + 24) % 30
e = (2*b+4*c+6*d + 5) % 7

# Ver a que mes corresponde
if d+e < 10  :
    dia = d+e+22
    print "la pascua cae el", dia," de marzo"
else:
    dia = d+e-9
    print "la pascua cae el", dia,"de abril"
