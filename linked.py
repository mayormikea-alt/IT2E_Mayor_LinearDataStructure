# Assessment 3.2: Singly Linked List Program
# Last Name: MAYOR

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_from_head(self):
        if not self.head:
            return False
        self.head = self.head.next
        return True

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        if not elements:
            print("[EMPTY]")
        else:
            print(" -> ".join(elements) + " -> NULL")

print("--- LINKED LIST INSERTION ---")
ll = SinglyLinkedList()
for letter in "MAYOR":
    ll.insert_at_end(letter)
    ll.display()

print("\n--- LINKED LIST DELETION ---")
while ll.head:
    ll.delete_from_head()
    ll.display()