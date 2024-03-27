#Программа на Python, которая будет строить графический вектор с расчетом направлений от точки до точки 
#сети географических координат, мы можем использовать библиотеку Matplotlib.
#Ниже приведен пример кода:

import matplotlib.pyplot as plt
import geopy.distance

# Функция для вычисления направления между двумя точками
def calculate_direction(lat1, lon1, lat2, lon2):
    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)
    
    # Вычисление угла направления
    azimuth = geopy.distance.geodesic(coords_1, coords_2).initial_bearing
    
    return azimuth

# Координаты точек
points = [(55.7558, 37.6176), (51.5074, 0.1278), (40.7128, -74.0060)]

# Создание графического вектора
fig, ax = plt.subplots()
for i in range(len(points)-1):
    lat1, lon1 = points[i]
    lat2, lon2 = points[i+1]
    azimuth = calculate_direction(lat1, lon1, lat2, lon2)
    ax.arrow(lon1, lat1, lon2-lon1, lat2-lat1, head_width=1, head_length=1, fc='b', ec='b',
             length_includes_head=True, label=f'Direction: {round(azimuth, 2)} degrees')
    ax.scatter(lon1, lat1, color='red')
    ax.annotate(f'({lat1}, {lon1})', (lon1, lat1))

ax.scatter(points[-1][1], points[-1][0], color='red')
ax.annotate(f'({points[-1][0]}, {points[-1][1]})', (points[-1][1]-5, points[-1][0]-5))

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Geographic Vectors')
plt.show()

#Результат: графический вектор, показывающий направления между точками сети географических координат. Каждый вектор будет иметь стрелку, указывающую направление, а также координаты точек будут отображены на графике.
#Установите библиотеку Matplotlib и Geopy перед запуском программы:

pip install matplotlib
pip install geopy
