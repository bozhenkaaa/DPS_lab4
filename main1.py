import numpy as np
import matplotlib.pyplot as plt

def linear_field(X, Y):
    U = -Y
    V = X
    return U, V

# Сітка
x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)
U, V = linear_field(X, Y)

plt.figure(figsize=(6,6))
plt.streamplot(X, Y, U, V, color='blue')
plt.scatter(0, 0, color='red', s=80, label='Equilibrium (0,0)')
plt.title("Linear System: Center")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axis('equal')
plt.show()



def homogeneous_field(X, Y):
    U = X**2 - Y**2
    V = 2*X*Y
    return U, V

x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
U, V = homogeneous_field(X, Y)

plt.figure(figsize=(6,6))
plt.streamplot(X, Y, U, V, color='green')
plt.scatter(0, 0, color='red', s=80, label='Equilibrium (0,0)')
plt.title("Homogeneous System: Rays")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axis('equal')
plt.show()