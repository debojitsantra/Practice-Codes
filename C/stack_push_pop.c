#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
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

int isEmpty(struct Node* top) {
    return (top == NULL);
}

void push(struct Node** top, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = *top;
    *top = newNode;
    printf("Pushed %d to stack\n", data);
}

int pop(struct Node** top) {
    if (isEmpty(*top)) {
        printf("Stack Underflow! Cannot pop from empty stack\n");
        return -1;
    }
    struct Node* temp = *top;
    int poppedData = temp->data;
    *top = (*top)->next;
    free(temp);
    return poppedData;
}

void display(struct Node* top) {
    if (isEmpty(top)) {
        printf("Stack is empty\n");
        return;
    }
    printf("Stack contents (top to bottom): ");
    struct Node* current = top;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

void menu() {
    printf("\nStack Operations Menu:\n");
    printf("1. Push\n");
    printf("2. Pop\n");
    printf("3. Display\n");
    printf("4. Exit\n");
    printf("Enter your choice (1-4): ");
}

int main() {
    struct Node* top = NULL;  
    int choice, data;
    while (1) {
        menu();
        scanf("%d", &choice);
        switch (choice) {
            case 1:  
                printf("Enter value to push: ");
                scanf("%d", &data);
                push(&top, data);
                break;
            case 2:  
                if (!isEmpty(top)) {
                    printf("Popped element: %d\n", pop(&top));
                } else {
                    pop(&top); 
                }
                break;
            case 3:  
                display(top);
                break;

            case 4: 
                printf("Exiting program...\n");
           
                while (!isEmpty(top)) {
                    pop(&top);
                }
                return 0;
            default:
                printf("Invalid choice! Please enter a number between 1 and 4\n");
        }
    }
    return 0;
}