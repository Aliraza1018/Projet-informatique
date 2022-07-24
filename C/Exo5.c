// pour n = 12 , le programme affiche 479001600 
// pour n = 13 , le programme affiche 1932053504
// Le programme n'a pas juste car 13! = 6227020800
#include <stdlib.h>
#include <stdio.h>

int factorielle(int n);

int main(void){
  printf("Entrer un entier positif : ");
  int n;
  if (scanf("%d", &n) != 1){
    printf("Erreur de saisie");
    exit(EXIT_FAILURE);
  }
  
  int facto = factorielle(n);
  printf("%d! = %d", n, facto);
	return EXIT_SUCCESS;
}

int factorielle(int n){
  int somme = 1;
  for (int k = 1; k < n + 1; ++k){
    somme *= k;
  }
  return somme;
}
