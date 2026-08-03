#include <stdio.h>
#include <stdlib.h>


struct Node {
    int data;
    struct Node* next;
};


struct Queue {
    struct Node* front;
    struct Node* rear;
};
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}
struct Queue* createQueue() {
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->front = queue->rear = NULL;
    return queue;
}

int isEmpty(struct Queue* queue) {
    return (queue->front == NULL);
}
void enqueue(struct Queue* queue, int data) {
    struct Node* newNode = createNode(data);
    struct Node *current, *prev;
    if (isEmpty(queue) || data < queue->front->data) {
        newNode->next = queue->front;
        queue->front = newNode;
        if (queue->rear == NULL) {
            queue->rear = newNode;
        }
        printf("Inserted %d\n", data);
        return;
    }
    
    current = queue->front;
    prev = NULL;
    while (current != NULL && current->data <= data) {
        prev = current;
        current = current->next;
    }
    prev->next = newNode;
    newNode->next = current;
   
    if (current == NULL) {
        queue->rear = newNode;
    }
    printf("Inserted %d\n", data);
}

int dequeue(struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("Queue Underflow! Cannot dequeue\n");
        return -1;
    }
    
    struct Node* temp = queue->front;
    int data = temp->data;
    queue->front = queue->front->next;
    
    if (queue->front == NULL) {
        queue->rear = NULL;
    }
    
    free(temp);
    return data;
}
void display(struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("Queue is empty\n");
        return;
    }
    
    printf("Queue contents (front to rear): ");
    struct Node* current = queue->front;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

void menu() {
    printf("\nQueue Operations Menu:\n");
    printf("1. Enqueue\n");
    printf("2. Dequeue\n");
    printf("3. Display\n");
    printf("4. Exit\n");
    printf("Enter your choice (1-4): ");
}

int main() {
    struct Queue* queue = createQueue();
    int choice, data;

    while (1) {
        menu();
        scanf("%d", &choice);

        switch (choice) {
            case 1:  
                printf("Enter value to insert: ");
                scanf("%d", &data);
                enqueue(queue, data);
                break;

            case 2:
                if (!isEmpty(queue)) {
                    printf("Dequeued element: %d\n", dequeue(queue));
                } else {
                    dequeue(queue);  
                }
                break;

            case 3: 
                display(queue);
                break;

            case 4: 
                printf("Exiting program...\n");
                while (!isEmpty(queue)) {
                    dequeue(queue);
                }
                free(queue);
                return 0;

            default:
                printf("Invalid choice! Please enter a number between 1 and 4\n");
        }
    }

    return 0;
}