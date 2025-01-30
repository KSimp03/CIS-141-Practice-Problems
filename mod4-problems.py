#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False. Your truth table should be commented out (as it's not valid Python code!)
#And Operation
# A    B        A and B
# ----------------------
#True True      True
#False False    False
#False True     False
#True False     False

#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".
daylight = int(input("What is the senor number?\n"))
if daylight >= 8:
    print("Headlights on")
elif daylight < 8:
    print("Headlights off")

#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. Print True if the user’s balance is below $100; print False, otherwise.
balance = int(input("What is your current balance?\n$"))
if balance >= 100:
    print("True")
elif balance < 100:
    print("False")

#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
age = int(input("How old are you?\n"))
if age >= 18:
    print("You can watch G, PG-13, and R rated movies.")
elif age <=13  or age < 18:
    print("You can watch G and PG-13.")
elif age <= 13:
    print("You can watch G rated movies.")

#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.
print("Orders that are $50 and above will have free shipping!")
total = int(input("What was your total today?\n$"))
if total >= 50:
    print("Your total today will be $",total,"\nThank you for shopping with us!")
elif total < 50: 
    print("Your total today will be $", total + 5, "\nThank you for shopping with us!")
