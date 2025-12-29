import random
words=["kite","hair","flower","sunshine","glad","heroic","phylum","melon","shock","found"]
choice=random.choice(words)
guessed=["_"]*len(choice)
print(" ".join(guessed))
lives=6
while lives>0:
    userchoice=(input("guess the letter: "))
    if userchoice in choice:
        for index in range(len(choice)):
            if userchoice==choice[index]:
                guessed[index]=userchoice
                print(" ".join(guessed))
                break
    else:
        lives-=1
        print(f"wrong guess! take another guess now you only have {lives} guesses")
    if "_" not in guessed:
        print(f"CONGRATULATIONS! you guessed the word correctly {choice}")
    elif lives==0 and "_" in guessed:
        print("game over!! the word was ", choice)


