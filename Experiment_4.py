# my_str = "Hello this Is an Example With cased letters"


my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words of the sentence are:")
for word in words:
   print(word)
