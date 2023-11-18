import matplotlib.pyplot as plt

# Datos de la gravedad en la Tierra
g = 9.81  # m/s^2

# Función para calcular la altura y velocidad en un tiempo dado
def calcular_altura_y_velocidad(tiempo):
    altura = 0.5 * g * tiempo**2
    velocidad = g * tiempo
    return altura, velocidad

# Tiempo de vuelo ingresado por el usuario
tiempo_de_vuelo = float(input("Ingrese el tiempo de vuelo en segundos: "))

# Calculamos la altura y velocidad en ese tiempo
altura, velocidad = calcular_altura_y_velocidad(tiempo_de_vuelo)

# Imprimimos los resultados
print(f"Altura a los {tiempo_de_vuelo} segundos: {altura} metros")
print(f"Velocidad a los {tiempo_de_vuelo} segundos: {velocidad} m/s")

# Graficamos la posición vs tiempo
tiempos = [t/10 for t in range(int(tiempo_de_vuelo*10)+1)]  # Muestreo del tiempo
alturas = [calcular_altura_y_velocidad(t)[0] for t in tiempos]

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(tiempos, alturas)
plt.title("Altura vs Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Altura (m)")

# Graficamos la velocidad vs tiempo
velocidades = [calcular_altura_y_velocidad(t)[1] for t in tiempos]

plt.subplot(1, 2, 2)
plt.plot(tiempos, velocidades)
plt.title("Velocidad vs Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")

plt.tight_layout()
plt.show()
