"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        n = int(input("Enter your numbers :"))# Your code here
        numbers.append(n)
        pass
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = []# Your code here
    odd_numbers = []# Your code here
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
        else:
            odd_numbers.append(n)


    # Calculate average
    average = sum(numbers)/len(numbers)# Your code here
    
    # Numbers greater than average
    above_average = []# Your code here ค่าที่มากกว่าค่าเฉลี่ย
    for n in numbers:
        if n > average:
            above_average.append(n)
    # Display results
    # Your code here
    print(f"\nSum: {sum(numbers)}")
    print(f"Average: {average}")
    print(f"Min: {min(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"List of even numbers : {even_numbers}")
    print(f"List of odd numbers : {odd_numbers}")
    print(f"List of numbers greater than the average : {above_average}\n")
    
if __name__ == "__main__":
    number_operations()