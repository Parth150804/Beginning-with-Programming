#include "bits/stdc++.h"

using namespace std;

// Every element of a linked list (node) will have a data and a 'pointer' which is pointing 
// towards the address of the next node.

// Structure of a Singly Linked list:
// NODE =  Data | Next

//    10k        20k        30k        40k
//   1 | 20k -> 2 | 30k -> 3 | 40k -> 4 | NULL
//     ^
//     |
//    HEAD = 10k (head pointer stores the address of head node)

// This HEAD pointer will be created in main() func before creating list

// Creating the node (a data type defined by us, ADT)
// -> means pointing towards, used only with pointer

class node {                // val -> NULL
    public:
    int data;           // data in node will be of type int 
    node* next;         // name of 'pointer of the node' is next

    node(int val) {     // (This is Constructor) node will accept a single argument (data will be assigned that value)
        data = val;
        next = NULL;    // and pointer will be set to point towards NULL(if we print it, output will be zero)
    }
};

// We can also encapsulate all these functions inside the class


void insertAtHead(node* &head, int val) {       // Since we need to modify our linked list,
    node* n = new node(val);                    // we will take input by reference, not by value
    n -> next = head;      // n -> next will give address whereas n -> data will give value             
    head = n;           // setting head pointer to head
}

void insertAtTail(node* &head, int val) {       // we have to traverse whole list from the beginning (head), that's why we have to pass head as argument

    node* n = new node(val);        // a pointer n of a node which will store address
                                    // of data(= val) which is to be inserted at head
    if(head == NULL) {      // Condition when our linked list is empty             
        head = n;
        return;
    }

    node* temp = head;
    while(temp -> next != NULL) {
        temp = temp -> next;
    }
    temp -> next = n;

}

void display(node* head) {      // Here we will take input by value as we are not modifying our linked list
    node* temp = head;              // So, we can use directly head also instead of temp
    while(temp != NULL) {
        std::cout << temp -> data << "->";
        temp = temp -> next;
    }
    std::cout << "NULL" << "\n";
}

bool search(node* head, int key) {

    node* temp = head;
    while(temp != NULL) {
        if(temp -> data == key) {
            return true;
        }
        temp = temp -> next;
    }
    return false;
}

// Deletion in a linked list

void deleteAtHead(node* &head) {
    node* toDelete = head;
    head = head -> next;

    delete toDelete;
}

void deletion(node* &head, int val) {       // This will not work for head as to delete nth node,
                                            // we are going till (n-1)th node
    if(head == NULL) {              // When list is empty
        return;
    }
    if(head -> next == NULL) {         // When list has only one element, head node
        deleteAtHead(head);
        return;
    }
    node* temp = head;
    while(temp -> next -> data != val) {            // Reaching till (n-1)th node
        temp = temp -> next;
    }
    node* toDelete = temp -> next;
    temp -> next = temp -> next -> next;

    delete toDelete;             // make sure to delete this otherwise there will be memory overflow or leak
}

// Reversing a linked list (three pointers will be made - previous, current & next) ----------> Very Important

node* reverse(node* &head) {        // Iterative Method

    node* prevptr = NULL;   // Initialized with NULL
    node* currptr = head;   //------""---- at head
    node* nextptr;

    while(currptr != NULL) {                // Termination condition will be when current becomes NULL
        nextptr = currptr -> next;          
        currptr -> next = prevptr;

        prevptr = currptr;
        currptr = nextptr;

    }                                   // head of reversed linked-list will be previous pointer

    return prevptr;
}

node* reverse_Rec(node* &head) {            // Recursive method
    if (head == NULL or head -> next == NULL) {         // When linked list is empty or contains only one element
        return head;
    }

    node* newhead = reverse_Rec(head -> next);
    head -> next -> next = head;            // Very Important
    head -> next = NULL;                    // step (we can access a node using it's address)

    return newhead;
}

// Reversing K-Nodes (using recursion)

node* Reverse_K_Nodes(node* &head, int k) {
// First reversing k-nodes using iterative method & then recursively calling it for remaining list

    node* prevptr = NULL;   
    node* currptr = head;   
    node* nextptr;

    int count = 0;          // This will keep track that only k-nodes get reversed
    while (currptr != NULL and count < k) {
        nextptr = currptr -> next;
        currptr -> next = prevptr;
        prevptr = currptr;
        currptr = nextptr;
        count++;
    }

    if (nextptr != NULL) {
    head -> next = Reverse_K_Nodes(nextptr, k);         // Important step
}
    return prevptr;

}

// Detection and Removal of Cycle in a linked list (Floyd's Algorithm OR Hare and Tortoise Algorithm)

void makeCycle(node* &head, int pos) {
    node* temp = head;
    node* startNode;

    int count = 1;
    while(temp -> next != NULL) {
        if (count == pos) {
            startNode = temp;
        }
        temp = temp -> next;
        count++;
    }

    temp -> next = startNode;
}

bool detectCycle(node* head) {

    node* slow = head;              // this will move one step at a time
    node* fast = head;              // this will move two step at a time

    while(fast != NULL and fast -> next != NULL) {      // Since fast will always cover more distance, the termination 
        slow = slow -> next;                            // condition of this loop will depend on it
        fast = fast -> next -> next;

        if (fast == slow) {
            return true;
        }
    }
    return false;
}

void removeCycle(node* &head) {

    node* slow = head;
    node* fast = head;

    do {
        slow = slow -> next;
        fast = fast -> next -> next;
    } while(slow != fast);

    fast = head;
    while(slow -> next != fast -> next) {
        slow = slow -> next;
        fast = fast -> next;
    }

    slow -> next = NULL;

}

int length(node* head) {

    int l = 0;
    node* temp = head;
    while (temp != NULL) {
        l++;
        temp = temp -> next;
    }

    return l;
}


node* Append_last_k_Nodes(node* &head, int k) {             // Cannot handle k = 1
    if (head == NULL) {
        return NULL;
    }


    node* newHead;
    node* newTail;
    node* tail = head;

    int l = length(head);
    k = k%l;                // to handle the case when k > l

    int count = 1;
    while(tail -> next != NULL) {
        if (count == l-k) {
            newTail = tail;
        }
        if (count == l-k+1) {
            newHead = tail;
        }
        tail = tail -> next;
        count++;
    }

    newTail -> next = NULL;
    tail -> next = head;

    return newHead;
}

// Intersection point of 2 linked lists

void intersect(node* &head1, node* &head2, int pos) {           // Function to intersect two linked lists

// head1 is assumed to be head of longer list

    node* temp1 = head1;
    pos--;
    while(pos--) {
        temp1 = temp1 -> next;
    }

    node* temp2 = head2;

    while (temp2 -> next != NULL) {
        temp2 = temp2 -> next;
    }

    temp2 -> next = temp1;
}



int intersection(node* head1, node* head2) {            // Time complexity = O(length of longer list)

    int l1 = length(head1);
    int l2 = length(head2);

    int d = 0;
    node* ptr1;             // pointes on the list which has greater length
    node* ptr2;             // ---------------""-------------shorter--""----

    if (l1 > l2) {
        d = l1 - l2;
        ptr1 = head1;
        ptr2 = head2;
    }
    else {
        d = l2 - l1;
        ptr1 = head2;
        ptr2 = head1;
    }

    while(d != 0) {             // pointer associated with the list having longer length should start from index = difference of length of the lists
        ptr1 = ptr1 -> next;
        if (ptr1 == NULL) {
            return -1;          // Intersection not possible
        }
        d--;
    }

    while (ptr1 != NULL and ptr2 != NULL) {
        if (ptr1 == ptr2) {
            return ptr1 -> data;
        }
        ptr1 = ptr1 -> next;
        ptr2 = ptr2 -> next;

    }

    return -1;



}

// Merging two sorted linked lists      T.C = O(n+m)

node* merge(node* &head1, node* &head2) {       // We are not making a new list, instead we are just changing the links

    node* p1 = head1;
    node* p2 = head2;
    node* dummyNode = new node(-1);
    node* p3 = dummyNode;

    while(p1 != NULL and p2 != NULL) {

        if (p1 -> data < p2 -> data) {
            p3 -> next = p1;
            p1 = p1 -> next;
        }
        else {
            p3 -> next = p2;
            p2 = p2 -> next;
        }

        p3 = p3 -> next;
    }

    while (p1 != NULL) {
        p3 -> next = p1;
        p1 = p1 -> next;
        p3 = p3 -> next;
    }

    while (p2 != NULL) {
        p3 -> next = p2;
        p2 = p2 -> next;
        p3 = p3 -> next;
    }

    return dummyNode -> next;           // Because merged list starts from next of dummynode
}

node* merge_recursive(node* &head1, node* &head2) {
    if (head1 == NULL) {
        return head2;
    }

    if (head2 == NULL) {
        return head1;
    }
    node* result;
    if (head1 -> data < head2 -> data) {
        result = head1;
        result -> next = merge_recursive(head1 -> next, head2);
    }

    else {
        result = head2;
        result -> next = merge_recursive(head1, head2 -> next);
    }

    return result;
}



int main() {

    node* head = NULL;
    insertAtTail(head, 1);
    insertAtTail(head, 2);
    insertAtTail(head, 3);
    display(head);
//     insertAtHead(head, 4);
//     insertAtTail(head, 2);
//     insertAtTail(head, 3);
//     insertAtHead(head, 5);
//     display(head);

// std::cout << search(head, 3);

//     // deletion(head, 3);
//     // deleteAtHead(head);
//     display(head);
//     // node* newhead = reverse(head);
//     node* newhead = reverse_Rec(head);
//     display(newhead);

// insertAtTail(head, 1);
// insertAtTail(head, 2);
// insertAtTail(head, 3);
// insertAtTail(head, 4);
// insertAtTail(head, 5);
// insertAtTail(head, 6);

// // makeCycle(head, 3);
// display(head);           // This will print the list infinite times because of display function

// std::cout << detectCycle(head) << "\n";

// removeCycle(head);
// std::cout << detectCycle(head) << "\n";
// display(head);
// node* newhead = Reverse_K_Nodes(head, 2);
// display(newhead);

// node* newhead = Append_last_k_Nodes(head, 1);
// display(newhead);


// Remember NULL and nullptr can only be used for pointers


node* head1 = NULL;
node* head2 = NULL;

// insertAtTail(head1, 1);
// insertAtTail(head1, 2);
// insertAtTail(head1, 3);
// insertAtTail(head1, 4);
// insertAtTail(head1, 5);
// insertAtTail(head1, 6);

// insertAtTail(head2, 9);
// insertAtTail(head2, 10);

// intersect(head1, head2, 3);

// display(head1);
// display(head2);

// std::cout << intersection(head1, head2);

// int arr1[] = {1, 4, 5, 7};
// int arr2[] = {2, 3, 6};

// for (int i = 0; i < 4; i++) {
//     insertAtTail(head1, arr1[i]);
// }

// for (int i = 0; i < 3; i++) {
//     insertAtTail(head2, arr2[i]);
// }


// display(head1);
// display(head2);

// node* newHead = merge_recursive(head1, head2);
// display(newHead);

}