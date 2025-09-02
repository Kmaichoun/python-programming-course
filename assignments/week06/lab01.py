""" เขียน function ชื่อ welcome_message ที่มีคุณสมบัติดังนี้:

รับ parameter 2 ตัว คือ name และ course
return ข้อความต้อนรับในรูปแบบ string
รูปแบบ: "Welcome [name] to [course] class!"

"""
def welcome_message(name, course):
    return f"Welcome {name} to {course} class!"

""" เขียน function ชื่อ calculate_circle ที่มีคุณสมบัติดังนี้:

รับ parameter 1 ตัว คือ radius
return dictionary ที่มี area และ circumference
ใช้ค่า π = 3.14159
ปัดเศษทั้งสองค่าให้เหลือ 2 ตำแหน่งหลังจุดทศนิยม """

def calculate_circle(radius):
    pi = 3.14159
    area = pi * radius * radius, 
    circumference = 2 * pi * radius
    return {"area": area, "circumference": circumference}

""" เขียน function ชื่อ create_user_profile ที่มีคุณสมบัติดังนี้:

รับ parameters: username (จำเป็น), age (ค่าเริ่มต้น 18), premium (ค่าเริ่มต้น False)
return string ที่จัดรูปแบบข้อมูลผู้ใช้
รูปแบบ: "[username] (age: [age]) - [Premium User / Standard User]"

"""

def create_user_profile(username, age=18, premium=False):
    status = "Premium User" if premium else "Standard User"
    return f"{username} (age: {age}) - {status}"
""" เขียน function ชื่อ analyze_scores ที่มีคุณสมบัติดังนี้:

รับ list ของคะแนน (ตัวเลข)
return dictionary ที่มี:

total: ผลรวมของคะแนนทั้งหมด
average: คะแนนเฉลี่ย (ปัดเศษ 1 ตำแหน่งหลังจุดทศนิยม)
highest: คะแนนสูงสุด
lowest: คะแนนต่ำสุด
passed: จำนวนคะแนนที่ >= 70 """
def analyze_scores(scores):
    total = sum(scores)
    average = round(total / len(scores))
    highest = max(scores) if scores else None
    lowest = min(scores) if scores else None
    passed = sum(1 for s in scores if s >= 70)
    return {
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed
    }

def count_vowels_consonants(text):
    vowels_set = set('aeiou')
    vowels = 0
    consonants = 0
    for char in text.lower():
        if char.isalpha():
            if char in vowels_set:
                vowels += 1
            else:
                consonants += 1
    return {"vowels": vowels, "consonants": consonants}

def count_vowels_consonants(text):
    
    text.lower()
    text.replace(" ","")
    text.replace("0","")
    text.replace("1","")
    text.replace("2","")
    text.replace("3","")
    text.replace("4","")
    text.replace("5","")
    text.replace("6","")
    text.replace("7","")
    text.replace("8","")
    text.replace("9","")

    vowels = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
    consonants = len(text) - vowels
    return {"vowels": vowels, "consonants": consonants}
    # Your Problem 5 solution
    pass

# =============================================================================
# TEST SECTION - DO NOT MODIFY
# =============================================================================

def run_all_tests():
    """Test all functions and display results"""
    print("="*50)
    print("PYTHON FUNCTIONS QUIZ - TEST RESULTS")
    print("="*50)
    
    # Test Problem 1
    print("\n--- Problem 1 Tests ---")
    try:
        result1 = welcome_message("Alice", "Python")
        print(f"Test 1: {result1}")
        result2 = welcome_message("Bob", "Data Science")
        print(f"Test 2: {result2}")
        print("✓ Problem 1: PASSED")
    except Exception as e:
        print(f"✗ Problem 1: ERROR - {e}")
    
    # Test Problem 2
    print("\n--- Problem 2 Tests ---")
    try:
        result1 = calculate_circle(5)
        print(f"Test 1: {result1}")
        result2 = calculate_circle(3)
        print(f"Test 2: {result2}")
        print("✓ Problem 2: PASSED")
    except Exception as e:
        print(f"✗ Problem 2: ERROR - {e}")
    
    # Test Problem 3
    print("\n--- Problem 3 Tests ---")
    try:
        result1 = create_user_profile("john_doe")
        print(f"Test 1: {result1}")
        result2 = create_user_profile("alice", 25)
        print(f"Test 2: {result2}")
        result3 = create_user_profile("bob", 30, True)
        print(f"Test 3: {result3}")
        print("✓ Problem 3: PASSED")
    except Exception as e:
        print(f"✗ Problem 3: ERROR - {e}")
    
    # Test Problem 4
    print("\n--- Problem 4 Tests ---")
    try:
        scores1 = [85, 92, 78, 65, 88, 76, 95]
        result1 = analyze_scores(scores1)
        print(f"Test 1: {result1}")
        scores2 = [45, 67, 89, 72, 58]
        result2 = analyze_scores(scores2)
        print(f"Test 2: {result2}")
        print("✓ Problem 4: PASSED")
    except Exception as e:
        print(f"✗ Problem 4: ERROR - {e}")
    
    # Test Problem 5
    print("\n--- Problem 5 Tests ---")
    try:
        result1 = count_vowels_consonants("Hello Worldoooooo")
        print(f"Test 1: {result1}")
        result2 = count_vowels_consonants("Python Programming 2024")
        print(f"Test 2: {result2}")
        print("✓ Problem 5: PASSED")
    except Exception as e:
        print(f"✗ Problem 5: ERROR - {e}")
    
    print("\n" + "="*50)
    print("END OF TESTS")
    print("="*50)
    

# Run the tests
if __name__ == "__main__":
    run_all_tests()