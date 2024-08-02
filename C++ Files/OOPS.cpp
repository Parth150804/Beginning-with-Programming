#include "bits/stdc++.h"

using namespace std;

// class Student {
//     public:                 // To access these data members outside class, we use public:

//     string name;            // These are 
//     int age;                // data
//     bool gender;            // members (attributes)

//     void printInfo() {                   // This is member function
//         std::cout << "Name: ";
//         std::cout << name << "\n";
//         std::cout << "Age: ";
//         std::cout << age << "\n";
//         std::cout << "Gender: ";
//         std::cout << gender << "\n";
//     }
// };

class Student {
    string name;
    public:                
            
    int age;                
    bool gender;  

    Student() {
        // std::cout << "Default Constructor" << "\n";         // When no arguments are passed then default constructor is called
    }   // Default Constructor

    Student(string s, int a, int g) {
        // std::cout << "Parameterised Constructor" << "\n";         
        name = s;
        age = a;
        gender = g;
    }   // Parameterised Constructor

    Student(Student &a) {       // if & is not used, this copy constructor will be called again and again
        // std::cout << "Copy Constructor" << "\n";         
        name = a.name;
        age = a.age;
        gender = a.gender;
    }   // Copy Constructor

// NOTE: There also exist a default copy constructor (it uses Shallow copy whereas copy constructor defined by us uses Deep copy) 


    ~Student() {
        // std::cout << "Destructor called" << "\n";
    }   // called when objects get destroyed (when we go out of main func)

    void setName(string s) {            // Function to access (here set) a private data member (therfore it is called setter function)
        name = s;
    }          

    void getName() {
        std::cout << name << "\n";      // Similarly, this is getter function
    }
    void printInfo() {
        std::cout << "Name: ";
        std::cout << name << "\n";
        std::cout << "Age: ";
        std::cout << age << "\n";
        std::cout << "Gender: ";
        std::cout << gender << "\n";
    }

// Defining == operator
    bool operator == (Student &a) {
        if (name == a.name and age == a.age and gender == a.gender) {
            return true;
        }
        else {
            return false;
        }
    }
};


// // Encapsulation (wrapping up data members & functions)

//    here capsule is used for class (because data members and functions are wrapped up in class)
//    Fully encapsulated class -> Data members are private and methods are public

class Employee {
private:
    string name;
    int age;
    int height;

public:
    int getAge() {
        return age;
    }

    int getHeight() {
        return height;
    }
};


// // Inheritance

// // Single Inheritance  (class B -----> class A )
// class A {
// public:
//     void func() {
//         std::cout << "Inherited";
//     }
// };

// class B : public A {            // Things which are inherited from class A will be in public to class B
// };


// // Multiple Inheritance (class A -----> class C & class B -----> class C)
// class A {
//     public:
//     void Afunc() {
//         std::cout << "Func A\n";
//     }
// };

// class B {
//     public:
//     void Bfunc() {
//         std::cout << "Func B\n";
//     }
// };

// class C : public A, public B {
//     public:
// };

// // Multi-Level Inheritance (class C -----> class B -----> class A)

// class A {
//     public:
//     void Afunc() {
//         std::cout << "Func A\n";
//     }
// };

// class B : public A {
//     public:
//     void Bfunc() {
//         std::cout << "Func B\n";
//     }
// };

// class C : public B {
//     public:
// };

// Hybrid Inheritance (multiple + multi-level)

// Hierarchical Inheritance (have structure like a binary tree with arrow pointing upwards)

// NOTE: private members cannot be accessed outside the class as well as they are not inherited whereas protected members can be inherited
//       but cannot be accessed outside the class

// An example:

class Ground {
    int Rooms;
protected:
    void put();
public:
    void get();
};
class Middle : private Ground {
    int Labs;
public:
    void Take();
    void Give();
};
class Top : public Middle {
    int Roof;
public:
    void In();
    void Out();
};

// Type of inheritance: Multi-Level
// Give() member func of class middle can access data members - Labs & member func - Put(), Get(), Take(), Give()
// Members which are accessible by the member func Out() of the class Top - Data members: Roof & Member functions: Take(), Give(), In(), Out()
// Write names of all the members which are directly accessible by the object T of class Top declared in main() function.
// Ans. Take(), Give(), In(), Out()



// Polymorphism (poly - many & morph - forms)

// 1) Compile Time Polymorphism (Static Polymorphism)
// A) Function Overloading
class Practice {
    public:
    void func() {
        std::cout << "I am a function with no arguments\n"; 
    }

    void func(int x) {
       std::cout << "I am a function with int argument\n"; 
    }

    void func(double x) {
       std::cout << "I am a function with double argument\n"; 
    }
};

// B) Operator Overloading
class Complex {
    private:
        int real, imag;
    public:
        Complex(int r, int i) {
            real = r;
            imag = i;
        }
    Complex operator + (Complex const &obj) {
        Complex res(0, 0);
        res.imag = imag + obj.imag;
        res.real = real + obj.real;
        return res;
    }

    void display() {
        std::cout << real << " + i" << imag << "\n";
    }
};


// 2) Run-Time Polymorphism (Dynamic Polymorphism)
// Method (or function) Overriding
// redefined func before whose name virtual is not written will be called
class base {
    public:
       virtual void print() {
            std::cout << "This is the base class's print function\n";
        }

        void display() {
            std::cout << "This is the base class's display function\n";
        }
};

class derived : public base {
    public:
        void print() {
                std::cout << "This is the derived class's print function\n";
        }

        void display() {
            std::cout << "This is the derived class's display function\n";
        }
};

// Abstraction (Implementation Hiding)
// Can be done using Classes, Header files, Access Specifiers


// Stack vs Heap Allocation

class A1 {
    public:
    int id;

    A1(int i) {
        id = i;
        std::cout << "Created object with ID: " << id << "\n";
    }

    ~A1() {
        std::cout << "Destroyed object with ID: " << id << "\n";
    }

};

int main() {

    // Student a;
    // a.name = "Parth";
    // a.age = 19;
    // a.gender = 0;

    // Student arr[3];
    // for (int i = 0; i < 3; i++) {
    //     std::cout << "Name: ";
    //     std::cin >> arr[i].name;
    //     std::cout << "Age: ";
    //     std::cin >> arr[i].age;
    //     std::cout << "Gender: ";
    //     std::cin >> arr[i].gender;
    // }

    // for (int i = 0; i < 3; i++) {
    //     arr[i].printInfo();
    // }




    // Student arr1[3];
    // for (int i = 0; i < 3; i++) {
    //     string s;
    //     std::cout << "Name: ";
    //     std::cin >> s;
    //     arr1[i].setName(s);
    //     std::cout << "Age: ";
    //     std::cin >> arr1[i].age;
    //     std::cout << "Gender: ";
    //     std::cin >> arr1[i].gender;
    // }

    // for (int i = 0; i < 3; i++) {
    //     arr1[i].printInfo();
    // }

Student a("Parth", 19, 0);
// a.getName();
// a.printInfo();

Student b;  // This would have given error if default constructor doesn't exist

Student c = a;  // or Student c(a) -------> Used to copy all attributes of a to c


// Operator Overloading 

// if (c == a) {
//     std::cout << "Same" << "\n";
// }

// else {
//     std::cout << "Not Same" << "\n";
// }



// Inheritance

// Base Class(parent) & Derived Class(child)

// Types:
// Single, Multiple, Multi-Level, Hybrid, Hierarchical

// // Single
// B b1;
// b1.func();

// // Multiple
// C c1;
// c1.Afunc();
// c1.Bfunc();

// // Multi-Level
// C c2;
// c2.Afunc();
// c2.Bfunc();



// Polymorphism
// Types:
// A) Compile Time: a) Function Overloading (function having same name but having different behaviour 
// like different no. of arguments or different types of argument). 
// b) Operator Overloading (same operator defined in different way like '+' in normal addition and '+' in additon of complex numbers).
// B) Run Time: a) Virtual Functions (if a function is in base class as well as derived class then the one will be called which doesn't have virtual
// keyword before it).

// Practice obj;
// obj.func();
// obj.func(4);
// obj.func(6.2);


// Complex c1(2, 5);
// Complex c2(9, 3);
// Complex c3 = c1 + c2;
// c3.display();

// NOTE: first ptr class' func will be called, if virtual is used, then object class' func will be called

// base* baseptr;
// derived d;
// baseptr = &d;

// baseptr -> print();
// baseptr -> display();       // If no virtual word is used then func of base class will be called because pointer is of base class


// NOTE: new (an operator) keyword returns a pointer to the memory we allocate

A1 a1(3);               // allocation of memory in stack (will be destroyed by system after getting out of main func)
A1* a2 = new A1(5);     // allocation of memory in heap (we have to destroy this)

delete(a2);      // -------> deallocate memory (also calls destructor)

// In stack, memory allocation will be made by system but in heap it is done manually
}