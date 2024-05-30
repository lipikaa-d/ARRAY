from list import ArrayOperations
from sll import SingleLinkedList


def single_linked_list_application():
    sll = SingleLinkedList(element_type=str)

    # Insert initial elements
    while True:
        element = input("Enter an element to insert (or press Enter to finish): ")
        if element == "":
            break
        sll.insert(element)
        print(f"Inserted element: '{element}'")

    while True:
        print("\nChoose an operation:")
        print("1. Insert element")
        print("2. Delete element")
        print("3. Search element")
        print("4. Display list")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            element = input("Enter an element to insert: ")
            sll.insert(element)
        elif choice == '2':
            delete_element = input("Enter the element to delete: ")
            sll.delete_at_index(delete_element)
        elif choice == '3':
            search_element = input("Enter the element to search: ")
            node = sll.get(search_element)
            if node:
                print(f"Element '{search_element}' found in the single linked list.")
            else:
                print(f"Element '{search_element}' not found in the single linked list.")
        elif choice == '4':
            print("Elements of the single linked list:")
            print(sll.display())
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")


def array_operations_application():
    array_ops = ArrayOperations()
    array_ops.create_array()
    array_ops.array.extend(input("Enter elements separated by space: ").split())
    while True:
        print("\nChoose an operation:")
        print("1. Insert element")
        print("2. Delete element")
        print("3. Search element")
        print("4. Display array")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            array_ops.insert_element()
        elif choice == '2':
            array_ops.delete_element()
        elif choice == '3':
            array_ops.search_element()
        elif choice == '4':
            array_ops.display_array()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    print("Choose application to run:")
    print("1. Single Linked List Application")
    print("2. List as array")
    choice = input("Enter your choice: ")

    if choice == '1':
        single_linked_list_application()
    elif choice == '2':
        array_operations_application()
    else:
        print("Invalid choice, exiting.")
