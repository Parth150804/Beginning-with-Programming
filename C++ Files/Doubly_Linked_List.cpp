#include "bits/stdc++.h"

using namespace std;

// Including next, there will be a previous (name) pointer which will point towards previous node (because of this we can traverse in both directions)

// Structure of a Doubly Linked list:
// NODE =  Previous | Data | Next

//         10k              20k              30k              40k
//   NULL | 1 | 20k <-> 10k | 2 | 30k <-> 20k | 3 | 40k <-> 30k | 4 | NULL
//          ^
//          |
//      HEAD = 10k (head pointer stores the address of head node)

class node {
    public:

    int data;
    node* next;
    node* prev;

    node(int val) {             // NULL <- val -> NULL
        data = val;
        next = NULL;
        prev = NULL;
    }                           // Destructor doesn't make sense as we have only class node not class list
};

void insertAtHead(node* &head, int val) {

    node* n = new node(val);
    n -> next = head;
    if (head != NULL) {
        head -> prev = n;
    }

    head = n;

}

void insertAtTail(node* &head, int val) {
    if (head == NULL) {
        insertAtHead(head, val);
        return;
    }

    node* n = new node(val);
    node* temp = head;

    while (temp -> next != NULL) {
        temp = temp -> next;
    }

    temp -> next = n;
    n -> prev = temp;

}

void display(node* head) {
    node* temp = head;
    if (head != NULL) {
        int count = 1;
        std::cout << "NULL<-";
        while (temp != NULL) {
            if (count == 1 and temp -> next != NULL) {
                std::cout << temp -> data << "<->";
                temp = temp -> next;
                count++;
            }
            else if (count == 2) {
                std::cout << temp -> data;
                temp = temp -> next;
                count++;
            }
            else if (count > 2) {
                std::cout << "<->";
                std::cout << temp -> data;
                temp = temp -> next;
            }
            else {
                std::cout << temp -> data;
                temp = temp -> next;
            }

        }
        std::cout << "->NULL" << "\n";
}
    else {
        std::cout << "NULL" << "\n";
    }

}

void deleteAtHead(node* &head) {

    node* todelete = head;
    head = head -> next;
    // head -> prev = NULL;


    delete todelete;
}

void deletion(node* &head, int pos) {
// Edge cases: 1) When we have to delete last node, we cannot access temp -> next -> prev
//             2) When we have to delete first node, we cannot access temp -> prev -> next

    if (pos == 1) {         // To deal with edge case 2)
        deleteAtHead(head);
        return;
    }
    node* temp = head;
    int count = 1;          // To note the count of the position

    while(temp != NULL and count != pos) {
        temp = temp -> next;
        count++;
    }

    temp -> prev -> next = temp -> next;

    if (temp -> next != NULL) {         // To deal with edge case 1)
        temp -> next -> prev = temp -> prev;
    }

    delete temp; 
}


int main() {

    node* head = NULL;
    insertAtTail(head, 1);
    insertAtTail(head, 2);
    insertAtTail(head, 3);
    insertAtTail(head, 4);

    display(head);

    deletion(head, 1);
    deletion(head, 1);
    deletion(head, 1);
    deletion(head, 1);
    display(head);
    
}