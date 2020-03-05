from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("TIC TAC FUCKTIN TOE")
click = True
root.configure(background = "#777E8B" )


def restart():                                                                                                          
    global  click, score1 , score2
    button1['text'] = ' '
    button2['text'] = ' '
    button3['text'] = ' '
    button4['text'] = ' '
    button5['text'] = ' '
    button6['text'] = ' '
    button7['text'] = ' '
    button8['text'] = ' '
    button9['text'] = ' '
    click = True
    checkActual()
    
score1 = 0 
score2 = 0 
p1Label = Label( root , text =" Player 1" , font =("Verdana",18) , bg = "#777E8B" ).grid(row = 0 ,column = 0 )
p2Label = Label( root , text =" Player 2" , font =("Verdana",18),bg = "#777E8B" ).grid(row = 1 ,column = 0 )

p1Entry = Entry(root , bd = 5  ,width = 10 )
p1Entry.grid( row = 0 , column = 1 )
p1Entry.insert(0,score1)

p2Entry = Entry(root , bd = 5  ,width = 10)
p2Entry.grid( row = 1 , column = 1 )
p2Entry.insert(0,score2)


def checkWinWin():
    if (button1[ 'text' ] == 'O' and button2[ 'text' ] == 'O'  and button3[ 'text' ] == 'O'  or
    button1[ 'text' ] == 'O' and button4[ 'text' ] == 'O'  and button7[ 'text' ] == 'O'  or
    button1[ 'text' ] == 'O' and button5[ 'text' ] == 'O'  and button9[ 'text' ] == 'O'  or
    button3[ 'text' ] == 'O' and button6[ 'text' ] == 'O'  and button9[ 'text' ] == 'O'  or
    button7[ 'text' ] == 'O' and button8[ 'text' ] == 'O'  and button9[ 'text' ] == 'O'  or
    button2[ 'text' ] == 'O' and button5[ 'text' ] == 'O'  and button8[ 'text' ] == 'O'  or
    button4[ 'text' ] == 'O' and button5[ 'text' ] == 'O'  and button6[ 'text' ] == 'O'  ) :
        return True
    
    elif (button1[ 'text' ] == 'X' and button2[ 'text' ] == 'X'  and button3[ 'text' ] == 'X'  or
    button1[ 'text' ] == 'X' and button4[ 'text' ] == 'X'  and button7[ 'text' ] == 'X'  or
    button1[ 'text' ] == 'X' and button5[ 'text' ] == 'X'  and button9[ 'text' ] == 'X'  or
    button3[ 'text' ] == 'X' and button6[ 'text' ] == 'X'  and button9[ 'text' ] == 'X'  or
    button7[ 'text' ] == 'X' and button8[ 'text' ] == 'X'  and button9[ 'text' ] == 'X'  or
    button2[ 'text' ] == 'X' and button5[ 'text' ] == 'X'  and button8[ 'text' ] == 'X'  or
    button4[ 'text' ] == 'X' and button5[ 'text' ] == 'X'  and button6[ 'text' ] == 'X'  ) :
        return True
    elif ((button1[ 'text' ] == 'X' or button1[ 'text' ] == 'O'  )and (button2[ 'text' ] == 'X'  or
           button2[ 'text' ] == 'O' )and( button3[ 'text' ] == 'X'  or button3[ 'text' ] == 'O') and
         ( button4[ 'text' ] == 'X' or button4[ 'text' ] == 'O')  and (button5[ 'text' ] == 'X'  or
           button5[ 'text' ] == 'O' )and( button6[ 'text' ] == 'X'  or button6[ 'text' ] == 'O') and
         ( button7[ 'text' ] == 'X' or button7[ 'text' ] == 'O' ) and (button8[ 'text' ] == 'X'  or
          button8[ 'text' ] == 'O' )and( button9[ 'text' ] == 'X'  or button9[ 'text' ] == 'O') ):
        messagebox.showinfo("Nobody Wins","No Winner Bitches")
        restart()
        return False
    
def buttonClicked(buttons):
    global click , score1 , score2 
    if buttons['text'] == ' ' and click == True:
        buttons['text'] = 'X'
        click = False
        if checkWinWin() :
            messagebox.showinfo("Damn boy!","You Made it")
            score1 += 1
            p1Entry.delete(0,END)
            p1Entry.insert(0,score1)
            restart()
       
            
    elif buttons['text'] == ' ' and click == False:
        buttons['text'] = 'O'
        click = True
        if checkWinWin():
            messagebox.showinfo("Such a jerk You are!","SMH!" )
            score2 += 1
            p2Entry.delete(0,END)
            p2Entry.insert(0,score2)
            restart()
    
        
def checkActual():
    global   score1 , score2
    if score1 > 2 :
        scoreLabell = Label(root,text = "Player X wins" ,bg="#F4C724").grid(row = 1 ,column =  2 , sticky = W)
        score1 = 0 
        score2 = 0
        p1Entry.delete(0,END)
        p2Entry.delete(0,END)

    elif score2 > 2 :
        scoreLabell = Label(root,text = "Player O wins" ,bg="#F4C724").grid(row = 1 ,column =  2 , sticky = W)
        score1 = 0 
        score2 = 0
    
    else : scoreLabel = Label(root,text = "X = {0}/3 , O = {1}/3".format(score1,score2) ,bg="#F4C724").grid(row = 1 ,column =  2 , sticky = W)


   
button1 = Button(root , text = ' ' , height = 4 ,font =("Verdana","10","bold"), width = 10 , command = lambda : buttonClicked(button1) , bg = "#0ABDE3" )
button1.grid(row = 2 ,column = 0 ,sticky = NSEW)


button2 = Button(root , text = ' ' , height = 4 ,font =("Verdana","10","bold"), width = 10 , command = lambda : buttonClicked(button2) , bg = "#0ABDE3" )
button2.grid(row = 2 ,column = 1 ,sticky = NSEW)


button3 = Button(root , text = ' ' , height = 4 ,font =("Verdana","10","bold"), width = 10 , command = lambda : buttonClicked(button3) , bg = "#0ABDE3" )
button3.grid(row = 2 ,column = 2 ,sticky = NSEW)

button4 = Button(root , text = ' ' , height = 4 ,font =("Verdana","10","bold"), width = 10 , command = lambda : buttonClicked(button4) , bg = "#0ABDE3" )
button4.grid(row = 3 ,column = 0 ,sticky = NSEW)


button5 = Button(root , text = ' ' , height = 4 ,font =("Verdana","10","bold"), width = 10 , command = lambda : buttonClicked(button5) , bg = "#0ABDE3" )
button5.grid(row = 3 ,column = 1 ,sticky = NSEW)


button6 = Button(root , text = ' ' , height = 4 ,font =("Verdana","10","bold"), width = 10 , command = lambda : buttonClicked(button6) , bg = "#0ABDE3" )
button6.grid(row = 3 ,column = 2 ,sticky = NSEW)

button7 = Button(root , text = ' ' , height = 4 ,font =("Verdana","10","bold"), width = 10 , command = lambda : buttonClicked(button7) , bg = "#0ABDE3" )
button7.grid(row = 4 ,column = 0 ,sticky = NSEW)


button8 = Button(root , text = ' ' , height = 4 ,font =("Verdana","10","bold"), width = 10 , command = lambda : buttonClicked(button8)  , bg = "#0ABDE3")
button8.grid(row = 4 ,column = 1 ,sticky = NSEW)


button9 = Button(root , text = ' ' , height = 4 ,font =("Verdana","10","bold"), width = 10 , command = lambda : buttonClicked(button9) , bg = "#0ABDE3" )
button9.grid(row = 4 ,column = 2 ,sticky = NSEW)

rrestart = Button(root , text = 'Once More ?' , bg = "#8B78E6" , fg = "#EAF0F1" , font = ("Verdana" ,10) , command = lambda: restart() )
rrestart.grid(row = 0 ,column = 2 , sticky = E)



root.mainloop()