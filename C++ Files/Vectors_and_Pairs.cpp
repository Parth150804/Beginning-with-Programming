#include "bits/stdc++.h"

using namespace std;

bool myCompare(pair<int, int> p1, pair<int, int> p2) {
    return p1.first < p2.first;
}
int main() {

// Vector


vector<int> v;
// to append elements use .push_back()
// v.push_back(2);
// std::variant<int, char, float> v; is used to store different data types in a single vector (available in C++17 and higher)


// Printing a vector

for(int i = 0; i < v.size(); i++) {
    std::cout << v[i] << " ";
}


// Another way

vector<int>::iterator it;
for(it = v.begin(); it != v.end(); it++) {
    std::cout << *it << " ";
}

// Another way

for(auto element : v) {         
    std::cout << element << " ";
}

v.pop_back();       // end element will get removed

vector<int> v2 (3, 50);      // size of vector, value of all elements
// 50 50 50

// Exchanging elements of two vectors
swap(v, v2);

sort(v.begin(), v.end());




// Pairs

pair<int, char> p;

p.first = 3;
p.second = 'f';

// Ques: we have to reduce the array (i.e we have to put 0 at the place of smallest element, 1 at an element which 2nd smallest and so on without changing order of elements)
// (import. ques)

int arr[] = {10, 16, 7, 14, 5, 3, 2, 9};
// 5 7 3 6 2 1 0 4

vector <pair<int, int>> v1;

for (int i = 0; i < (sizeof(arr)/sizeof(arr[0])); i++) {

// pair<int, int> p;
// p.first = arr[i];
// p.second = i;

// Shortcut
        v1.push_back(make_pair(arr[i], i));

}

sort(v1.begin(), v1.end(), myCompare);      

for(int i = 0; i < v1.size(); i++) {        // Very good logic
    arr[v1[i].second] = i;                  // see and understand this carefully
}

for (int i = 0; i < v1.size(); i++) {
    std::cout << arr[i] << " ";
}

}