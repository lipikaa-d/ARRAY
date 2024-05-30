class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self, element_type):
        self.head = None
        self.element_type = element_type

    def insert(self, data):
        if not isinstance(data, self.element_type):
            raise TypeError(f"All elements must be of type {self.element_type.__name__}")

        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_index(self, index, data):
        print(f"Debug: Attempting to insert '{data}' at index {index}")
        if not isinstance(data, self.element_type):
            raise TypeError(f"All elements must be of type {self.element_type.__name__}")

        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1

        if not current:
            raise IndexError("Index out of range")

        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, data):
        print(f"Debug: Attempting to delete '{data}' from the list.")
        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if not current:
            print(f"Element '{data}' not found in the list.")
            return

        if prev:
            prev.next = current.next
        else:
            self.head = current.next
        print(f"Debug: List after deletion: {self.display()}")

    def get(self, data):
        print(f"Debug: Attempting to get element '{data}'")
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

