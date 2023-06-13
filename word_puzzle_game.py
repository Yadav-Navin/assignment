import random

def word_puzzle_game():
    # we create a list
    list1=["ppale","sparg","ananba","rutht","ssech","eykobadr","ekatsmi","manhu","manwo"]
    list2=["apple","graps","banana","truth","chess","keyboard","mistake","human","woman"]

    # here wrong can contain wrong point
    wrong=0
    
    # here correct can contain correct point
    correct=0

    j=1
    i=0

    #while loop executes five times
    while i<5:
        print("\"Arrange the letters to form a valid word\"")
        print("{}.".format(j),list1[random.randint(0,len(list1)-1)])
        s=input()
        if s in list2:
            #correct variable can contain correct point
            correct+=1
            print("\nCorrect")
        else:
            #wrong variable can contain wrong point
            wrong+=1
            print("\nWrong")
        i+=1
        j+=1

    print("\ncorrect word is",correct)#display correct point
    print("wrong word is",wrong)#display wrong point
    print("\ncorrect weightage is {}%".format(correct*100/5))#display correct percentage

word_puzzle_game()
