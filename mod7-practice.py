#1. Write a function called count_vowels(input) that takes a string
#    and returns the number of vowels (a, e, i, o, u) in it.
def count_vowels(input):
    vowel_count = 0
    vowels = "aeiou"    
    for char in input.lower():  
        if char in vowels:  
            vowel_count += 1              
    return f"The vowel count is: {vowel_count}"  
# Test 
input1 = "waitress"
print(count_vowels(input1))  

#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
#    (reads the same forward and backward, ignoring case). The function should returns
#    either True or False.

def is_palindrome(s):
   lower_s = s.lower()
   flipped_s = lower_s[::-1]
   #print(flipped_s)
   return lower_s == flipped_s
print(is_palindrome("Mouse"))
print(is_palindrome("Madam"))
  
#3.
def type_advantage(attacker, defender):
    if attacker =="Water" and defender =="Fire":
        return "Super Effective"
    elif attacker == "Fire" and defender ==  "Water":
        return "Not Very Effective"
    elif attacker == "Electric" and defender == "Grass":
        return "Neutral"
advantage = type_advantage("Water","Fire")
advantage2 = type_advantage("Fire","Water")
advantage3 = type_advantage("Electric","Grass")
print("Water v. Fire is",advantage)
print("Fire v. Water is",advantage2)
print("Electric v. Grass is",advantage3)

#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
#    based on age and whether the person has a vehicle. Assume the following rates:
#    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
#    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
#    * Children (0-18): Free.

def ferry_fare(age, vehicle):
    if 19 <= age <= 64:  
        if vehicle:
            return "$20"
        else:
            return "$10"
    elif age >= 65: 
        if vehicle:
            return "$15"
        else:
            return "$5"
    elif 0 <= age <= 18: 
        return "Free"
print(ferry_fare(19, False))  
print(ferry_fare(30, True)) 
print(ferry_fare(65, False))  
print(ferry_fare(70, True))  
print(ferry_fare(10, False)) 

#5. Write a function called level_up(experience) that takes a player's experience points
#    and returns their new level based on these rules:
#    * 0-99 XP → Level 1
#    * 100-199 XP → Level 2
#    * 200+ XP → Level 3

def level_up(experience):
    if experience <= 99:
        return "level 1"
    elif 100 <= experience <= 199:
        return "level 2"
    elif experience >= 200:
        return "level 3"
#Test runs
print(level_up(12))
print(level_up(165))
print(level_up(205))
