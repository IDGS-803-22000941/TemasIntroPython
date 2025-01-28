class Traductor:
    def __init__(self):
        self.archivo = 'diccionario.txt'

    def capturar_palabra(self):
        palabra_espanol = input("Palabra español: ")
        palabra_ingles = input("Palabra inglés: ")
        
        archivo = open(self.archivo, 'a')
        archivo.write("{}:{}\n".format(palabra_espanol, palabra_ingles))
        archivo.close()
        
        print("Palabra guardada")

    def buscar_palabra(self):
        print("Buscar en:")
        print("1. Español")
        print("2. Inglés")
        
        opcion = input("Opción: ")
        palabra = input("Palabra: ")
        
        archivo = open(self.archivo, 'r')
        lineas = archivo.read().splitlines()
        archivo.close()
        
        for linea in lineas:
            esp, ing = linea.split(':')
            
            if opcion == '1':
                if palabra == esp:
                    print("Traducción: {}".format(ing))
                    return
            
            if opcion == '2':
                if palabra == ing:
                    print("Traducción: {}".format(esp))
                    return
        
        print("Palabra no encotda")

def main():
    traductor = Traductor()
    
    while True:
        print("\nTraductor")
        print("1.Capturar palabra")
        print("2.Buscar palabra")
        print("3.Salir")
        
        opcion = input("Opción: ")
        
        if opcion == '1':
            traductor.capturar_palabra()
        else:
            if opcion == '2':
                traductor.buscar_palabra()
            else:
                if opcion == '3':
                    break
                else:
                    print("Opción inválida")

if __name__ == "__main__":
    main()