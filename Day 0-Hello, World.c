#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
   char name[60];
   scanf("%[^\n]", &name);
   printf("Hello, World.\n");
   printf("%s",name);
   return 0;
