# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
print("Please insert a word:\n")
str1 = input()
print('How many times would you like to repeat"',str1,'"?\n')
#convert repeat into an integer
repeat = int(input())
print(str1 * repeat)

#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
print("Hello! What is your name?")
user_name = input()
print("Hi,",user_name,"what is your current age?")
user_age = int(input())
next_age = user_age + 1
print("Hello,",user_name,"! You are",user_age,"years old. Next year you will be",next_age,"years old!")

#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
print("Provide me with a sentence\n")
str1 = input()
word = input("What word am I looking for in this sentence:\n")
print(word in str1)

#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
word = input("Please enter a word:\n")
first_index = int(input("Enter the first index:"))
last_index = int(input("Enter the last index:"))
sliced_word = word[first_index:last_index + 1]
print("The sliced word is:", sliced_word)

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
print("cat","rat","hat", sep ="|")
