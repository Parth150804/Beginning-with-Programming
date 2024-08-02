#include "bits/stdc++.h"

using namespace std;
// Use of new keyword
// NOTE: int a = 4;
//       int* ptr = &a;
// is same as
//       int* p = new int(4);

// Use of delete keyword
// int* arr = new int[3];
// arr[0] = 10;
// arr[1] or *(arr+1) = 20;
// arr[2] = 30;
// Now, to delete the entire array, we use - delete[] arr



bool sorted_arr(int arr[], int n, int p = 0, int q = 1) {
    if ((n == 1) or (p == n - 2 && q == n - 1 && arr[p] <= arr[q])) {
        return true;
    }
    else {
        if (arr[p] > arr[q]) {
            return false;
        }
        else {
            return sorted_arr(arr, n, p + 1, q + 1);
        }
    }

}

int firstocc(int arr[], int n, int target, int ans = 0) {
    if (arr[ans] == target) {
        return ans;
    }
    else {
        return firstocc(arr, n, target, ans + 1);
    }
}

int lastocc(int arr[], int n, int target, int ans = -1, int p = 0) {       
    if (p == n - 1 and arr[p] != target) {
        return ans;
    }
    else if (p == n - 1 and arr[p] == target) {
        return p;
    }
    else {
        if (arr[p] == target) {
            return lastocc(arr, n, target, p, p + 1);
        }
        else {
            return lastocc(arr, n, target, ans, p + 1);
        }
    }
}

// int lastocc(int arr[], int n, int i, int key) {             // Remember, arguments with default value should be at the end   
//     if (i == n) {                                           // This is code in lecture video
//         return -1;
//     }

//     int restArray = lastocc(arr, n, i+1, key);

//     if (restArray != -1) {
//         return restArray;
//     }
//     if (arr[i] == key) {
//         return i;
//     }
//     return -1;
// }

string rev_string(string s) {
    if (s.size() == 0) {
        return s;
    }
    else {
        return rev_string(s.substr(1)) + s[0];
    }

}

void replacePi(string s) {
    if (s.length() == 0) {
        return;
    }
    if (s[0] == 'p' and s[1] == 'i') {
        std::cout << "3.14";
        replacePi(s.substr(2));
    }
    else {
        std::cout << s[0];
        replacePi(s.substr(1));
    }
}

void towerofHanoi(int n, char src, char dest, char helper) {        // Dest tower is the one in which disks have to be inserted
                                                        
    if( n == 0) {                                                   //     src      helper     dest
        return;         // base case                                //      --
    }                                                               //     ----
        // firstly put n-1 disks to helper tower                    //    ------
    towerofHanoi(n - 1, src, helper, dest);                         //   --------
    //  now move the last remaining disk from src to dest tower

    std::cout << "Move from " << src << " to " << dest << "\n";
    // then call the func recursively with helper being src, dest being helper & src being dest so that problem can be started with n-1 on src tower

    towerofHanoi(n - 1, helper, dest, src);
}


string removeDup(string s) {            // <----- The code is valid when duplicates appear adjacent to each other
    if (s.length() == 0) {
        return "";
    }

    char ch = s[0];
    string ans = removeDup(s.substr(1));
    if (ch == ans[0]) {
    return ans;
    }
    else {
        return ch + ans;
    }

}

string better_removeDup(string s) {             // <------- this is an improved version
    if (s.size() == 0) {
        return "";
    }
    else {
        char ch = s[0];
        string ros = better_removeDup(s.substr(1));
        int val = ros.find(ch);
        if (val < ros.size()) {
            return ros;
        }
        else {
            return ch + ros;
        }
    }
}


string moveallx(string s) {
    if (s.length() == 0) {
        return "";
    }

    char ch = s[0];
    string ans = moveallx(s.substr(1));
    if (ch == 'x') {
        return ans + ch;
    }
    else {
        return ch + ans;
    }
}

void allsubstr(string s, string ans = "") {                     // Basically, kind of subsets of that string
    if(s.length() == 0) {
        std::cout << ans << "\n";
        return;
    }

    char ch = s[0];
    string ros = s.substr(1);

    allsubstr(ros, ans);
    allsubstr(ros, ans + ch);
}

void allsubstrwithASCII(string s, string ans = "") {
    if(s.length() == 0) {
        std::cout << ans << "\n";
        return;
    }

    char ch = s[0];
    int code = ch;          // <----------- This will give ASCII code
    string ros = s.substr(1);

    allsubstrwithASCII(ros, ans);           // These two will generate 
    allsubstrwithASCII(ros, ans + ch);      // normal substrings
    allsubstrwithASCII(ros, ans + to_string(code));         // This will create substrings with ASCII value
    
}

string keypadArr[] = {"", "./", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

void keypad(string s, string ans = "") {      //------> Will give combination of letter corr. to each number in the number which is given as input
    if (s.length() == 0) {
        std::cout << ans << "\n";
        return; 
    }

    char ch = s[0];
    string code = keypadArr[ch - '0'];      // if we typecast ch into int, then it will return it's ASCII value (ASCII value of 1 is 49)
    string ros = s.substr(1);               // so to get that no. we should take difference b/w ASCII values of that number and zero, which is what done here

    for (int i = 0; i < code.length(); i++) {
        keypad(ros, ans + code[i]);
    }
}

void permutations(string s, string ans = "") {          // Valid when string have no duplicate characters
    if (s.length() == 0) {
        std::cout << ans << "\n";
        return;
    }
    else {
        for(int i = 0; i < s.length(); i++) {                  // This logic is nice
            char ch = s[i];
            string ros = s.substr(0, i) + s.substr(i+1);

            permutations(ros, ans + ch);
        }
    }
}

int countPath(int s, int e) {           // No. of paths possible on a linear board game, e.g    0  1  2  3  4
    if (s >= e) {                       // a dice is thrown and player is moved acc. to no. appeared on it
        return 0;
    }
    int count  = 1;
    for (int i = 1; i <= 6; i++) {
        count += countPath(s+i, e);
    }
    return count;
}


int no_of_paths(int n, int i = 0, int j = 0) {       // Given a grid of size nxn with index starting from 0 to n-1
                                                     // // we have to calculate number of paths to reach (n-1, n-1) from any starting point, by default (0, 0)
    if (i == n - 1 and j == n - 1) {                
        return 1;
    }
    if (i >= n or j >= n) {
        return 0;
    }

    return no_of_paths(n, i + 1, j) + no_of_paths(n, i, j + 1);      // either we move downward or forward
}

int tiling_ways(int n) {        // this code is for problem when board is of size 2xn and tile is of size 2x1
    if (n == 0 or n == 1) {
        return n;
    }

    return tiling_ways(n-1) + tiling_ways(n-2);
}

int friends_pairing(int n) {                // Any friend can be paired up or left single
    if (n == 1 or n == 0 or n == 2) {
        return n;
    }
    else {
        return friends_pairing(n-1) + (n-1)*friends_pairing(n-2);
    }
}

int knapsack(int value[], int wt[], int n, int W) {
    if (n == 0 || W == 0) {
        return 0;
    }
    if (wt[n-1] > W) {
        return knapsack(value, wt, n-1, W);
    }

    return max(knapsack(value, wt, n-1, W-wt[n-1])+value[n-1], knapsack(value, wt, n-1, W));
}


// Backtracking

// int** arr[] denotes it is a 2D array
// Here we assume maze to be a square matrix (nxn)

bool isSafe(int** arr, int x, int y, int n) {
    if (x < n && y < n && arr[x][y] == 1) {
        return true;
    }
    return false;
}

// solArr will be initialized with all entries zero

bool rat_in_Maze(int** arr, int x, int y, int n, int** solArr) {

    if (x == n-1 and y == n-1) {
        solArr[x][y] = 1;
        return true;
    }
    if (isSafe(arr, x, y, n)) {
        solArr[x][y] = 1;
        if (rat_in_Maze(arr, x+1, y, n, solArr)) {
            return true;
        }
        if (rat_in_Maze(arr, x, y+1, n, solArr)) {
            return true;
    }
    solArr[x][y] = 0;
    return false;
    }
    return false;
}


// Permutations

                                            // 2D array which will store permuted arrays
void permute(vector<int> &a, vector<vector<int>> &ans, int idx = 0) {
    if(idx == a.size()) {
        ans.push_back(a);
        return;
    }
    for (int i = idx; i < a.size(); i++) {
        if(i != idx and a[i] == a[idx]) {
            continue;
        }
        swap(a[i], a[idx]);
        permute(a, ans, idx+1);
        swap(a[i], a[idx]);

    }
    return;
}


// N - Queen Problem

bool IsSafe(int** arr, int x, int y, int n) {
    for(int row = 0; row<x; row++) {
        if(arr[row][y] == 1) {
            return false;
        }
    }

    int row = x;
    int col = y;
    while (row >= 0 and col >= 0) {
        if(arr[row][col] == 1) {
            return false;
        }
        row--;
        col--;
    }

    row = x;
    col = y;
    while(row >= 0 and col < n) {
        if(arr[row][col] == 1) {
            return false;
        }
        row--;
        col++;
    }

    return true;
}

bool nQueen(int** arr, int x, int n) {
    if(x >= n) {
        return true;
    }

    for(int col = 0; col < n; col++) {
        if(IsSafe(arr, x, col, n)) {
            arr[x][col] = 1;

        if(nQueen(arr, x+1, n)) {
            return true;
        }

        arr[x][col] = 0;      //backtracking

        }

    }
return false;

}

void combinations(vector<int> &arr, int targ, vector<vector<int>> &ans, vector<int> &v, int idx = 0) {
    if (idx == arr.size()) {
        if (targ == 0) {
            ans.push_back(v);
            return;
        }
    }
    else {
        for (int i = idx; i < arr.size(); i++) {
            if (targ >= arr[i]) {
                v.push_back(arr[i]);
                combinations(arr, targ-arr[i], ans, v, i+1);
                v.pop_back();
            }
            combinations(arr, targ, ans, v, i+1);
        }
    }
}

vector<vector<int>> howSum(vector<int> &arr, int targ) {
    vector<int> v;
    vector<vector<int>> ans;
    combinations(arr, targ, ans, v);
    return ans;
}

int main() {

// int arr[5] = {1, 3, 4, 5, 6};
// std::cout << sorted_arr(arr, 5);

// int arr[6] = {1, 2, 3, 4, 2, 2};
// std::cout << lastocc(arr, 6, 2);

// std::cout << rev_string("Parth");

// string str = "pippxxppiixipi";
// replacePi(str);

// towerofHanoi(3, 'S', 'D', 'H');

// std::cout << better_removeDup("abac");

// std::cout << moveallx("jsalgdxasjxxjhsaxbjaxxxjhsbxsxl");


// allsubstr("ABC");

// allsubstrwithASCII("AB");

// keypad("23");

// permutations("ABC");

// std::cout << countPath(0, 3);

// std::cout << no_of_paths(3);

// std::cout << tiling_ways(4) << "\n";
// std::cout << friends_pairing(4);

// int wt[] = {10, 20, 30};
// int value[] = {100, 50, 150};
// int W = 50;

// std::cout << knapsack(value, wt, 3, W);

// Backtracking

// // 1 0 1 0 1
// // 1 1 1 1 1
// // 0 1 0 1 0
// // 1 0 0 1 1
// // 1 1 1 0 1

// int n;
// std::cin >> n;

// int** arr = new int*[n];        // to declare 1D dynamic array, we use single pointer int* arr = new int[n];
// for (int i = 0; i < n; i++) {   // Similarly to declare 2D dynamic array we use double pointer int** arr = new int*[n];
//     arr[i] = new int[n];        // int** arr is double pointer as 2D array is array of arrays, instead of int we use int*[n];
// }                            // arr[i] = new int[n] means creating empty arrays of size n inside array arr of size n.

// for (int i = 0; i < n; i++) {
//     for (int j = 0; j < n; j++) {
//         std::cin >> arr[i][j];
//     }
// }

// int** solArr = new int*[n];
// for (int i = 0; i < n; i++) {
//     solArr[i] = new int [n];
//     for (int j = 0; j < n; j++) {
//         solArr[i][j] = 0;           // Initially solArr will have all entries zero
//     }
// }

// std::cout << "\n";

// if (rat_in_Maze(arr, 0, 0, n, solArr)) {
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < n; j++) {
//             std::cout << solArr[i][j] << " ";
//         }
//     std::cout << "\n";
// }
// }


// Permutations   (Time complexity = O(n!))

// int n;
// std::cin >> n;
// vector<int> a(n);

// for (auto &i : a) {
//     std::cin >> i;
// }

// std::cout << "\n";

// vector<vector<int>> ans;
// permute(a, ans);      // This is defined function(input is array and index from where permutations should be started)

// sort(a.begin(), a.end());
// do {
//     ans.push_back(a);
// } while(next_permutation(a.begin(), a.end()));    // -----> Inbuilt Function

// for(auto v : ans) {                 // ans array is the one which contains possibles arrangements of array
//     for(auto i : v) {
//         std::cout << i << " ";
//     }
//     std::cout << "\n";
// }

// // N - Queen Problem

// int n;
// std::cin >> n;

// int** arr = new int*[n];
// for(int i = 0; i < n; i++) {
//     arr[i] = new int[n];
//     for(int j = 0; j < n; j++) {
//         arr[i][j] = 0;
//     }
// }


// if(nQueen(arr, 0, n)) {
//     for(int i = 0; i < n; i++) {
//         for(int j = 0; j < n; j++) {
//             std::cout << arr[i][j] << " ";
//         }
//     std::cout << "\n";
// }

// }

    // vector<int> arr = {2,4,3,5,1};
    // int targ = 7;
    // vector<vector<int>> ans = howSum(arr, targ);
    // for (auto ele: ans) {
    //     for (int val: ele) {
    //         std::cout << val << " ";
    //     }
    //     std::cout << "\n";
    // }
}