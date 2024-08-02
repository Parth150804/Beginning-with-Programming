#include <bits/stdc++.h>

using namespace std;

// Map is an associative array

int main() {
    // Ordered Maps (implemented using red-black trees)
    map<string, int> marksMap;
    marksMap["Harry"] = 98;
    marksMap["Jack"] = 59;
    marksMap["Rohan"] = 2;
    
    marksMap.insert({{"Parth", 165}, {"Shantanu", 45}});

    // if value is inserted at existing key, then its value gets updated (stores unique key value pair)

    map<string, int> :: iterator itr;

    for (itr = marksMap.begin(); itr != marksMap.end(); itr++) {
        std::cout << (*itr).first << " " << (*itr).second << "\n";
    }

    // This can be used instead of above for loop and iterator
    // for (auto &itr : marksMap) {
    // std::cout << itr.first << " " << itr.second << "\n"
    // }

    std::cout << "The size is: " << marksMap.size() << "\n";
    std::cout << "Max Size is: " << marksMap.max_size() << "\n";
    std::cout << "Is map empty? - " << marksMap.empty() << "\n";

    auto it = marksMap.find("Parth");  // .find() returns an iterator

    // if key inside .find() doesn't exist then it will return marksMap.end()
    // .clear() clears the map
    std::cout << (*it).first << " " << (*it).second << "\n";


// Q. Given N strings, print unique strings in lexiographical order with their frequency.
// N <= 10^5
// S <= 100

map<string, int> m;
int n;
std::cin >> n;
for (int i = 0; i < n; i++) {
    string s;
    std::cin >> s;
    m[s] = m[s] + 1;          // if we initialize a key then by default zero value gets stored there
}

for (auto pr : m) {
    std::cout << pr.first << " " << pr.second << "\n";
}


// Unordered Maps (implemented using hashtables)
// syntax is same, just use unordered_map instead of map
// pairs cannot be used in unordered maps (because no hash func is defined for pairs)

}