import random

def jugar_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("Tienes que adivinar un número entre 1 y 100.")

    while True:
        intento = int(input("Introduce tu suposición: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break

    print("¡Gracias por jugar!")

if __name__ == "__main__":
    jugar_adivinanza()