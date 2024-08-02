#include "bits/stdc++.h"

using namespace std;

void merge(int arr[], int l, int mid, int r) {      // This merge func splits the list by itself, stores those splited lists
    int n1 = mid - l + 1;                           // in two lists a & b of appropriate size
    int n2 = r - mid;

    int a[n1];
    int b[n2];   // temp arrays

    for (int i = 0; i < n1; i++) {          // Storing values of first half elements of array in a
        a[i] = arr[l+i];
    }
    for (int i = 0; i < n2; i++) {          // Storing values of second half elements of array in b
        b[i] = arr[mid+1+i];
    }

    int i = 0;
    int j = 0;
    int k = l;      // to traverse original array
    while(i < n1 and j < n2) {
        if (a[i] < b[j]) {
            arr[k] = a[i];
            k++;
            i++;
        }
        else {
            arr[k] = b[j];
            k++;
            j++;
        }
    }

    // If any one of i or j crosses their respective upper bounds, then these while loops will continue the 
    // traversing of other remaining list 

    // NOTE: these two while loops are the reason why this func only merges two sorted list to give overall sorted list.
    // Because these while loops directly then add the remaining elements to the original array without comparing them with anyone.

    while(i < n1) {
        arr[k] = a[i];
        k++; i++;
    }

    while ( j < n2) {
        arr[k] = b[j];
        k++; j++;
    }
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int mid = (l+r)/2;          // This makes the size of array each time half
        mergeSort(arr, l, mid);
        mergeSort(arr, mid+1, r);

        merge(arr, l, mid, r);
    }
}
//                                                         _   _
// Timings Analysis (No. of splitting levels would be k = |log n|)
// Recurrance relation : T(n) = 2T(n/2) + n;
// T(n) = 2T(n/2) + n       
// T(n/2) = 2T(n/4) + n/2
// T(n/4) = 2T(n/8) + n/4
// ....
// (Add these eqns by multiplying each eqn after 2nd eqn by 2, it becomes telescopic sum)
// T(n) = n log n   ("in every case")

int partition(int arr[], int l, int r) {
    int pivot = arr[r];
    int i = l-1;

    for(int j = l; j < r; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i+1], arr[r]); 
    return i+1;                 // returns the index at which pivot is there
}

void quickSort(int arr[], int l, int r) {
    if (l < r) {

        int pi = partition(arr, l, r);
        quickSort(arr, l, pi-1);
        quickSort(arr, pi+1, r);
    }
}

// Timing Analysis
// In best case, pivot would be median element.
// In worst case, pivot would be end element.
// T(n) = n log n (Avg. case) & n^2 in worst case

void countSort(int arr[], int n) {
    int k = arr[0];
    for(int i = 0; i < n; i++) {
        k = max(k, arr[i]);
    }

    int count[k+1] = {0};
    for(int i = 0; i < n; i++) {
        count[arr[i]]++;
    }

    for (int i = 0; i < k; i++) {
        count[i+1] += count[i];
    }

    int output[n];
    for(int i = n-1; i >= 0; i--) {
        output[--count[arr[i]]] = arr[i];
    }

    for(int i = 0; i < n; i++) {
        arr[i] = output[i];
    }

}


// Timing Analysis
// 1. First we create an array of appropriate range, O(max(A_i));
// 2. Fill the frequencies of each element, O(N);
// 3. Iterate the frequency array, O(max(A_i));

// Final time complexity = O(max(A_i, N))


void dnfSort(int arr[], int n) {

    int low = 0;
    int mid = 0;
    int high = n-1;

    while(mid <= high) {
        if (arr[mid] == 0) {
            swap(arr[low], arr[mid]);
            low++;
            mid++;
        }
        else if (arr[mid] == 1) {
            mid++;
        }
        else {
            swap(arr[high], arr[mid]);
            high--;
        }
    }
}

// Timing Analysis
// In each iteration, mid gets incremented or high gets decremented
// T.C will be O(n);


void waveSort(int arr[], int n) {         // This sorting technique is used to sort array in a wave form
    for(int i = 1; i < n; i += 2) {       // arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4].........
        if(arr[i] > arr[i-1]) {
            swap(arr[i], arr[i-1]);
        }
        if(arr[i] > arr[i+1] and i <= n-2) {
            swap(arr[i], arr[i+1]);
        }
    }
}

// Time Complexity = O(n)


// Count Inversion (No. of pairs such that arr[i] > arr[j] & i < j) using the logic of merge sort
// Inefficient Approach (Brute force): Using two nested loops, O(n^2)

long long merge2(int arr[], int l, int mid, int r) {
    long long inv = 0;
    int n1 = mid-l+1;
    int n2 = r - mid;
    int a[n1];
    int b[n2];
    for(int i = 0; i < n1; i++) {
        a[i] = arr[l+i];
    }
    for(int i = 0; i < n2; i++) {
        b[i] = arr[mid+i+1];
    }
    int i = 0, j = 0, k = l;
    while(i < n1 and j < n2) {
        if(a[i] <= b[j]) {
            arr[k] = a[i];
            k++;
            i++;
        }
        else {
            arr[k] = b[j];
            inv += n1 - i;  // Important
            // a[i] > b[j] and  i < j
            k++;
            j++;
        }
    }

    while (i < n1) {
        arr[k] = a[i];
        k++;
        i++;
    }
    while(j < n2) {
    arr[k] = b[j];
    k++;
    j++;
}

return inv;

}

long long count_inversions(int arr[], int l, int r) {
    long long inv = 0;
    if(l < r) {
        int mid = (l+r)/2;
        inv += count_inversions(arr, l, mid);
        inv += count_inversions(arr, mid+1, r);
        inv += merge2(arr, l, mid, r);
    }

    return inv;

}



int main() {
    // int n;
    // std::cin >> n;

    // int arr[n];

    // for (int i = 0; i < n; i++) {
    //     std::cin >> arr[i];
    // }

    // Selection sort (find the min element in the unsorted array and swap it with element at beginning)  T(n) = O(n^2)
    // for (int i = 0; i < n - 1; i++) {
    //     for (int j = i; j < n; j++) {
    //         if (arr[j] < arr [i]) {
    //             int temp = arr[i];
    //             arr[i] = arr[j];
    //             arr[j] = temp;

    //         }
    //     }
    // }

    // Bubble sort (Repeatedly swap two adjacent elements if they are swap in wrong order)  T(n) = O(n^2)
    // for (int i = n; i > 0; i--) {
    //     for (int j = 0; j < i; j++) {
    //         if (arr[j] > arr[j + 1]) {
    //             int temp = arr[j];
    //             arr[j] = arr[j + 1];
    //             arr[j + 1] = temp;
    //         }
    //     }
    // }

    // Insertion Sort (insert an element from unsorted array to its correct position in sorted array)  T(n) = O(n^2)
    // for (int i = 1; i < n; i++) {
    //     int j = 0;
    //     while ( j < i) {
    //         if (arr[j] > arr[i]) {
    //             int temp = arr[i];
    //             arr[i] = arr[j];
    //             arr[j] = temp;
    //             j = j + 1;
    //         }
    //         else {
    //             j = j + 1;
    //         }
    //     }
    // } 


    // for (int i = 0; i < n; i++) {
    //     std::cout << arr[i] << " ";
    // }

    // int arr[] = {5, 4, 3, 2, 1};
    // // mergeSort(arr, 0, 4);  
    // quickSort(arr, 0, 4);
    // for(int i = 0; i < 5; i++) {
    //     std::cout << arr[i] << " ";
    // }
    // std::cout << "\n";


// int arr[] = {5, 4, 9, 1, 0, 8, 2, 2, 3};

// countSort(arr, 9);

// for (int i = 0; i < 9; i++) {
//     std::cout << arr[i] << " ";
// }

// DNF Sort (used to combine elements of one kind together if three kinds of elements are present in an array, here 0, 1 & 2)
// check value of arr[mid] - 
//      if 0, swap(arr[low], arr[mid]); low++; mid++;
//      if 1; mid++;
//      if 2; swap(arr[high], arr[mid]); high--


// int arr[] = {1, 0, 2, 1, 0, 1, 2, 1, 2};
// dnfSort(arr, 9);

// for(int i = 0; i < 9; i++) {
//     std::cout << arr[i] << " ";
// }

// int arr[] = {1, 3, 4, 7, 5, 6, 2};
// waveSort(arr, 7);

// for(int i = 0; i < 7; i++) {
//     std::cout << arr[i] << " ";
// }


int n;
std::cin >> n;
int arr[n];
for(int i = 0; i < n; i++) {
    std::cin >> arr[i];
}

std::cout << count_inversions(arr, 0, n-1);



}