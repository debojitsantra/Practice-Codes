#include <stdio.h>
int check(int k)
{
	int b, h;
	int c = 1, m = 1, s = 0;
	h = k;
	dol
	{
		b = k % 10;
		k = k / 10;
		s = s + b;
		m = m * b;
	}
	while (k >= 1)
		;
	if (s == m)
	{
		printf("%d is a Spy Number \n", h);
	}
	else
	{
		printf("%d is not a Spy Number \n", h);
	}
}

int main()
{
	int a[100], n;
	printf("Enter The Number of Elements: ");
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		scanf("%d", &a[i]);
	}

	for (int j = 1; j <= n; j++)
	{
		check(a[j]);
	}
}