class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Add to the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Add to the front
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at index
    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        curr = self.head
        for i in range(index - 1):
            if not curr:
                raise IndexError("Index out of bounds")
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    # Remove by value
    def remove(self, data):
        curr = self.head
        prev = None
        while curr:
            if curr.data == data:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    # Remove at index
    def remove_at(self, index):
        curr = self.head
        prev = None
        for i in range(index):
            if not curr:
                raise IndexError("Index out of bounds")
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
        else:
            self.head = curr.next

    # Get size
    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    # Find (returns index)
    def find(self, data):
        curr = self.head
        idx = 0
        while curr:
            if curr.data == data:
                return idx
            curr = curr.next
            idx += 1
        return -1

    # Print all elements
    def print_list(self):
        curr = self.head
        elems = []
        while curr:
            elems.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elems))

    # Reverse the list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    # Clear the list
    def clear(self):
        self.head = None

# Example usage:
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.prepend(0)
# ll.print_list()
# ll.remove(1)
# ll.print_list()

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.print_list()