BelloAna_Final_15.pdf : grafica15.py
	python particula.py
leapfrog.txt : a.out
	./a.out
a.out : particula.cpp
	g++ particula.cpp