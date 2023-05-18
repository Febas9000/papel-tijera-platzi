import random

tipos = ["piedra", "papel", "tijera"]


rounds = 0

while True:
    user_option = input("Ingresa una opcion: piedra/papel/pijera -> ")
    bot_option = random.choice(tipos)

    if not user_option in tipos:
        print("La opcion no es valida")
        continue

    if user_option == bot_option:
        print(f"¡Fue un empate! el bot eligio {user_option} y tu elegiste {bot_option}")

    elif bot_option == "piedra":
        if user_option == "papel":
            print("El bot eligio piedra y tu papel asi que ganaste")
        else:
            print(f"El bot eligio piedra y tu {user_option}, asi que perdiste el juego")

    elif bot_option == "papel":
        if user_option == "tijera":
            print("El bot eligio papel y tu tijera asi que ganaste")
        else:
            print(f"El bot eligio papel y tu {user_option}, asi que perdiste el juego")

    elif bot_option == "tijera":
        if user_option == "piedra":
            print("El bot eligio tijera y tu piedra asi que ganaste")
        else:
            print(f"El bot eligio tijera y tu {user_option}, asi que perdiste el juego")
    
    rounds += 1


    if rounds > 3:
        print("La partida finalizo!")
        break

