#include<iostream>
#include<cstring>
#include <fstream>

using namespace std;

float m= 7294.29;
int q=2;
float t=0;
float tfinal= 1000;
float dt=0.1;

float f(float t, float t_final);
float void a(float m, float t, float tfinal);
void leapfrog(float t, float t_final, float dt, string name );

int main(){

	leapfrog(t,tfinal,dt, "leapfrog.txt")

	return 0;
}

// mdv/dt = m vn+1 -vn /dt http://www.sc.ehu.es/sbweb/fisica/elecmagnet/movimiento/cicloide/cicloide.htm
float F(float t, float t_final)
{
	return m*a(m ,t , tfinal)	
}


void a(float m, float t, float tfinal){
	float E;
		if( i < 3)
		{
			E=3;
		}
		elif(i<3)
		{
			E=0;
		}

		elif(i>7)
		{
			E=0;
		}

	return (q*E)/m;
}

void leapfrog(float t, float t_final, float dt, string name ){

	ofstream outfile;
	outfile.open()

	float t= 0;
	float t_final= t_final;
	float y=0;
	float x=0;

	while(t < t_final)

	outfile << t  << "\t" << x << "\t" << y << "\t" << endl;
	y = y + (1/2)*dt*F(m,,t,tfinal);
	x= x + (1/2)*dt*F(m,,t,tfinal);
	z= z+ dt*F(m,,t,tfinal);	 
	t= t + dt;

	outfile.close()
}