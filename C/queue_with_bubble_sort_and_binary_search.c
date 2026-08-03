#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

int data[MAX_SIZE];
int front = -1;
int rear = -1;

void swap(int *p, int *q) {
    int c;
    c = *p;
    *p = *q;
    *q = c;
}

void enqueue() {
    int item;
    if (rear == MAX_SIZE - 1) {
        printf("No Space Left\n");
        exit(0);
    } else {
        printf("Enter Data: ");
        scanf("%d", &item);
        if ((rear == -1) && (front == -1)) {
            front = 0;
        }
        rear++;
        data[rear] = item;
    }
}

void dequeue() {
    int item;
    if (front == -1) {
        printf("There is no data to delete\n");
    } else {
        item = data[front];
        if (front == rear) {
            rear = -1;
            front = -1;
        } else {
            front++;
        }
    }
}

void view() {
    printf("Viewing Data\n");
    printf("---------------------\n");
    for (int i = front; i <= rear; i++) {
        printf("%d\n", data[i]);
    }
    printf("---------------------\n");
}

void sort() {
    for (int i = 0; i <= rear; i++) {
        for (int j = i + 1; j <= rear; j++) {
            if (data[i] > data[j]) {
                swap(&data[i], &data[j]);
            }
        }
    }
}

void search() {
    int flag = 0, mid, k;
    int u = rear, l = front;
    printf("Enter Search Value: ");
    scanf("%d", &k);
    while (l <= u) {
        mid = (u + l) / 2;
        if (k == data[mid]) {
            printf("Present in the dataset");
            flag = 1;
            break;
        }
        if (k < data[mid]) {
            u = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    if (flag == 0) {
        printf("Not Found\n");
    }
}

int main() {
    int select;
    printf("---------------------\n");
    printf("Data Collection System\n");
    printf("---------------------\n");
    while (1) {
        printf("1. Enqueue\n2. Dequeue\n3. View\n4. Sort\n5. Search\n6. Exit\n");
        printf("---------------------\n");
        printf(">>> ");
        scanf("%d", &select);
        switch (select) {
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
                printf("Wrong Choice\n");
        }
    }
    return 0;
}