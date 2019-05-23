import numpy as np
import matplotlib.pylab as plt

datos= np.genfromtxt("leapfrog.txt")

t=datos[:,0]
x=datos[:,1]
y=datos[:,2]

plt.figure()
plt.plot(t,y, 'c')
plt.title("Trayectoria x y de particula")
plt.xlabel("t(s)")
plt.ylabel("F")
plt.savefig("BelloAna_Final_15.pdf")