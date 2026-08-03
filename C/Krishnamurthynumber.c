#include <stdio.h>
int factorial(int n)
{
	int i, f = 1;
	for (i = 1; i <= n; i++)
	{
		f = f * i;
	}
	return f;
}
int main()
{
	int a[50], n, i, j, k, h, r, p ;
	printf("Enter The Number of elements: ");
	scanf("%d", &n);
	for (i = 0; i <n; i++)
	{
		printf("Enter %d th element: ",i+1);
		scanf("%d", &a[i]);
	}

	for (j = 0; j < n; j++)
	{
		h = a[j];
		p = 0;
		do
		{
			k = h % 10;
			p = p + factorial(k) ;
			h = h / 10;
		} while (h >= 1);
		if (a[j] == p)
		{
			printf("%d is a krisna murthy number", a[j]);
		}
	}
}
