"""
 Personal Finance Calculator
 Student: [Kritsana Maichoun]
 Date: [7/27/2025  ]
 Purpose: Calculate monthly budget and savings
"""

#input รับค่าเป็น float เเละ input ตามโจทย์
income = float(input("User's monthly income in THB: "))
rent_coat = float(input("Monthly rent/housing cost: "))
food_budget = int(input("Monthly food budget in THB: "))
transportation_cost = float(input("Monthly transportation expenses: "))
entertainment_budget = int(input("Monthly entertainment budget: "))
emergency_fund_percent = float(input("Percentage to save for emergency (e.g., 10.5): "))
investment_percent = float(input("Percentage to invest (e.g., 15.0): "))

#calculate เเยกเขียนระหว่างส่วนคำนวณเเละเเสดงผลจะได้ดูง่ายๆ 
fixexpenses = rent_coat + transportation_cost #คำนวณตั้งเเต่ line 23
variableexpenses = food_budget + entertainment_budget #24
totalexpenses = fixexpenses + variableexpenses #25
remainingincome = income - totalexpenses #26
emergencyfund = income * (emergency_fund_percent / 100) #28
investment = income * (investment_percent / 100) #29
saving = remainingincome - emergencyfund - investment #30
ratio = (totalexpenses / income) * 100 #32

#output display
#ใช้ f string จะได้เขียนสั้นๆเเละ format เลขได้
print("=== MONTHLY BUDGET REPORT ===")
print(f"Income: {income:.2f} บาท")
print(f"Total Fixed Expenses: {fixexpenses:.2f} บาท")
print(f"Total Variable Expenses: {variableexpenses:.2f} บาท")
print(f"Total Expenses: {totalexpenses:.2f} บาท")
print(f"Remaining Income: {remainingincome:.2f} บาท")
print("\n=== SAVING BREAKDOWN ===")
print(f"Emergency Fund Amount({emergency_fund_percent:.2f}%): {emergencyfund:.2f} บาท ")
print(f"Investment Amount({emergency_fund_percent:.2f}%): {investment:.2f} บาท ")
print(f"Avaliable for Savings: {saving:.2f} บาท")
print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {ratio:.2f}%")

