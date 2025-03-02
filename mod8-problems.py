#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
#Write a Python script that reads a file gardening_tips.txt and prints out each tip one by one.
# Create and write to the file
with open("gardening_tips.txt", "w") as file:
    file.write("1. Water your plants early in the morning or late in the evening to prevent evaporation.\n")
    file.write("2. Use compost to enrich your soil and promote healthy plant growth.\n")
    file.write("3. Plant flowers that attract pollinators like bees and butterflies.\n")
# Read and print each tip one by one
with open("gardening_tips.txt", "r") as file:
    for line in file:
        print(line, end = "")
#2. Write a Python program that allows users to log their hiking trips. The program should:
#Use a while loop to repeatedly ask for a hike name and distance in miles
# Save each entry to hiking_log.txt (each hike on a new line)
#When the user presses 0, exit the loop & print the contents of hiking_log.txt

#create file
#'a'= append
with open ("hiking_trips.txt", "a") as file:
    while True:
        hike_name = input("Please enter a hike name (press 0 to exit):\n")
        hike_dis = input("Please enter your hike's distance in miles (press 0 to exit):\n")
        if hike_dis == '0':
            break
        if hike_name and hike_dis:
            file.write(f"{hike_name} - {hike_dis} miles\n")
            file.flush()
with open("hiking_trips.txt","r") as file:
    print("\nHiking Log:")
    print(file.read())

#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
#Requests 5 inputs from the user: 5 words the user would like to count the frequency of
#Counts how many times each word appears
#Creates a dictionary of the words and their counts
#Print the dictionary to the console
#I chose party in the USA  
#Reads the file
with open("song_lyrics.txt",'r') as file:
   lyrics = file.read().lower() 
   print(lyrics)
#Ask the user to pick 5 words to count
pick = input("Choose a word to count in the song:\n").lower()
pick1 = input("Choose a word to count in the song:\n").lower()
pick2 = input("Choose a word to count in the song:\n").lower()
pick3 = input("Choose a word to count in the song:\n").lower()
pick4 = input("Choose a word to count in the song:\n").lower()
 
words = lyrics.split()
word_count = {
    pick: words.count(pick),
    pick1:words.count(pick1),
    pick2:words.count(pick2),
    pick3:words.count(pick3),
    pick4:words.count(pick4),
    }
print("\nWord Frequency Count:")
print(word_count) 

#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
#Write a program that reads the poll.txt file... Count how many votes "yea" or "nay" received and print the results.
#poll.txt contained "yea,nay,yea,nay,nay,nay,yea,nay,nay,nay,nay,yea"
with open("poll.txt", "r") as file:
    results = file.read()
votes = results
# Count "yea" and "nay"
yea_count = votes.count("yea")
nay_count = votes.count("nay")
# Print the results
print(f"Yea votes: {yea_count}")
print(f"Nay votes: {nay_count}")
