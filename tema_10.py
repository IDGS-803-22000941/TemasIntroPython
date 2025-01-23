from io import open

texto="Hola me llamo angel vicenmte"
archivo=open("archivo.txt","w")
archivo.write(texto)
archivo.close()