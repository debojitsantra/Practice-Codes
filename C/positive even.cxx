#include <stdio.h> 
int main() {
	int a[100],n,i,j;
	printf("Enter the number of elements: ");
	scanf("%d",&n);
	for(i = 1; i<=n; i++)
	     scanf("%d",&a[i]);
	
	for(j = 1; j<=n; j++) {
		if ((a[j] > 0) && (a[j] % 2 == 0)){
			printf("   %d \n",a[j]);
		}
		
}
}