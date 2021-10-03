fichero = open("ejemplo1.txt","r")
lineas = fichero.readlines()
for j in range (0,len(lineas)):
    print(f"{j}",lineas[j])

fichero.close()