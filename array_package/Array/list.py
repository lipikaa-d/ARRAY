class ArrayOperations:
    def __init__(self):
        self.array = []
        self.element_type = None

    def create_array(self):
        self.array = []
        self.element_type = None

    def instantiating_array(self):
        array_ops = ArrayOperations()  # instantiating class
        array_ops.create_array()       # creating new list
        array_ops.array.extend(input("Enter elements separated by space: ").split())

    def insert_element(self):
        element = input("Enter the element to insert: ")
        try:
            if self.element_type is None:
                self.element_type = type(element)
            element = self.element_type(element)
        except (ValueError, TypeError):
            print("Error: Invalid element type")
            return

        if self.array and not all(isinstance(e, type(element)) for e in self.array):
            print("Error: All elements must be of the same type.")
            return

        position = input("Enter the position to insert at (leave empty to append): ")
        if position == "":
            self.array.append(element)
        else:
            position = int(position)
            if 0 <= position <= len(self.array):
                self.array.insert(position, element)
            else:
                print("Invalid position")

    def delete_element(self):
        if len(self.array) == 0:
            print("Array is empty")
            return

        position = int(input("Enter the position to delete from: "))
        if 0 <= position < len(self.array):
            removed_element = self.array.pop(position)
            print(f"Removed element: {removed_element}")
        else:
            print("Invalid position")

    def search_element(self):
        element = input("Enter the element to search for: ")
        if element in self.array:
            position = self.array.index(element)
            print(f"Element {element} found at position {position}")
        else:
            print(f"Element {element} not found in the array")

    def display_array(self):
        print("Current array:", self.array)

    def reverse_array(self):
        self.array.reverse()
        print("Array reversed")

    def delete_array(self):
        self.array = []
        print("Array deleted")

    def get_length(self):
        length = len(self.array)
        print(f"Length of the array: {length}")
