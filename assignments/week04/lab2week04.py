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
        num = int(input(f"Enter number [{i+1}]: "))
        numbers.append(num)
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = []
    odd_numbers = []
    
    # Calculate average
    average = sum(numbers) / len(numbers)
    
    # Numbers greater than average
    above_average = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
        if num > average:
            above_average.append(num)
    # Display results
    print(f"\nSum: {sum(numbers)}")
    print(f"Average: {average}")
    print(f"Min: {min(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"List of even numbers : {even_numbers}")
    print(f"List of odd numbers : {odd_numbers}")
    print(f"List of numbers greater than the average : {above_average}\n")
    
if __name__ == "__main__":
    number_operations()