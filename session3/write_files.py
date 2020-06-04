"""
try:
    file = open("archivito.txt", 'w')
    file.write("Esto es un contenido añadido...")

except Exception as e:
    print("error : ", str(e))

else:
    file.close()
    print(file)
"""

try:
    file = open("archivito.txt", 'a')
    file.write("Esto es un contenido añadido adicional...")
    file.write("\n")
    file.write("Esta es una línea más abajo")

except Exception as e:
    print("error : ", str(e))

else:
    file.close()
    print(file)