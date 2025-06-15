#!/usr/bin/env python3
import random
import os

def main():
    seed = os.environ.get("GUESS_SEED")
    if seed is not None:
        try:
            random.seed(int(seed))
        except ValueError:
            pass
    target = random.randint(1, 100)
    attempts = 0
    print("Adivina el número del 1 al 100")
    while True:
        try:
            guess = int(input("Ingresa tu intento: "))
        except ValueError:
            print("Por favor ingresa un número válido")
            continue
        attempts += 1
        if guess < target:
            print("Más alto")
        elif guess > target:
            print("Más bajo")
        else:
            print(f"¡Correcto! Lo lograste en {attempts} intentos")
            break

if __name__ == "__main__":
    main()
