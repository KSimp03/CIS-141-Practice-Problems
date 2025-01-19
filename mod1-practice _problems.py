# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water.Earth Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")


# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
user_input = float(input("Pick a number\n"))
num_input = int(input("Pick another number\n"))
#Additon
num_add = user_input + num_input
print("The sum of",user_input,"+",num_input,"is", num_add)
#num_divide
num_divide = user_input // num_input
print("The qoutient of", user_input,"/", num_input, "is", num_divide)
#num_product
num_product = user_input * num_input
print("The product of",user_input,"*",num_input,"is", num_product)
#num_subtract
num_subtract =  user_input - num_input
print("The differce of",user_input,"-",num_input,"is", num_subtract)

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
import math
print("Please insert the side measurements of the triangle:\n")
side_a = float(input("length of side a:"))
side_b = float(input("length of side b:"))
side_c = float(input("length of side c:"))
# Check if the inputs form a valid triangle
if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    # s = 1/2 ( a + b + c ) 
    s = (side_a + side_b + side_c) / 2
    area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    print("The area of the triangle is:", area)
else:
    print("This is not a valid triangle, try reinputting your numbers.")


# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
#Get users input
import math
print("Input your numbers to calculate total, average, minumum, maximum, range and standard deviation")
numbers = [
    float(input("First number:")),
    float(input("Next number:")),
    float(input("Next number:")),
    float(input("Next number:")),
    float(input("Next number:")),
    ]
#Calcutate total, average, minimum, maximum, range, and standard deviation
total = sum(numbers)
average = sum(numbers) // len(numbers)
minimum = min(numbers)
maximum = max(numbers)
range_val = minimum - maximum
#I had to look this part up I still dont quite understand standard deviation
variance = sum((x - average) * 2 for x in numbers) / len(numbers)
std_deviation = math.sqrt(variance)
#Print total, average, minimum, maximum, range, and standard deviation
print("\nTotal is", total)
print("Average is", average)
print("Minimum is:", minimum)
print("Maximum is:", maximum)
print("Range is:", range_val)
print("Standard deviation is:", std_deviation)
