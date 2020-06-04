# -*- coding: utf8 -*-

"""
try:
    file = open("archivo.txt", 'r')
    print(file.read())
except Exception as e:
    print("error: ", str(e))

else:
    file.close()
"""

try:
    file = open("archivo.txt", 'r')
    for line in file.readlines():
        print(line)
except Exception as e:
    print("error: ", str(e))

else:
    file.close()