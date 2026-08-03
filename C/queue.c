#include <stdio.h>
#include <stdlib.h>
int data[100];
int front = -1;
int rear = -1;
int n = 100;
void swap(int *p, int *q)
{
	int c;
	c = *p;
	*p = *q;
	*q = c;
}
void enqueue()
{
	int item;
	if (rear == n)
	{
		printf("No Space Left");
		exit(0);
	}
	else
	{
		printf("Enter Data:");
		scanf("%d", &item);
		if ((rear == -1) && (front == -1))
		{
			front = 0;
		}
		rear = rear + 1;
		data[rear] = item;
	}
}
void dequeue()
{
	int item;
	if (front == -1)
	{
		printf("There is no data to delete");
	}
	else
	{
		item = data[front];
		if (front == rear)
		{
			rear = -1;
			front = -1;
		}
		else
		{
			front = front + 1;
		}
	}
}
void view()
{
	printf("Viewing Data \n");
	printf("--------------------- \n");
	for (int i = rear; i >= front; i--)
	{
		printf("%d \n", data[i]);
	}
	printf("--------------------- \n");
}
void sort()
{
	for (int i = 1; i <= rear - 1; i++)
	{
		for (int j = 1; i < rear - i; j++)
		{
			if (data[j] > data[j + 1])
			{
				swap(&data[j], &data[j + 1]);
			}
		}
	}
}
void search()
{
	int flag = 0, mid, k;
	int u = rear, l = front;
	if (data[l] > data[l + 1])
	{
		printf("Sort Before Search");
		exit(0);
	}
	printf("Enter Search Value:");
	scanf("%d", &k);
	while (flag != 1)
	{
		mid = (u + l) / 2;
		if (k == mid)
		{
			printf("Present in the dataset in the %d th position", mid);
			flag = 1;
		}
		if (k < data[mid])
		{
			u = mid - 1;
		}
		else
		{
			l = mid + 1;
		}
	}
	if (flag == 0)
	{
		printf("Not Found");
	}
}
int main()
{
	int select;
	
	printf("--------------------- \n");
	printf("Data Collection System \n");
	printf("--------------------- \n");
    system("clear");
	while (1)
	{
		printf("1. Enqueue \n2. Dequeue \n3. View \n4. Sort \n5. Search \n6. Exit\n");
		printf("--------------------- \n");
		printf(">>>");
		scanf("%d", &select);
		switch (select)
		{
		case 1:
			enqueue();
			break;
		case 2:
			dequeue();
			break;
		case 3:
			view();
			break;
		case 4:
			sort();
			break;
		case 5:
			search();
			break;
		case 6:
			exit(0);
		default:
			printf("Wrong Choice");
			break;
		}
	}
}