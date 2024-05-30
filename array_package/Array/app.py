from sll import SingleLinkedList


def single_linked_list_application():
    # Determine the type of elements
    element_type_input = input("Enter the type of elements (int/str): ").strip()
    if element_type_input == 'int':
        element_type = int
    elif element_type_input == 'str':
        element_type = str
    else:
        print("Unsupported element type")
        return

    # Initializing linked list
    sll = SingleLinkedList(element_type)

    num_elements = int(input("Enter the number of elements to insert: "))

    print("Enter the elements:")
    for _ in range(num_elements):
        element = input("Element: ")
        element = element_type(element)
        sll.insert(element)

    # Display
    print("Elements of the single linked list:")
    print(sll.display())

    # Input
    index_to_insert = int(input("Enter the index at which to insert a new element: "))
    element_to_insert = input("Enter the element to insert: ")
    element_to_insert = element_type(element_to_insert)
    try:
        sll.insert_at_index(index_to_insert, element_to_insert)
        print(f"Inserted element '{element_to_insert}' at index {index_to_insert}")
    except IndexError as e:
        print(e)

    # Display after insert
    print("Elements after insertion:")
    print(sll.display())

    # Input for deletion
    index_to_delete = int(input("Enter the index of the element to delete: "))
    try:
        sll.delete_at_index(index_to_delete)
        print(f"Deleted element at index {index_to_delete}")
    except IndexError as e:
        print(e)

    # Display after delete
    print("Elements after deletion:")
    print(sll.display())

    # Input for search
    index_to_get = int(input("Enter the index of the element to get: "))
    try:
        element_at_index = sll.get(index_to_get)
        print(f"Element at index {index_to_get} is '{element_at_index}'")
    except IndexError as e:
        print(e)

    # Input for setting a value
    index_to_set = int(input("Enter the index of the element to set: "))
    new_value = input("Enter the new value: ")
    new_value = element_type(new_value)
    try:
        sll.set(index_to_set, new_value)
        print(f"Set element at index {index_to_set} to '{new_value}'")
    except IndexError as e:
        print(e)

    # Display after setting
    print("Elements after setting new value:")
    print(sll.display())


if __name__ == "__main__":
    single_linked_list_application()
