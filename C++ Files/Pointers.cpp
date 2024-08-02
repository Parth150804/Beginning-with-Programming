#include "bits/stdc++.h"

using namespace std;

//                 |---------> Different variable a 
void increment(int a) {     // inside func, value of variables are passed, not actually variables
    a++;
}


void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {

// int a = 10;
// int *aptr;
// aptr = &a;

// std::cout << &a << "\n";     // Memory address of a
// std::cout << aptr << "\n";   // -------""------------

// std::cout << *aptr << "\n";   // Value stored in a i.e. 10

// *aptr = 20;
// std::cout << a;   // Value of a changes to 20

// aptr++;
// std::cout << aptr << "\n";    //  Memory address increased by 4 bytes (as integer stores 4 byte of value)


// Pointers ans Arrays

// int arr[] = {10, 20, 30};           // Memory address of 20 will be 4 bytes ahead of 10 and so on.
// // std::cout << *arr << "\n";         // will print element at 0th index of arr[]
// int *ptr = arr;                       // arr is an indexing pointer, by default it points at 0th index.

// for (int i = 0; i < 3; i++) {
//     // std::cout << *ptr << "\n";
//     // ptr++;
//     // OR
//     std::cout << *(arr + i) << "\n";
// }


// Pointer to Pointer

// int a = 10;
// int *p;
// p = &a;

// std::cout << *p << '\n';    // 10

// int **q = &p;

// std::cout << *q << '\n';    // Memory address of a
// std::cout << **q << '\n';   // value of a

// Passing pointers to functions;

// int a = 2;

// increment(a);
// std::cout << a << '\n';        // 2

int a = 2;
int b = 4;

// swap(a, b);       // No swap will happen

// std::cout << a << " " << b;

// int *aptr = &a;
// int *bptr = &b;

// swap(aptr, bptr);       // Now, it is correct

// std::cout << a << " " << b;


}