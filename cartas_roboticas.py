import random

# Función para generar un robot con atributos aleatorios
def generar_robot(nombre):
    return {
        "Nombre": nombre,
        "Batería": random.randint(0, 100),  # Batería en porcentaje (0% a 100%)
        "Utilidad": random.choice(["Doméstico", "Industrial", "Médico", "Militar"]),
        "Inteligencia": random.randint(50, 200),  # Nivel de inteligencia (50 a 200)
        "Velocidad": random.randint(1, 10)  # Velocidad en una escala de 1 a 10
    }

# Función para generar una carta robótica
def generar_carta_robot(robot):
    carta = f"""
    **Carta Robótica**
    Nombre: {robot['Nombre']}
    Batería: {robot['Batería']}%
    Utilidad: {robot['Utilidad']}
    Inteligencia: {robot['Inteligencia']}
    Velocidad: {robot['Velocidad']}/10
    --------------------------
    """
    return carta

# Lista de nombres de robots
nombres_robots = ["Robo-1", "Robo-2", "Robo-3", "Robo-4", "Robo-5"]

# Generar cartas para cada robot
for nombre in nombres_robots:
    robot = generar_robot(nombre)
    carta = generar_carta_robot(robot)
    print(carta)