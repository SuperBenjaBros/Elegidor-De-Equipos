import random  # Importamos la librería 'random' para poder mezclar la lista de jugadores aleatoriamente

# 1. Solicitamos la cantidad de grupos
num_grupos = int(input("\n\n\nIngresa el número de grupos: "))

# 2. Solicitamos la cantidad de participantes que tendrá cada grupo
num_participantes = int(input("Ingresa el número de participantes en cada grupo: "))

# Calculamos el total de jugadores requeridos
total_jugadores = num_grupos * num_participantes
print(f"\nSe necesitan {total_jugadores} jugadores en total.\n")

# 3. Pedimos el nombre de cada jugador individualmente
jugadores = []  # Lista donde almacenaremos los nombres
for i in range(total_jugadores):
    nombre = input(f"Jugador {i+1}: ")  # Pedimos el nombre del jugador
    jugadores.append(nombre)

# 4. Mezclamos la lista de jugadores de forma aleatoria para asignarlos a equipos sin favoritismos
random.shuffle(jugadores)

# 5. Creamos los grupos dividiendo la lista según el número de participantes por grupo
grupos = []
for i in range(num_grupos):
    # Extraemos el segmento correspondiente a cada grupo
    grupo = jugadores[i * num_participantes:(i + 1) * num_participantes]
    grupos.append(grupo)

# 6. Imprimimos los equipos en el formato solicitado
print("\nEquipos:")
for indice, grupo in enumerate(grupos, start=1):
    # Convertimos la lista de integrantes en una cadena separada por comas
    integrantes = ", ".join(grupo)
    print(f"- Equipo {indice}: {integrantes}")
