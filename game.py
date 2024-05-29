#Rock, Paper, Scissor game

from tkinter import*
import random

def generate_computer_choice():
    computer_choice = random.randint(0, 2)
    return computer_choice

def result():
    stri=entry.get()
    u=int(stri)
    c=generate_computer_choice()
    computer_choice_label=Label(root,text=f"Computer's Choice: {str(c)}")
    computer_choice_label.grid(row=3,column=0,padx=20,pady=20)


    if (u>2 or u<0):
        myLabel=Label(root,text="You entered a wrong no.!")
        myLabel.grid(row=4,column=0,columnspan=4,padx=20, pady=20)
    elif(c==u):
         myLabel=Label(root,text="It's a tie!", bg="blue")
         myLabel.grid(row=4,column=0,columnspan=4,padx=20, pady=20)
    elif(c>u):
        if(c==2):
            myLabel=Label(root,text="You win!", bg="green")
            myLabel.grid(row=4,column=0,columnspan=4,padx=20, pady=20)
        else:
            myLabel=Label(root,text="You lose!", bg="red")
            myLabel.grid(row=4,column=0,columnspan=4,padx=20, pady=20)
    else:
        if(c==0):
            myLabel=Label(root,text="You lose!", bg="red")
            myLabel.grid(row=4,column=0,columnspan=4,padx=20, pady=20)
        else:
            myLabel=Label(root,text="You win!", bg="green")
            myLabel.grid(row=4,column=0,columnspan=4,padx=20, pady=20)

        


root=Tk()
root.title("Game")
guidelines="RULES:\n1. Rock beats scissor.\n2. Scissor beats paper.\n3. Paper beats rock.\nCHOICES:\n0=ROCK\n1=PAPER\n2=SCISSOR\n"
guide=Label(root,text=guidelines)
guide.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

label = Label(root, text="Enter your choice:")
label.grid(row=1, column=0, padx=10, pady=10)

entry = Entry(root, width=30, borderwidth=5)
entry.grid(row=1, column=1, padx=10, pady=10)

myButton=Button(root,text="Submit", command=result)
myButton.grid(row=2,column=1, columnspan=4,padx=20, pady=20)

root.mainloop()