import numpy as np
import matplotlib.pylab as plt




def MH():
	probables=[]
	incertidumbre= np.random.random()*2-1
	probables.append(incertidumbre)

	for i in range(N):

		i2=np.random.normal(caminata[i],sigma)
		alpha=MB(T,m,v1)/MB(T,m,caminata[i])

		if(alpha>=1):
			incertidumbre.append(i2)

		else: 
			beta=np.random.random()

			if(beta<=alpha):
				probables.append(i2)

			else:
				probables.append(probables[i])
	return probables
