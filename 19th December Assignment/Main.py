
#load dictionary
print("loading dictionary", end=" ")
with open("dictionary.txt", "r", encoding="latin-1") as f:
    words = [w.strip() for w in f]
print("done")

#shows amound of words dictionary contains
print(f"Dictionary contains: {len(words)} words.")

#select words with 6 letters or less
print("selecting words with 6 letters or less", end="")
small_words = [w for w in words if len(w) <= 6]
print("done")

#number of words found
print(f"Found {len(small_words)} small words.")


import random

#load words
f = open("dictionary.txt", "r", encoding="latin-1")
w = f.readlines()
f.close
words=[]
for x in w:
    x=x.strip()
    if len(x)<=6:
        words.append(x)