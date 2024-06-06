import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, xp):
    yp = 0
    n = len(x)
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += p * y[i]
    return yp

# Data yang diberikan
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Rentang x untuk plotting
x_plot = np.linspace(5, 40, 500)

# Interpolasi Lagrange
y_lagrange = [lagrange_interpolation(x_data, y_data, xp) for xp in x_plot]

# Plot hasil interpolasi
plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'ro', label='Titik Data')
plt.plot(x_plot, y_lagrange, 'b-', label='Interpolasi Lagrange')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Patah (s)')
plt.legend()
plt.title('Interpolasi Polinomial Lagrange')
plt.grid(True)
plt.show()