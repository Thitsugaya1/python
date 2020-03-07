num = int(raw_input("Ingrese numero: "))
i = 0
serie = 1
while i < num:
    if i % 2 == 0:
        serie += 2
    else:
        serie += 3
    i+=1
print serie