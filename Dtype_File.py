def string_example():
    print("\nSTRING EXAMPLE")
    text = input("Enter a word: ")
    print(f"You entered: {text}")
    print(f"Uppercase: {text.upper()}")
    print("")

def integer_example():
    print("\nINTEGER EXAMPLE")
    number = int(input("Enter a whole number: "))
    print(f"You entered: {number}")
    print(f"Double: {number * 2}")
    print("")

def float_example():
    print("\nFLOAT EXAMPLE")
    number = float(input("Enter a decimal number: "))
    print(f"You entered: {number}")
    print(f"Half: {number / 2}")
    print("")

def list_example():
    print("\nLIST EXAMPLE")
    items = input("Enter a few words separated by commas: ").split(",")
    print(f"You entered: {items}")
    print(f"First item: {items[0] if items else 'None'}")
    print("")

def dict_example():
    print("\nDICTIONARY EXAMPLE")
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    my_dict = {key: value}
    print(f"You created: {my_dict}")
    print("")

def boolean_example():
    print("\nBOOLEAN EXAMPLE")
    answer = input("Is Python fun? (yes/no): ").strip().lower()
    is_fun = answer == "yes"
    print(f"Python is fun: {is_fun}")
    print("")

def main():
    while True:
        print("\nMENU")
        print("1. String")
        print("2. Integer")
        print("3. Float")
        print("4. List")
        print("5. Dictionary")
        print("6. Boolean")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")
        
        if choice == "1":
            string_example()
        elif choice == "2":
            integer_example()
        elif choice == "3":
            float_example()
        elif choice == "4":
            list_example()
        elif choice == "5":
            dict_example()
        elif choice == "6":
            boolean_example()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()
