import random

def suffleword(word):
    #here we can change given word character position throught random.sample().
    #random.sample() method return list of string
    list_of_string=random.sample(word,k=len(word))
    return ''.join(list_of_string)

def puzzle(word,score):
    #suffleword function suffle the given word
    sufferedWord = suffleword(word)

    print("Arrenge the given word")
    print(sufferedWord)

    #user enter right word for this given puzzle.
    userInput = input()

    #here we can check user entered word right or not.
    if userInput.upper() == word:
        score+=1
        print("\ncorrect\n")
    else:
        score-=1
        print("\nWrong\n")

    return score
        
def main():
    score = 0
    words=["APPLE","GRAPS","BANANA","CHESS","WOMEN"]

    #random.sample return suffered list they does not change the list only change list element position
    words = random.sample(words,k=len(words))
    for wrd in words:
        score=puzzle(wrd,score)
    
    print("Your score is",score)

main()

