import matplotlib.pyplot as plt
import numpy as np

# Функция, которая строит график выхода на орбиту
def orbit_entry(altitude):
  x = np.linspace(0, altitude, 100)
  y = np.sqrt(x * altitude)
  plt.plot(x, y, label='Выход на орбиту Земли(высота в км)')

# Функция, которая рисует орбиту планеты
def draw_orbit(altitude, orbit_speed):
  t = np.linspace(0, 2 * np.pi, 100)
  x = altitude * np.cos(t)
  y = altitude * np.sin(t)
  plt.plot(x, y, label='Орбита Земли(км)')

# Главная функция, которая будет запускать все остальные и рисовать график
def main():
  print("Расчет траектории спутника")
  print("==========================================")
  # Начинай писать код на строке снизу

  altitude = float(input("Введите высоту в км: "))
  orbit_speed = float(input("Введите скорость в км/ч:"))

if __name__ == "__main__":
  main()
