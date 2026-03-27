from insured_person import InsuredPerson
from insurance_manager import InsuranceManager

def main():
    manager = InsuranceManager()

    while True:
        print("\n--- Insurance Registry ---")
        print("1. Add insured person")
        print("2. Show all insured people")
        print("3. Find insured person")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            # add insured person
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            age = input("Enter age: ")
            phone_number = input("Enter phone number: ")

            # checking if the person was added to the list, if yes, add him to the list;
            # if not, raise a ValueError based on conditions in insured_person file
            try:
                person = InsuredPerson(first_name, last_name, age, phone_number)
                manager.add_insured_person(person)
                print("Insured person added successfully. Press any key to continue...")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            # show all insured people using a cycle
            people = manager.get_insured_people()
            if not people:
                print("No insured people found.")
            else:
                print("\n--- List of insured people ---")
                for person in people:
                    print(person)
            print("\nPress any key to continue")

        elif choice == "3":
            # find insured person based on first and last name
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            found = manager.find_insured_person(first_name, last_name)
            if found:
                print("\nPerson found:")
                print(found) # the found object is automatically displayed via set __str__
            else:
                print("No matching person found.")
            print("\nPress any key to continue")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

# run the program only with the command "python main.py" and avoid running when main() is imported in different file
if __name__ == "__main__": # __main__ is a special value/name for main file from
                        # which the program runs (it also can be file called "program.py" not only "main.py")
    main()
