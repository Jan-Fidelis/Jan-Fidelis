import  random
options=['rock','paper','scissors']
running=True 
while  running:
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("Enter choice(rock,paper,scissors):")
        print(f"computer:{computer}")
        print(f"player:{player}")
        if computer==player:
            print("it\'s a tie")
        elif (player=='rock' and computer=='scissors'):
            print("you win")
        elif(player=='paper' and computer=='rock'):
            print("you win:")
        elif(player=='scissors' and computer=='paper'):
            print("you win")
        else:
            print("you lose")
        if not input("Play again?(y/n):").lower()=='y':
            running=False
print("Thanks for playing, subscribe for more!!")
print("always check our site for more updates please.")
print("with love from the CsbossTech team❤.")
