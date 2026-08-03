#include <stdio.h>
int main()
{
	int a[100], n, i, j, max, min;
	printf("Enter the number of elements: ");
	scanf("%d", &n);
	for (i = 0; i < n; i++)
		scanf("%d", &a[i]);
	max = a[0];
	min = a[0];
	for (j = 0; j < n; j++)
	{
		if (max < a[j])
		{
			max = a[j];
		}
		if (min > a[j])
		{
			min = a[j];
		}
	}
	printf("Max is %d & Min is %d", max, min);
}