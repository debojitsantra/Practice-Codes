#include <stdio.h> 
int check(int k) {
	int i;
	if (k<=1)
	    return 0;
	    
	for (i = 2; i<k; i++) {
		if (k%i == 0) {
			   return 0;
		}
	}
		return 1;
	
}
int main() {
	int a[100],r,n,i,j;
	printf("Enter The Number of Elements: ");
	scanf("%d",&r);
	for (i = 0; i<r;i++){
		scanf("%d",&a[i]);
	}
	for (j=0; j<r;j++) {
		if (check(a[j])) {
			printf("%d is a prime number\n ",a[j]);
		} else {
			printf("%d is not a prime number\n",a[j]);
		} 
	}
}