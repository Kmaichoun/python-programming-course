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
    person = ("Wave", 21, "Chonburi", "Thailand")  # name, age, city, country
    hobbies = []
    # Your code here

    #Display all information
    while True:
        print("\n1. Display all information.")
        print("2. Add new hobbies.")
        print("3. Remove hobbies.") 
        print("4. Update age.")
        print("5. Exit\n")
        choice = input("Choose option: ")
        if choice == "1":
            print("\nPersonal Information")
            print("Name: ", person[0])
            print("Age: ", person[1])
            print("City: ", person[2])
            print("country: ", person[3])
            print("Hobby: ")
            for i in range(len(hobbies)):
                print(hobbies[i])
    #Add new hobbie   
        elif choice == "2":
            hobby = input("\nWhat's your hooby :")
            hobbies.append(hobby)
    #Remove hobbies
        elif choice == "3":
         del hobbies[0]
    #Update age (by creating a new tuple)
        elif choice == "4":   
            person_list = list(person)
            age =int(input("\nHow old are you :"))
            person_list[1] = age
            person = tuple(person_list)
        elif choice == "5":
            break
        else:
            print("\nYour choice is worng.\nPlease Enter your choice again.")
            continue

if __name__ == "__main__":
    personal_info_manager()