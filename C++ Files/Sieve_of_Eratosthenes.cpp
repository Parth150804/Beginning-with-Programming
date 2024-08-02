#include "bits/stdc++.h"

using namespace std;

// 0 -----> unmarked and 1 -----> marked

void primeSieve(int n) {                // printing prime numbers upto n
    int prime[n] = {0};
    for (int i = 2; i <= n; i++) {
        if (prime[i] == 0) {
            for (int j = i*i; j <=n ; j += i) {
                prime[j] = 1;
            }
        }
    }
    for (int i = 2; i <= n; i++) {
        if (prime[i] == 0) {
            std::cout << i << " ";
        }
    }
}

void primefactor(int n) {
    int spf[n] = {0};
    for (int i = 0; i <= n; i++) {
        spf[i] = i;
    }
    for (int i = 2; i <= n; i++) {
        if (spf[i] == i) {
            for (int j = i*i; j <= n; j += i) {
                if (spf[j] == j) {
                    spf[j] = i;
                } 
            }
        }
    }

    while (n != 1) {
        std::cout << spf[n] << " ";
        n /= spf[n];
    }
}



int main() {
    int n;
    std::cin >> n;
    // primeSieve(n);


    // Prime Factorization of a number
    primefactor(n);

}