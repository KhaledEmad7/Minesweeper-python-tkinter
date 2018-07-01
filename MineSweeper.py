from tkinter import *
from tkinter import messagebox
from random import *

win = Tk()

difficulty = input("Please pick a difficulty: Easy, Medium, or Hard. \n")

# rows,columns,number of bombs
g = h = 9
if difficulty == "Easy":
    NumberOfBombs = 10
elif difficulty == "Medium":
    NumberOfBombs = 20
else:
    NumberOfBombs = 30

#opening images
Bomb = PhotoImage(file = "bomb.png")
Flag2 = PhotoImage(file = "flagged.png")
normal = PhotoImage(file = "facingDown.png")
Blank = PhotoImage(file = "0.png")
one = PhotoImage(file = "1.png")
two = PhotoImage(file = "2.png")
three = PhotoImage(file = "3.png")
four = PhotoImage(file = "4.png")
five = PhotoImage(file = "5.png")



#Createing the main list
L =[[0 for n in range(g+1)] for n in range(h+1)]
L2 = [[0 for n in range(g+1)] for n in range(h+1)]
Values = [0,1,2,3,4,5]



#Inserting bombs
for k in range(NumberOfBombs):
    a= randint(0,9)
    b= randint(0,9)
    if L[a][b] != 9:
        L[a][b]=9


#Counting bombs arround a square
for x in range(g+1):
    for y in range(h+1):
        if L[x][y] ==9:
            if x<g:
                if L[x+1][y] != 9:
                    L[x+1][y]+=1
            if x>=1:
                if L[x-1][y] != 9:
                    L[x-1][y]+=1
            if y<h:
                if L[x][y+1] != 9:
                    L[x][y+1]+=1
            if y>=1:
                if L[x][y-1] != 9:
                    L[x][y-1]+=1
            if x<g and y<h:
                if L[x+1][y+1] != 9:
                    L[x+1][y+1] +=1
            if x>=1 and y<h:
                if L[x-1][y+1] != 9:
                    L[x-1][y+1]+=1
            if x<g and y>=1:
                if L[x+1][y-1] != 9:
                    L[x+1][y-1]+=1
            if x>=1 and y>=1:
                if L[x-1][y-1] != 9:
                    L[x-1][y-1]+=1


#Changing rows with columns so that it can fit with the dictionary
Transpose = [[L[j][i] for j in range(len(L))] for i in range(len(L[0]))]

#Getting all numbers of the list in a string
x = ""
for i in Transpose:
    z = "".join(str(f) for f in i)
    x += z

#for i in L:
    #print(i)

#Open all boxes
def OpenAll():
    c = 0
    for i in w.values():
        if int(x[c]) == 9:
            i.configure(image = Bomb , width = "30", height = "30")
        else:
            image(i, int(x[c]))
        c+=1


# opening images
def image(x,y):

    if x in w.values():
        if y == 1:
            x.configure(image = one , width = "30", height = "30")
        elif y == 2:
            x.configure(image = two , width = "30", height = "30")
        elif y == 3:
            x.configure(image = three , width = "30", height = "30")
        elif y == 4:
            x.configure(image = four , width = "30", height = "30")
        elif y == 5:
            x.configure(image = five , width = "30", height = "30")
        elif y == 0:
            x.configure(image = Blank , width = "30", height = "30")
    else:
        if y == 1:
            x.widget.configure(image = one , width = "30", height = "30")
        elif y == 2:
            x.widget.configure(image = two , width = "30", height = "30")
        elif y == 3:
            x.widget.configure(image = three , width = "30", height = "30")
        elif y == 4:
            x.widget.configure(image = four , width = "30", height = "30")
        elif y == 5:
            x.widget.configure(image = five , width = "30", height = "30")
        elif y == 0:
            x.widget.configure(image = Blank , width = "30", height = "30")




#Opening all zeroes around a box that have zero value
def RemoveZeroes(i,j):
    try:
        image(w[str(j+1),str(i)], L[i][j+1])
        image(w[str(j+1),str(i+1)], L[i+1][j+1])
        image(w[str(j+1),str(i-1)], L[i-1][j+1])
        image(w[str(j-1),str(i-1)], L[i-1][j-1])
        image(w[str(j-1),str(i)], L[i][j-1])
        image(w[str(j-1),str(i+1)], L[i+1][j-1])
        image(w[str(j),str(i+1)], L[i+1][j])
        image(w[str(j),str(i-1)], L[i-1][j])

    except KeyError:
        pass



#Adding Flags
def Flag(event, index):
    i = index[1]
    j = index[0]
    if L2[i][j] == "Flag":
        L2[i][j] = L[i][j]
        event.widget.configure(image = normal , width = "30", height = "30")

    else:
        L2[i][j] = "Flag"
        event.widget.configure(image = Flag2 , width = "30", height = "30")



#This function works when a button is clicked
def ClickMe(event, index):
    i = index[1]
    j = index[0]


    if L[i][j] != 9 and L[i][j] != 0 and L2[i][j] != "Flag":
        image(event, (L[i][j]))


    elif L[i][j] == 0 and L2[i][j] != "Flag":

        try:
            image(event, L[i][j])
            image(w[str(j+1),str(i)], L[i][j+1])
            if L[i][j+1] == 0:
                RemoveZeroes(i,j+1)
        except KeyError:
            pass

        try:
            image(w[str(j+1),str(i+1)], L[i+1][j+1])
            if L[i+1][j+1] == 0:
                RemoveZeroes(i+1,j+1)
        except KeyError:
            pass

        try:
            image(w[str(j+1),str(i-1)], L[i-1][j+1])
            if L[i-1][j+1] == 0:
                RemoveZeroes(i-1,j+1)
        except KeyError:
            pass

        try:
            image(w[str(j-1),str(i-1)], L[i-1][j-1])
            if L[i-1][j-1] == 0:
                RemoveZeroes(i-1,j-1)
        except KeyError:
            pass

        try:
            image(w[str(j-1),str(i)], L[i][j-1])
            if L[i][j-1] == 0:
                RemoveZeroes(i,j-1)
        except KeyError:
            pass

        try:
            image(w[str(j-1),str(i+1)], L[i+1][j-1])
            if L[i+1][j-1] == 0:
                RemoveZeroes(i+1,j-1)
        except KeyError:
            pass

        try:
            image(w[str(j),str(i+1)], L[i+1][j])
            if L[i+1][j] == 0:
                RemoveZeroes(i+1,j)
        except KeyError:
            pass
        
        try:
            image(w[str(j),str(i-1)], L[i-1][j])
            if L[i-1][j] == 0:
                RemoveZeroes(i-1,j)
        except KeyError:
            pass


    elif L[i][j] and L2[i][j] != "Flag":
        event.widget.configure(image = Bomb, width = "10", height = "10")
        OpenAll()
        messagebox.showinfo("Ops","You lost")



#Creating buttons
w={}
#for i in L:
    #print(i)
for i in range(g+1):
    for j in range(h+1):
        action = Button(win, image = normal , width = "30", height = "30")
        action.bind("<Button-1>", lambda event, index=[i, j] : ClickMe(event , index))
        action.bind("<Button-3>", lambda event, index=[i, j] : Flag(event , index))
        action.grid(column=i, row=j)
        w[str(i),str(j)]=action


win.mainloop()
