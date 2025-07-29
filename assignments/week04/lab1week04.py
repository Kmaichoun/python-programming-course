"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    city = input("What city do you live in? ")
    country = input("Where are you from? ")
    person = ("Wave", 19, "Samutsakorn", "Thailand") 
    hobbies = []

    while True:
        print("\nMenu:")
        print("1. Display all information")
        print("2. Add hobby")
        print("3. Remove hobby")
        print("4. Update age")
        print("5. EXIT")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Name:", person[0])
            print("Age:", person[1])
            print("City:", person[2])
            print("Country:", person[3])
            print("Hobbies:", hobbies)
        elif choice == "2":
            hobby = input("Enter a hobby to add: ")
            hobbies.append(hobby)
            print("Hobby added.")
        elif choice == "3":
            if hobbies:
                print("Current hobbies:", hobbies)
                to_remove = input("Enter the hobby to remove: ")
                if to_remove in hobbies:
                    hobbies.remove(to_remove)
                    print("Hobby removed.")
                else:
                    print("Hobby not found.")
            else:
                print("No hobbies to remove.")
        elif choice == "4":
            person_list = list(person)
            age = int(input("Enter new age: "))
            person_list[1] = age
            person = tuple(person_list)
            print("Age updated.")
        elif choice == "5":
            print("Exiting Personal Information Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

if __name__ == "__main__":
    personal_info_manager()