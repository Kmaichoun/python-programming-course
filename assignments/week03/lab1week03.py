# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

if age >= 60:
    print("You're Senior")
elif age >= 20:
    print("You're Adult")
elif age >= 13:
    print("You're Teenager")
elif age >= 0:
    print("You're Child")
else:
    print("Invalid age")