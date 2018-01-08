#rolling dice
import random
c=(random.randint(1,100))
b=input("Input your choice between 1 to 100: ")
d=int(b)
if(c==d):
    print("Tie")
    print("Computers choice was: ",c)

elif(c>d):
    print("Computer Wins")
    print("Computers choice was: ",c)
    
elif(c<d):
    print("Human Wins")
    print("Computers choice was: ",c)
def cont():
    restart=input("Like to play again: ")
    if restart=='yes' or restart=='y':
        cont()

    if restart=="No" or restart=="n":
        print("Have a good day !")


cont()       
