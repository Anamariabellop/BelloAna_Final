import numpy as np
import matplotlib.pylab as plt


t= np.linspace(0,100000)

def proyectilx(t):
	return v_0*np.cos(a)*t

def proyectily(t):
	return v_0*np.sen(a)*t - ((g*(t**2))/2)

def derivproyectil():
	return v_0*np.sen(a) - (g*t)


def MH(t):
	probables=[]
	incertidumbre= np.random.random()*2-1
	probables.append(incertidumbre)

	for i in range(N):

		i2=np.random.normal(caminata[i],sigma)
		alpha=proyectily(t)/derivproyectil(t)

		if(alpha>=1):
			incertidumbre.append(i2)

		else: 
			beta=np.random.random()

			if(beta<=alpha):
				probables.append(i2)

			else:
				probables.append(probables[i])
	return probables
