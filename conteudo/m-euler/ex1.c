#include <stdio.h>

float f(float x){
	return 2*x;
}

float g(float x){
	return x*x;
}

int main () {
	float cont, i, aux, atual, prox, ant,x0;

	printf("Metodo de Euler pra aproximar os roles\n");
	printf("Ponto     -----     Valor real    ----    Valor aprox\n");
	cont = 0;
	ant = x0 = 0;
	for(i=0;i<100;i++) {
		atual = ant + 0.1 * f(x0);
		if(cont == 10) {
			printf("%.3f     -----     %.3f    ---    %.3f\n",x0,g(x0),atual);
			cont = 0;
		}
		else cont ++;
		ant = atual;
		x0 += 0.1;
	}
	
	return 0;
}
