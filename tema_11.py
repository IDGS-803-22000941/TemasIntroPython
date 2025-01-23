from io import open

texto="Hola jejeje"
archivo=open("archivo.txt","r")

texto=archivo.readline()
print(texto)

archivo.close()