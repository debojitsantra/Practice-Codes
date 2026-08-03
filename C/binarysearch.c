#include <stdio.h>

int binarySearch(int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2; 
        if (arr[mid] == target)
            return mid;
        if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}

int main() {
    int target;
    int arr[] = {2, 3, 4, 5, 6, 10, 20, 70}; //predefined array
    int size = sizeof(arr) / sizeof(arr[0]);
    printf("Enter search value: ");
    scanf("%d",&target);
    
    int result = binarySearch(arr, size, target);
    
    if (result == -1)
        printf("Element not present");
    else
        printf("Element found at index %d", result);
    
    return 0;
}