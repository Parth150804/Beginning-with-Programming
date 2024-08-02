#include "bits/stdc++.h"

using namespace std;

// NOTE: To get size of array, use sizeof(arr)/sizeof(arr[0])

int linear_search(int arr[], int n, int key) {
        for (int i = 0; i < n; i++) {
            if (arr[i] == key) {
                return i;
            }
        }
        return -1;
    }

int binary_search(int arr[], int n, int key) {
    int low = 0;
    int high = n - 1;

    while (low <= high) {
        int mid = (low+high)/2;

        if (arr[mid] == key) {
            return mid;
        }
        else if (arr[mid] > key) {
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }
    }
    return -1;
}


int main() {

    // int array[4] = {10,20,30,40};
    // std::cout << array[0];

    int n;
    std::cin >> n;

    int arr[n];

    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }
    // }

    // int maxNo = INT_MIN;
    // int minNo =  INT_MAX;

    // for (int j = 0; j < n; j++) {
    //     maxNo = max(maxNo, arr[j]);
    //     minNo = min(minNo, arr[j]);
    // }

    // std::cout << maxNo << "\n" << minNo;
    
    int key;
    std::cin >> key;
    
    // std::cout << linear_search(arr, n, key);
    // std::cout << binary_search(arr, n, key);
    

}


