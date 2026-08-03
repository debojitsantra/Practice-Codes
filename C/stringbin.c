#include <stdio.h>
#include <string.h>

int main() {
    int a, i = 0;
    char bin[65];

    printf("Enter Dec Num: ");
    scanf("%d", &a);

    do {
        bin[i++] = (a % 2) + '0'; 
        a = a / 2;
    } while (a > 0);

    bin[i] = '\0'; 

    strrev(bin); 
    printf("%s\n", bin);
    return 0;
}