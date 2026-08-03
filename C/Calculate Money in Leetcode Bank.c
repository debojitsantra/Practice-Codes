#include <stdio.h>

float totalMoney(int n)  {
    int week = n / 7;
    int left = n % 7;
    float arr[week + 2]; 
    float sum = 0, tsum = 0;

    if (n <= 7) {  
        sum = ((n / 2.0) * (n + 1));  
        arr[0] = sum;
        tsum = sum;
    } else {  
        sum = 28;  
        arr[0] = sum; 
        for (int i = 1; i < week; i++) {  
            sum = sum + 7;  
            arr[i] = sum;  
        }  
        if (left != 0) {  
            sum = ((left / 2.0) * (2 * week + 1 + left));  
            arr[week] = sum;   
        }

      
        int total_elements = week + (left != 0 ? 1 : 0);
        for (int i = 0; i < total_elements; i++) {
            tsum += arr[i];
        }
    }  



    return tsum;
}
