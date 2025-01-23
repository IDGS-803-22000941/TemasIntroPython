import os

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre 0"

def run():
    while True:
        os.system('cls')  
        print("Menú de opciones:")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicar")
        print("4.- Dividir")
        print("5.- Salir")
        
        opcion = int(input("Dame una opción: "))
        
        if opcion == 5:
            break
        
        num1 = float(input("Dame el primer número: "))
        num2 = float(input("Dame el segundo número: "))
        
        if opcion == 1:
            print("Resultado:", sumar(num1, num2))
        elif opcion == 2:
            print("Resultado:", restar(num1, num2))
        elif opcion == 3:
            print("Resultado:", multiplicar(num1, num2))
        elif opcion == 4:
            print("Resultado:", dividir(num1, num2))
        else:
            print("Opción no válida")
        
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    run()
