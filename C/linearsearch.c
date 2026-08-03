#include <stdio.h>

int linearSearch(int arr[], int size, int key) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == key) {
            return i;  
        }
    }
    return -1; 
}

int main() {
    int arr[] = {10, 20, 80, 30, 60, 50, 110, 100};
    int size = sizeof(arr) / sizeof(arr[0]);
    int key;
    
    printf("Enter element to search: ");
    scanf("%d", &key);
    int result = linearSearch(arr, size, key);
    if (result == -1) {
        printf("Element %d not found\n", key);
    } else {
        printf("Element %d found at index %d\n", key, result);
    }

    return 0;
}