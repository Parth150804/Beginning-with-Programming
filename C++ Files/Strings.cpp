#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Single quotes are used to identify letters and diuble quotes are used to identify strings

int main() {
    // string str;
    // getline(cin, str);  // <------------- used to take single input of string with spaces
    // std::cout << str;



    // Joining of strings

    // string s1 = "fam";
    // string s2 = "ily";
    // s1.append(s2);      // or s1 = s1 + s2
    // std::cout << s1;

    // NOTE: 1) Indexing in string is same as indexing in array

    // 2) .clear() is used to clear the string or to make it empty

    // 3) .empty() returns bool value that string is empty or not

    // 4) .erase(starting index of deletion, no. of char to be deleted) func is used to delete char from a string

    // 5) .find(substring) is used to check whether a substring is present in a string. It returns the index from where 
    // the subtring starts (it's first occurance). If substring which is not in string is passed in find, it returns a very large number

    // 6) .insert(index where another string has to inserted, another string) is used to insert a string 

    // 7) .size() or .len() is used to get size of a string (it counts spaces too)

    // 8) .substr(index from where subtring starts, no. of character we want after that index) is used to get substring of a string

    // 9) stoi(s) is used to typecast string to int and for reverse, we use to_string(int)

    // 10) sort(s.begin(), s.end()) is used to sort a string

    // 11) toupper() and tolower() are used to convert a letter to upper or lower case resp. and isupper() and islower() are used for checking.
    
    // 12) to convert whole string to a case, use transform(idx1, idx2, idx3, ::toupper/tolower)


    // .compare()

    // string s1 = "abc";
    // string s2 = "abc";
    // std::cout << s1.compare(s2);

    // if s2 > s1 (lexiographically or acc. to dictionary order), it returns -1
    // else if s1 == s2, it returns 0
    // else returns 1



}