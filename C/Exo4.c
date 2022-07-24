#include <stdlib.h>
#include <stdio.h>

int somme_pair(int n);

int main(void){
  printf("Entrer un entier positif : ");
  int n;
  if (scanf("%d", &n) != 1){
    printf("Erreur de saisie");
    exit(EXIT_FAILURE);
  }
  
  int somme = somme_pair(n);
  printf("La somme des entiers positif pairs situer entre 2");
  printf(" et %d est %d", n, somme);
	return EXIT_SUCCESS;
}

int somme_pair(int n){
  int resulta = 0;
  int z = 2;
  while (z <= n){
    resulta += z;
    z = z + 2;
  }
  return resulta;
}
