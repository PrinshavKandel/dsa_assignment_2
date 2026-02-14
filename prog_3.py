class Node:
    """Node class for linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked List class"""
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        """Insert a new node at the end of the list"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def reverse_traversal(self):
        """Reverse traversal using stack"""
        if self.head is None:
            print("List is empty")
            return
        
        stack = []
        current = self.head
        
        # Push all nodes onto stack
        while current:
            stack.append(current.data)
            current = current.next
        
        # Pop from stack to print in reverse
        print("Reverse Traversal: ", end="")
        while stack:
            print(stack.pop(), end=" ")
        print()


def main():
    """Main function to demonstrate reverse traversal"""
    # Create linked list
    ll = LinkedList()
    
    # Insert elements
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.insert(40)
    ll.insert(50)
    
    # Perform reverse traversal
    ll.reverse_traversal()


if __name__ == "__main__":
    main()
