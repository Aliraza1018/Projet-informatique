#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

void moin_1_seconde(int *m, int *s);

int main(void){
  printf("Saisir un temp : ");
  int m, s;
  if (scanf("%d:%d", &m, &s) != 2){
    printf("Erreur de saisie");
    exit(EXIT_FAILURE);
  }
  
  while ( m != 0 || s != 0){
    printf("%02d:%02d\n", m, s);
    moin_1_seconde(&m, &s);
    sleep(1);
  }
  return EXIT_SUCCESS;
}

void moin_1_seconde(int *m, int *s){
  if (*s == 00){
    *s = 59;
    *m -= 1;
  } else{
    *s -= 1;
  }
}
