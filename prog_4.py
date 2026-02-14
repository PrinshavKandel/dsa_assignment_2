class Node:
    """Node structure for doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Doubly Linked List class"""
    def __init__(self):
        self.head = None
    
    def insert_after(self, prev_node, data):
        """Insert a new node after given node"""
        if prev_node is None:
            print("Previous node cannot be None")
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        
        if new_node.next is not None:
            new_node.next.prev = new_node
    
    def delete_node(self, node):
        """Delete the given node from doubly linked list"""
        if self.head is None or node is None:
            print("Cannot delete")
            return
        
        # If node to be deleted is head
        if self.head == node:
            self.head = node.next
        
        # Change next only if node to be deleted is not last node
        if node.next is not None:
            node.next.prev = node.prev
        
        # Change prev only if node to be deleted is not first node
        if node.prev is not None:
            node.prev.next = node.next


def main():
    """Main function to demonstrate insert_after and delete_node"""
    dll = DoublyLinkedList()
    
    # Create initial nodes
    dll.head = Node(10)
    second = Node(20)
    third = Node(30)
    
    # Link nodes
    dll.head.next = second
    second.prev = dll.head
    second.next = third
    third.prev = second
    
    print("Initial list: 10 <-> 20 <-> 30")
    
    # Insert after second node
    dll.insert_after(second, 25)
    print("After inserting 25 after 20: 10 <-> 20 <-> 25 <-> 30")
    
    # Delete node with value 20
    dll.delete_node(second)
    print("After deleting 20: 10 <-> 25 <-> 30")


if __name__ == "__main__":
    main()