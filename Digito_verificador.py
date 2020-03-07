#Calcuo del digito verificador
dig1=int(raw_input("digito 1: ")) *3
dig2=int(raw_input("digito 2: ")) *2
dig3=int(raw_input("digito 3: ")) *7
dig4=int(raw_input("digito 4: ")) *6
dig5=int(raw_input("digito 5: ")) *5
dig6=int(raw_input("digito 6: ")) *4
dig7=int(raw_input("digito 7: ")) *3
dig8=int(raw_input("digito 8: ")) *2
suma = dig8+dig7+dig6+dig5+dig4+dig3+dig2+dig1
resto = suma%11
if (11-resto) < 10:
    print "El digito verificador es: ",11-resto
elif (11-resto) == 10:
    print "El digito verificador es: k"
elif (11-resto) == 11:
    print "El digito verificador es: 0"
