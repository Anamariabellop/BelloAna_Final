import numpy as np
import matplotlib.pylab as plt

datos= np.genfromtxt("leapfrog.txt")

t=datos[:,0]
x=datos[:,1]
y=datos[:,2]

plt.figure()
plt.plot(x,y, 'c')
plt.title("Trayectoria x y de particula")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("BelloAna_Final_15.pdf")