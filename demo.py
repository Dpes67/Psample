import random
def my_hand():
    hand=input("enter rock, paper or scissors?\n")
    return hand

def computer_choice():
    list=['rock','paper','scissors']
    choice=random.choice(list)
    print(choice)
    return choice

def determine_winnner(hand,choice):
    if hand==choice:
        print("its fokin tie")
    elif (
         (hand=='rock' and choice=='scissors')or
         (hand=='paper' and choice=='rock')or
         (hand=='scissors' and choice=='paper')
    ):
        return"you win"
    else:
        return"you lose"

while True:
    a=my_hand()
    b=computer_choice()
    print(f"you choose {a} and computer choose {b}")
    result=determine_winnner(a,b)
    print(result)

    if result=="you win":
        break









