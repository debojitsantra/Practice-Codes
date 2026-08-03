#include <stdio.h>

int leap()
{
    int a;
    printf("\nEnter the number:");
    scanf("%d",&a);
    if ((a %4 == 0) && (a%5!=0 )) {
        printf("The Number is Divisible by 4 but not by 5");
    }
    else if (a % 5 == 0) {
        printf("The Number is divisible by 5");
    }
    else if (a%4 == 0) {
        printf("The number is divisible by 4");
         }
        
    else if((a%4 == 0)&&(a %5 == 0)) {
        printf("The number is divisible by both 4 & 5");
    }
    else {
        printf("The number is neither divisible by 4 nor 5");
    }
   
}

int main() {
    while (i!=0)
	 {
		leap();
		
		}
    
    
}