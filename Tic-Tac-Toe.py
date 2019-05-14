from tkinter import  *
from tkinter import  ttk
from tkinter import messagebox
root = Tk()
root.title('Tic tac toy: Player 1')

style=ttk.Style()
style.theme_use('classic')

ActivatedPlayer =1
p1=[]
p2=[]


bu1=ttk.Button(root , text='' )
bu1.grid(row=0 , column= 0 , sticky='snew', ipadx=30 , ipady=30)
bu1.config(command=lambda:click(1))

bu2=ttk.Button(root , text='')
bu2.grid(row=0 , column= 1 , sticky='snew', ipadx=30 , ipady=30)
bu2.config(command=lambda:click(2))


bu3=ttk.Button(root , text='')
bu3.grid(row=0 , column= 2 , sticky='snew', ipadx=30 , ipady=30)
bu3.config(command=lambda:click(3))

bu4=ttk.Button(root , text='')
bu4.grid(row=1 , column= 0 , sticky='snew', ipadx=30 , ipady=30)
bu4.config(command=lambda:click(4))


bu5=ttk.Button(root , text='')
bu5.grid(row=1 , column= 1 , sticky='snew', ipadx=30 , ipady=30)
bu5.config(command=lambda:click(5))


bu6=ttk.Button(root , text='')
bu6.grid(row=1 , column= 2 , sticky='snew', ipadx=30 , ipady=30)
bu6.config(command=lambda:click(6))

bu7=ttk.Button(root , text='')
bu7.grid(row=2 , column= 0 , sticky='snew', ipadx=30 , ipady=30)
bu7.config(command=lambda:click(7))

bu8=ttk.Button(root , text='')
bu8.grid(row=2 , column= 1 , sticky='snew', ipadx=30 , ipady=30)
bu8.config(command=lambda:click(8))


bu9=ttk.Button(root , text='')
bu9.grid(row=2 , column= 2 , sticky='snew', ipadx=30 , ipady=30)
bu9.config(command=lambda:click(9))





def click(id):
 global ActivatedPlayer
 global p1
 global p2

 if(ActivatedPlayer==1):
  appearing_XO(id,'X')
  p1.append(id)
  root.title('Tic Tac toy: Player 2')
  ActivatedPlayer=2


 elif(ActivatedPlayer==2):
  appearing_XO(id,'O')
  p2.append(id)
  root.title('Tic Tac toy: Player 1')
  ActivatedPlayer=1
 CheckWinner()


def CheckWinner():
 winner=0
 if (1 in p1 and 2 in p1 and 3 in p1):
  winner=1
 elif (1 in p2 and 2 in p2 and 3 in p2):
  winner = 2
 elif (4 in p1 and 5 in p1 and 6 in p1):
   winner = 1
 elif (4 in p2 and 5 in p2 and 6 in p2):
    winner = 1
 elif (7 in p1 and 8 in p1 and 9 in p1):
     winner = 1
 elif (7 in p2 and 8 in p2 and 9 in p2):
      winner = 1
 elif (1 in p1 and 4 in p1 and 7 in p1):
       winner = 1
 elif (1 in p2 and 4 in p2 and 7 in p2):
  winner = 2

 elif (2 in p1 and 5 in p1 and 8 in p1):
  winner = 1
 elif (2 in p2 and 5 in p2 and 8 in p2):
  winner = 2
 elif (3 in p1 and 6 in p1 and 9 in p1):
  winner = 1
 elif (3 in p2 and 6 in p2 and 9 in p2):
  winner = 2

 if (winner==1):
   messagebox.showinfo(title='Winner Winner, Chicken Dinner' , message='Player 1 Wins')

 elif (winner ==2):
   messagebox.showinfo(title='Winner Winner, Chicken Dinner', message='Player 2 Wins')



def appearing_XO(id , text):
 if (id ==1):
  bu1.config(text=text)
  bu1.state(['disabled'])

 elif (id == 2):
  bu2.config(text=text)
  bu2.state(['disabled'])

 elif (id == 3):
  bu3.config(text=text )
  bu3.state(['disabled'])

 elif (id == 4):
  bu4.config(text=text)
  bu4.state(['disabled'])

 elif (id == 5):
  bu5.config(text=text)
  bu5.state(['disabled'])

 elif (id == 6):
  bu6.config(text=text)
  bu6.state(['disabled'])

 elif (id == 7):
  bu7.config(text=text)
  bu7.state(['disabled'])

 elif (id == 8):
  bu8.config(text=text)
  bu8.state(['disabled'])

 elif (id == 9):
  bu9.config(text=text)
  bu9.state(['disabled'])




root.mainloop()
