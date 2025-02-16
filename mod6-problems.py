#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
num_list = [1,2,3,4,5,6,7,8,9]
num_sum = num_list[1] + num_list[3] + num_list[5] + num_list[7]
print("the sum of the even numbers (1 - 9) is:",num_sum)

#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.
str_list = ["Olympic", "Dog", "lotion", "waterbottle", "keyboard", "Olympic"]
counter = 0
print(str_list)
for i in str_list:
    if i == "Olympic":
        counter += 1
print("Olymic appears",counter,"time(s)")
    
#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.
words = ["at", "rat", "beads", "on", "chicken"]
print("Original words:", words)
new_words = []
for i in words:
    if len(i) > 3:
        new_words.append(i)
print("Words with more than 3 characters:", new_words)

#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.
num = [-1,4,-89, 13,43]
print("List:",num)
neg = []
posi = []
for n in num:
    if n > 0:
        posi.append(n)
    elif n < 0:
        neg.append(n)
print("There are:", len(posi), "positive numbers")
print("There are:", len(neg), "negative numbers")

#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.
nums = [8,5,1,3]
print("List:",nums)
sq_num = []
for i in nums:
    sq_num.append(i**2)
print("List numbers squared:",sq_num)
