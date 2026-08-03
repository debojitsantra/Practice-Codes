#include <stdio.h>
int main()
{
	int a[100], n, i, j, k, s,h;
	printf("Enter the number of elements: ");
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	for (j = 0; j < n; j++)
	{   s = 0;
		h = a[j];
		do
		{
			k = h % 10;
			s = (s * 10) + k;
			h = h / 10;

		} while (h > 0);
		if (a[j] == s)
		{
			printf("%d is a palindrome\n", a[j]);
		}
	}
}