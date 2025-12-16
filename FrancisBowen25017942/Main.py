
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

#open dictionary and had to use latin due to an error in utf-8
f=open("dictionary.txt","r",encoding="latin-1")
w=f.readlines()
f.close()

#beginning of my loop and checking length of word chosen
words=[]
for x in w:
    x=x.strip()
    if len(x)<=6:
        words.append(x)

tscore=0
rnd=1

while True:
    print("Round:",rnd,", Total Score =",tscore) # this shows score and round

    word=random.choice(words) # selects a random word under conditions I set(6 letters or less)

#shuffles the word
    letters=list(word)
    random.shuffle(letters)
    shuff=""
    for i in letters:
        shuff=shuff+i

    print("Shuffled word:",shuff)

    attempts=3
    guessed=False

    while attempts>0:
        g=input("Enter your guess: ")

        if g==word:
            sc=len(word)
            tscore=tscore+sc
            print("Congratulations! You guessed the word:",word,", Attempt Score",sc,", TotalScore",tscore,".")
            guessed=True
            break
        else:
            attempts=attempts-1
            if attempts>0:
                print("wrong guess! attempts left:", attempts)

    if guessed==False:
        print("Wrong! The correct word was:",word)
        print("(Actual word:",word+")")

    input("Press Enter For Next Round")

    rnd=rnd+1   