import random

def obtener_opcion_usuario():
    """
    Solicita al usuario que elija entre piedra, papel o tijera.
    Returns:
    str: La opción elegida por el usuario.
    """
    while True:
        opcion_usuario = input("Elige piedra, papel o tijera: ").lower()
        if opcion_usuario in ["piedra", "papel", "tijera"]:
            return opcion_usuario
        else:
            print("Por favor elige una opción válida: piedra, papel o tijera.")

def determinar_ganador(opcion_usuario, opcion_cpu):
    """
    Determina el ganador del juego.
    Args:
    opcion_usuario (str): La opción elegida por el usuario.
    opcion_cpu (str): La opción elegida por la CPU.
    Returns:
    str: El resultado del juego.
    """
    if opcion_usuario == opcion_cpu:
        return "Empate"
    elif (opcion_usuario == "piedra" and opcion_cpu == "tijera") or (opcion_usuario == "papel" and opcion_cpu == "piedra") or (opcion_usuario == "tijera" and opcion_cpu == "papel"):
        return "¡Ganaste que crack :3!"
    else:
        return "¡Te gano la CPU :(!"

def jugar_juego():
    """
    Inicia el juego de piedra, papel o tijera.
    """
    print("¡BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA!")
    print("Creado por 'zlAngel'")
    print("\nEspero que te diviertas y recuerda respetar tu turno.\n")

    opciones = ["piedra", "papel", "tijera"]

    while True:  # Bucle que permite jugar múltiples veces
        opcion_usuario = obtener_opcion_usuario()
        opcion_cpu = random.choice(opciones)

        print(f"Tu elección: {opcion_usuario}")
        print(f"La CPU eligió: {opcion_cpu}")

        ganador = determinar_ganador(opcion_usuario, opcion_cpu)
        print(ganador)

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (si/no): ").lower()
        if jugar_nuevamente != "si":
            break  # Salir del bucle si la respuesta es "no"
    print("Fin del Juego")

jugar_juego()