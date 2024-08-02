#include "bits/stdc++.h"
using namespace std;

int main() {

// Creating the matrix of dim nxm
int n,m; 
std::cin >> n >> m;
int arr[n][m];

for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        std::cin >> arr[i][j];
    }
}

for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        std::cout << arr[i][j] << " ";
    }
    std::cout << "\n";
}

// Spiral Order Traversal ( 4 variables will be used)
//         -------->
// e.g   ^ 1  20  7  |
//       | 20  3  5  |
//       | 8  19  20 |
//         <-------- v
// Code:
// Our Matrix will be   1  5  7  9  10 11
//                      6  10 12 13 20 21
//                      9  25 29 30 32 41
//                      15 55 59 63 68 70
//                      40 70 79 81 95 105

int row_start = 0, row_end = n-1, column_start = 0, column_end = m-1;

while (row_start <= row_end && column_start <= column_end) {
    // for row_start
    for(int col = column_start; col <= column_end; col++) {
        std::cout << arr[row_start][col] << " ";
    }
    row_start++;

    // for column_end
    for(int row = row_start; row <= row_end; row++) {
        std::cout << arr[row][column_end] << " ";
    }
    column_end--;

    // for row_end
    for(int col = column_end; col >= column_start; col--) {
        std::cout << arr[row_end][col] << " ";
    }
    row_end--;

    // for column_start
    for(int row = row_end; row >= row_start; row--) {
        std::cout << arr[row][column_start] << " ";
    }
    column_start++;
}

// Output: 1 5 7 9 10 11 21 41 70 105 95 81 79 70 40 15 9 6 10 12 13 20 32 68 63 59 55 25 29 30 29

// Some problems on 2-D Arrays

// Transpose of a matrix

for (int i = 0; i < n; i++) {
    for (int j = i; j < m; j++) {          // See the range of j, we swapped upper triangular with lower triangular matrix
        int temp = arr[i][j];              // if j is from 0 to m - 1, then swap would have performed two times which means no swapping at all.
        arr[i][j] = arr[j][i];
        arr[j][i] = temp;
    }
}

for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        std::cout << arr[i][j] << " ";
    }
    std::cout << "\n";
}

// Matrix Multiplication (n1xn2 and n2xn3) --------> Very Important

int n1, n2, n3;
std::cin >> n1 >> n2 >> n3;

int m1[n1][n2];
int m2[n2][n3];

for (int i = 0; i < n1; i++) {
    for (int j = 0; j < n2; j++) {
        std::cin >> m1[i][j];
    }
}

for (int i = 0; i < n2; i++) {
    for (int j = 0; j < n3; j++) {
        std::cin >> m2[i][j];
    }
}

int ans[n1][n3];                // creating ans matrix with all zero entries
for (int i = 0; i < n1; i++) {
    for (int j = 0; j < n3; j++) {
        ans[i][j] = 0;
    }
}

for (int i = 0; i < n1; i++) {
    for (int j = 0; j < n3; j++) {
        for (int k = 0; k < n2; k++) {
            ans[i][j] += m1[i][k]*m2[k][j];
        }
    }
}

for (int i = 0; i < n1; i++) {
    for (int j = 0; j < n3; j++) {
        std::cout << ans[i][j] << " ";
    }
    std::cout << "\n";
}
//                                                                        we are starting
// Searching a target element in a sorted matrix;            1  4  7  11  our pointer from top right
//                                                           2  5  8  12
//                                                           3  6  9  16
//                                                           10 13 14 17
//                                                 we can start 
// Logic          <X  X                            from this corner also
//                    >X

int n,m; 
std::cin >> n >> m;
int target; 
std::cin >> target;
int mat[n][m];

for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        std::cin >> mat[i][j];
    }
}

int r = 0, c = m - 1;
bool found;
while (r < n and c >= 0) {
    if (mat[r][c] == target) {
        found = true;
        break;
    }
    else if (mat[r][c] > target) {
        c--;
    }
    else {
        r++;
    }

}
if (found == true) {
    std::cout << "Element found";
}
else {
    std::cout << "Element does not exist";
}


}