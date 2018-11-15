'''Musical Piano'''

from tkinter import *
import time;
import datetime
import pygame

pygame.init()
root = Tk()
root.title('Musical Piano')
#Functions for the first row of keys
#------------------------------------
def C_Sharp():
    str1.set('C#')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\C_sharp.wav')
    sound.play()

def D_Sharp():
    str1.set('D#')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\D_sharp.wav')
    sound.play()

def F_Sharp():
    str1.set('F#')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\F_sharp.wav')
    sound.play()

def G_Sharp():
    str1.set('G#')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\G_sharp.wav')
    sound.play()

def B_Flat():
    str1.set('B Flat')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\Bb.wav')
    sound.play()

def CS1():
    str1.set('C#1')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\C_S1.wav')
    sound.play()

def DS1():
    str1.set('D#1')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\D_S1.wav')
    sound.play()
    
#Functions for the second row of keys
#--------------------------------------
def C():
    str1.set('C')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\C.wav')
    sound.play()

def D():
    str1.set('D')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\D.wav')
    sound.play()

def E():
    str1.set('E')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\E.wav')
    sound.play()

def F():
    str1.set('F')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\F.wav')
    sound.play()

def G():
    str1.set('G')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\G.wav')
    sound.play()

def A():
    str1.set('A')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\A.wav')
    sound.play()

def B():
    str1.set('B')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\B.wav')
    sound.play()

def C1():
    str1.set('C1')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\C1.wav')
    sound.play()

def D1():
    str1.set('D1')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\D1.wav')
    sound.play()

def E1():
    str1.set('E1')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\E1.wav')
    sound.play()

def F1():
    str1.set('F1')
    sound = pygame.mixer.Sound('D:\PYTHON\Chords\F1.wav')
    sound.play()

    
#Main Frame
ABC = Frame(root,bg='RoyalBlue1',bd=20,relief=RIDGE)
ABC.grid()

#Sub Frames
ABC1 = Frame(ABC,bg='RoyalBlue1',bd=20,relief=RIDGE)
ABC1.grid()
ABC2 = Frame(ABC,bg='RoyalBlue1',relief=RIDGE)
ABC2.grid()
ABC3 = Frame(ABC,bg='RoyalBlue1',relief=RIDGE)
ABC3.grid()

#Setting Date and Time Variables
str1 = StringVar()
str1.set('Just Like Music')
Date1 = StringVar()
Time1 = StringVar()

#Setting the date and time using TIME MODULE
Date1.set(time.strftime('%d/%m/%Y'))
Time1.set(time.strftime('%H:%M:%S'))

#Now we will create a label
Label(ABC1,text='Piano Keys',font=('arial',25,'italic'),padx=6,pady=6,bd=4,
      bg='grey',fg='white',justify=CENTER,).grid(row=0,column=0,columnspan=11)

#Create some Entry for frame ABC1
txtDate = Entry(ABC1,textvariable=Date1,font=('arial',18,'italic'),
      bg='RoyalBlue1',fg='white',width=28,justify=CENTER,bd=34)
txtDate.grid(row=1,column=0,pady=1)

txtDisplay = Entry(ABC1,textvariable=str1,font=('arial',18,'italic'),
      bg='RoyalBlue1',fg='white',width=28,justify=CENTER,bd=34)
txtDisplay.grid(row=1,column=1,pady=1)

txtTime = Entry(ABC1,textvariable=Time1,font=('arial',18,'italic'),
      bg='RoyalBlue1',fg='white',width=28,justify=CENTER,bd=34)
txtTime.grid(row=1,column=2,pady=1)

#Create First set of keys on frame ABC2
#-------------------------------------------
#C Sharp Button
btnCs = Button(ABC2,width=6,bd=4,text='C#',font=('arial',18,'italic')
      ,height=6,bg='peach puff',fg='grey5',command=C_Sharp)
btnCs.grid(row=0,column=0,padx=4,pady=4)
#D Sharp Button
btnDs = Button(ABC2,width=6,bd=4,text='D#',font=('arial',18,'italic')
      ,height=6,bg='peach puff',fg='grey5',command=D_Sharp)
btnDs.grid(row=0,column=1,padx=4,pady=4)
#Space
btnSpace2 = Button(ABC2,width=2,state=DISABLED,relief=FLAT
      ,height=6,bg='pink')
btnSpace2.grid(row=0,column=3,padx=0,pady=0)
#F Sharp Button
btnFs = Button(ABC2,width=6,bd=4,text='F#',font=('arial',18,'italic')
      ,height=6,bg='peach puff',fg='grey5',command=F_Sharp)
btnFs.grid(row=0,column=4,padx=4,pady=4)
#G Sharp Button
btnGs = Button(ABC2,width=6,bd=4,text='G#',font=('arial',18,'italic')
      ,height=6,bg='peach puff',fg='grey5',command=G_Sharp)
btnGs.grid(row=0,column=6,padx=4,pady=4)
#B Flat Button 
btnBb = Button(ABC2,width=6,bd=4,text='Bb',font=('arial',18,'italic')
      ,height=6,bg='peach puff',fg='grey5',command=B_Flat)
btnBb.grid(row=0,column=8,padx=4,pady=4)
#Space
btnSpace5 = Button(ABC2,width=2,bd=4,state=DISABLED,relief=FLAT
      ,height=6,bg='pink')
btnSpace5.grid(row=0,column=9,padx=0,pady=0)
#C Sharp1 Button
btnCs1 = Button(ABC2,width=6,bd=4,text='C#1',font=('arial',18,'italic')
      ,height=6,bg='peach puff',fg='grey5',command=CS1)
btnCs1.grid(row=0,column=10,padx=4,pady=4)
#D Sharp1 Button
btnDs1 = Button(ABC2,width=6,bd=4,text='D#1',font=('arial',18,'italic')
      ,height=6,bg='peach puff',fg='grey5',command=DS1)
btnDs1.grid(row=0,column=11,padx=4,pady=4)

#Create second set of keys on Frame ABC3
#------------------------------------------
#C Chord
btnC = Button(ABC3,width=6,height=8,bd=4,fg='white',bg='goldenrod',text='C',
              font=('arial',18,'bold'),command=C)
btnC.grid(row=0,column=0,padx=4,pady=4)
#D Chord
btnD = Button(ABC3,width=6,height=8,bd=4,fg='white',bg='goldenrod',text='D',
              font=('arial',18,'bold'),command=D)
btnD.grid(row=0,column=1,padx=4,pady=4)
#E Chord
btnE = Button(ABC3,width=6,height=8,bd=4,fg='white',bg='goldenrod',text='E',
              font=('arial',18,'bold'),command=E)
btnE.grid(row=0,column=2,padx=4,pady=4)
#F Chord
btnF = Button(ABC3,width=6,height=8,bd=4,fg='white',bg='goldenrod',text='F',
              font=('arial',18,'bold'),command=F)
btnF.grid(row=0,column=3,padx=4,pady=4)

#G Chord
btnG = Button(ABC3,width=6,height=8,bd=4,fg='white',bg='goldenrod',text='G',
              font=('arial',18,'bold'),command=G)
btnG.grid(row=0,column=4,padx=4,pady=4)
#A Chord
btnA = Button(ABC3,width=6,height=8,bd=4,fg='white',bg='goldenrod',text='A',
              font=('arial',18,'bold'),command=A)
btnA.grid(row=0,column=5,padx=4,pady=4)
#B Chord
btnB = Button(ABC3,width=6,height=8,bd=4,fg='white',bg='goldenrod',text='B',
              font=('arial',18,'bold'),command=B)
btnB.grid(row=0,column=6,padx=4,pady=4)
#C1 Chord
btnC1 = Button(ABC3,width=6,height=8,bd=4,fg='white',bg='goldenrod',text='C1',
              font=('arial',18,'bold'),command=C1)
btnC1.grid(row=0,column=7,padx=4,pady=4)

#D1 Chord
btnD1 = Button(ABC3,width=6,height=8,bd=4,fg='white',bg='goldenrod',text='D1',
              font=('arial',18,'bold'),command=D1)
btnD1.grid(row=0,column=8,padx=4,pady=4)
#E1 Chord
btnE1 = Button(ABC3,width=6,height=8,bd=4,fg='white',bg='goldenrod',text='E1',
              font=('arial',18,'bold'),command=E1)
btnE1.grid(row=0,column=9,padx=4,pady=4)
#F1 Chord
btnF1 = Button(ABC3,width=6,height=8,bd=4,fg='white',bg='goldenrod',text='F1',
              font=('arial',18,'bold'),command=F1)
btnF1.grid(row=0,column=10,padx=4,pady=4)



root.geometry('1400x700+0+0')
root.configure(background='white')
root.mainloop()

