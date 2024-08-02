#include "bits/stdc++.h"

using namespace std;

// NOTE: 1) In bit manipulation, a) use & instead of &&, b) use | instead of ||
//       2) a << b (left-shifting of an integer 'a' by an integer 'b') is equivalent to a*(2^b)

int getBit (int n, int pos) {      
    return (n & (1 << pos)) != 0;
}

int setBit (int n, int pos) {
    return (n | (1 << pos));
}

int clearBit (int n, int pos) {
    int mask = ~(1 << pos);
    return (n & mask);
}

int updateBit (int n, int pos, int value) {             // Set bit then clear bit
    int mask = ~(1 << pos);         // taking 1's complement
    n = n & mask;
    return (n | (value << pos));
}

// Some Questions

bool is_pow_of_2(int n) {
    if ((n == 0) or (n & n - 1) == 0) {
        return true;
    }
    else {
        return false;
    }
}

int no_of_ones(int n) {
    int count = 0;
    while (n != 0) {
        n = n & (n - 1);
        count++;
    }
    return count;
}

void print_subsets(int arr[], int n) {
    for (int i = 0; i < (1 << n); i++) {            // 1 << n = 2^n
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                std::cout << arr[j] << " ";
            }
        }
        std::cout << "\n";
    }
}

int unique_in2(int arr[], int n) {
    int xorsum = 0;
    for (int i = 0; i < n; i++) {
        xorsum = xorsum ^ arr[i];
    }
    return xorsum;
}

void two_unique(int arr[], int n) {
    int xorsum = 0;
    
    for (int i = 0; i < n; i++) {
        xorsum = xorsum ^ arr[i];
    }
    int tempxor = xorsum;
    int setbit = 0;
    int pos = 0;
    while (setbit != 1) {
        setbit = xorsum & 1;
        pos++;
        xorsum = xorsum >> 1;
    }
    int newxor = 0;
    for (int i = 0; i < n; i++) {
        if (getBit(arr[i], pos - 1)) {
            newxor = newxor ^ arr[i];
        }
    }
    std::cout << newxor << "\n";
    std::cout << (tempxor ^ newxor);
}

int unique_in3(int arr[], int n) {
    int result = 0;
    for (int i = 0; i < 64; i++) {
    int sum = 0;
    for (int j = 0; j < n; j++) {
        if (getBit(arr[j], i)) {
            sum++;
        }
    }
    if (sum%3 != 0) {
        result = setBit(result, i);
    }
    }
    return result;
}


// Important Conversions


int binaryTodecimal(int n) {
    int ans = 0;
    int x = 1;
    while (n > 0) {
        int y = n%10;
        ans += x * y;
        x *= 2;         // for octal change 2 to 8
        n /= 10;
    }
    return ans;
}

std::string decimalTobinary(int n) {
    string ans = "\0";
    while (n > 0) {
        int s1 = n%2;
        string s2 = to_string(s1);
        ans = s2.append(ans);
        n = n/2;
    }
    return ans;
}

std::string octalTobinary(int n) {
    string ans = "\0";
    while (n > 0) {
        int s1 = n%8;
        string s2 = to_string(s1);
        ans = s2.append(ans);
        n = n/8;
    }
    return ans;
}

int hexadecimalTodecimal(string n) {

int ans = 0;
int x = 1;

int s = n.size();
for (int i = s - 1; i >= 0; i--) {
    if (n[i] >= '0' && n[i] <= '9') {
        ans += x*(n[i] - '0');
    }
    else if (n[i] >= 'A' && n[i] <= 'F') {
        ans += x*(n[i] - 'A' + 10);
    }

    x *= 16;
}
return ans;
}

std::string decimalTohexadecimal(int n) {
    int x = 1;
    string ans = "";
    while (x <= n) {
        x *= 16;
    }
    x /= 16;
    while (x > 0) {
        int lastDigit = n/x;
        n -= lastDigit*x;
        x /= 16;
    
    if (lastDigit <= 9) {
        ans += to_string(lastDigit);
    }
    else {
        char c = 'A' + lastDigit - 10;
        ans.push_back(c);
    }
}
    return ans;
}


string add_bin_num(int n, int m) {
    int n1 = binaryTodecimal(n);
    int n2 = binaryTodecimal(m);
    int ans = n1 + n2;
    return decimalTobinary(ans);
}

// int reverse(int n) {
//     int res = 0;
//     while (n > 0) {
//         int lastDigit = n%10;
//         res = res * 10 + lastDigit;
//         n /= 10;
//     }
//     return res;
// }

// int addBinary(int a, int b) {
//     int ans = 0;
//     int prevCarry = 0;
//     while (a > 0 && b > 0) {
//         if (a%2 == 0 && b%2 == 0) {
//             ans = ans * 10 + prevCarry;
//         }
//         else if ((a%2 == 0 && b%2 == 1) || (a%2 == 1 && b%2 == 0)) {
//             if (prevCarry == 1) {
//                 ans = ans*10 + 0;
//                 prevCarry = 1;
//             }
//             else {
//                 ans = ans*10 + 1;
//                 prevCarry = 0;
//             }
//         }
//         else {
//             ans = ans * 10 + prevCarry;
//             prevCarry = 1;
//         }
//         a /= 10;
//         b /= 10;
//     }
//     while ( a > 0) {
//         if (prevCarry == 1) {
//             if (a%2 == 1) {
//             ans = ans * 10 + 0;
//             prevCarry = 1;
//             }
//             else {
//             ans = ans*10 + 1;
//             prevCarry = 0;
//             }
            
//         }
//         else {
            
//             ans = ans * 10 + (a%2);
//         }
//         a /= 10;
//     }
//     while ( b > 0) {
//         if (prevCarry == 1) {
//             if (b%2 == 1) {
//             ans = ans * 10 + 0;
//             prevCarry = 1;
//             }
//             else {
//             ans = ans*10 + 1;
//             prevCarry = 0;
//             }
            
//         }
//         else {
            
//             ans = ans * 10 + (b%2);
//         }
//         b /= 10;
//     }

//     if (prevCarry == 1) {
//         ans = ans*10 + 1;
//     }
//     ans = reverse(ans);
//     return ans;
// }


int main() {

// 1) Get Bit (at a given position, tell which bit is present, 0 or 1). E.g
// Indexing starts from 'rightmost number' with a value of 0

int n = 0101;   // Binary form of 5

// Suppose we need to get bit at position i = 2

// i) Form a number 1 << i (Here it will be 0100)

int m = 1 << 2;

// ii) if n & (m) != 0, then bit is 1 (means the condition after if is true), otherwise 0

// std::cout << getBit(19, 3);

// 2) Set bit (given a position where zero is there, we have to put value 1 there)

// Similarly create a number 1 << i and do n | (1 << i)

// std::cout << setBit(5, 1);

// 3) Clear bit or Unset bit (set bit at given pos where 1 is there to 0, and if 0 then leave as it is)

// Create 1 << i = m(say), then m = ~m (taking 1s complement) and m & n(original number) ----> ans 

// std::cout << clearBit(5, 1);

// 4) Update bit (set a bit at given pos to 1 or 0 whichever is passed)
// It is basically clear bit and set bit

// 1 << i = m, m1 = ~m
// m1 && n = p(say)
// m | p = ans

// or Clear bit and Unset bit

// std::cout << updateBit(5, 2, 0);




// int arr[4] = {1, 2, 3, 4};
// print_subsets(arr, 4);


// int arr[] = {1, 2, 3, 4, 1, 2, 3};
// std::cout << unique_in2(arr, 7);


// int arr[] = {1, 2, 3, 1, 2, 3, 7, 5};
// two_unique(arr, 8);





// NOTE: Decimal to Binary conversion

// 1) To obtain digits of int N (which is written in decimal system), we use N%10 and at every step we update N as N/10 
//    till N = 0 (digits will be obtained in reverse order).
// 2) Using similar logic, to obtain digits of N (given in decimal form) in binary form, we use N%2 and update N as N/2 
//    till N = 0 (digits will be obtained in reverse order).

// std::cout << decimalTobinary(10);
// std::cout << binaryTodecimal(1010);
// std::cout << hexadecimalTodecimal("1CF");
// std::cout << octalTobinary(100);
// std::cout << decimalTohexadecimal(463);
// std::cout << add_bin_num(10101, 11010);


}
