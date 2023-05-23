from tkinter import Image
from customtkinter import*
import customtkinter
from tkinter import  messagebox
import tkinter
import sys
import os
import subprocess
from PIL import Image, ImageTk
root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window
root_tk.iconbitmap(default='hacker.ico')  
root_tk.geometry("1200x720")#setting up the geometry of the window screen
root_tk.minsize(920, 520)
root_tk.title('the cyber king => CREATE YOUR ACCOUNT')
customtkinter.set_appearance_mode("dark")
bg_image = Image.open("green.jpeg").resize((1100, 750))
image_TK = ImageTk.PhotoImage(bg_image)
app =  tkinter.Label(root_tk,                            #displaying the background image
                     text='hahaha',
                       image=image_TK,
                       border=0,
                         )
app.pack()

def create():
          Entry5=Entry5.get()
          Entry1=Entry1.get()
          Entry2= Entry2.get()                       #getting the user name and Entry1
          
          if Entry5 =='':
                 messagebox.showwarning("FROM CYBER KING", "ENTER USER NAME")
         
          elif Entry1 =='':
                messagebox.showwarning("FROM CYBER KING", "ENTER Entry1")
        
          elif Entry2 =='':
                 messagebox.showwarning("FROM CYBER KING", " CONFIRM YOUR Entry1")
          
          elif Entry1 != Entry2:
                messagebox.showwarning("FROM CYBER KING", "CONFIRM YOUR Entry1 CORRECTLY")
         
          else:
           print('usser name=> '+Entry5)                            ####################################
           print('Entry1=> '+Entry1)
           print('Entry1 confirm = TRUE')
           root_tk.destroy()
           subprocess.Popen([sys.executable, "authentication.py"])

# new_frame= customtkinter.CTkLabel(
#              root_tk,
#              text='</>',
#              width=60,
#              height=600,  #the dark frame of the login
             
#              corner_radius= 40
#               )
# new_frame.place(
#             relx=0.5,    #dispay of the dark frame
#                rely=0.50,
#                 anchor=tkinter.CENTER
    
#              )
def create():
    """Restarts the current program."""
    root_tk.destroy()
    subprocess.Popen([sys.executable, "create_password.py"])

login = customtkinter.CTkButton(
            root_tk,
            text="create account",
             command=create,
              border_color='black',
            fg_color='transparent',    #creating the 'create account' button
              text_color='white',
              hover_color='green',
              border_width=2,
              width=400,
               height=55, 

             font=('serif, Bold', 20),
             corner_radius=20,
            )
login.place(
            relx=0.5,
              rely=0.80,      #dispaying the login button
               anchor=tkinter.CENTER
               )

create_account = customtkinter.CTkButton(
            root_tk,
            text="continue",
              border_color='black',
            fg_color='transparent',    #creating the 'create account' button
              text_color='white',
              hover_color='green',
              border_width=2,
              width=400,
               height=60, 

             font=('serif, Bold', 20),
             corner_radius=20,
            )
create_account.place(
            relx=0.5,    #dispaying the creat account button
              rely=0.60,
               anchor=tkinter.CENTER
               )
create_account = customtkinter.CTkButton(
            root_tk,
            text="resend code",
             command=create,
              border_color='black',
            fg_color='transparent',    #creating the 'create account' button
              text_color='white',
              hover_color='green',
              border_width=2,
              width=400,
               height=60, 

             font=('serif, Bold', 20),
             corner_radius=20,
            )
create_account.place(
            relx=0.5,    #dispaying the creat account button
              rely=0.70,
               anchor=tkinter.CENTER
               )


Entry3 = customtkinter.CTkComboBox(
             root_tk,
             dropdown_hover_color='green',
            values=['1','2','3','4','5','6','7','8','9'],
               border_width=2,
               width=60,
               bg_color='transparent',   #getting the entry imput
               text_color='green',
               border_color='green',
                height=60, 
             
              corner_radius=20,
             )
Entry3.place(
        relx=0.5,
               rely=0.4,       #displaying the user input
                anchor=tkinter.CENTER
               )


Entry4 = customtkinter.CTkComboBox(
             root_tk,
             dropdown_hover_color='green',
            values=['1','2','3','4','5','6','7','8','9'],
               border_width=2,
               width=60,
               bg_color='transparent',   #getting the entry imput
               text_color='green',
               border_color='green',
                height=60, 
             
              corner_radius=20,
             )
Entry4.place(
        relx=0.6,
               rely=0.4,       #displaying the user input
                anchor=tkinter.CENTER
               )


Entry5 = customtkinter.CTkComboBox(
             root_tk,
             dropdown_hover_color='green',
            values=['1','2','3','4','5','6','7','8','9'],
               border_width=2,
               width=60,
               bg_color='transparent',   #getting the entry imput
               text_color='green',
               border_color='green',
                height=60, 
             
              corner_radius=20,
             )
Entry5.place(
        relx=0.7,
               rely=0.4,       #displaying the user input
                anchor=tkinter.CENTER
               )
labell_me1 = customtkinter.CTkLabel(
             root_tk,
              text="VERIFY YOUR ACCOUNT",
           bg_color='transparent',
           text_color='green',     #creating the creat account lebel
           font=('serif, Bold', 40),
                      )
labell_me1.place(
        relx=0.5,        #displaying the crreate account lebel
               rely=0.20,
                anchor=tkinter.CENTER
               )
labell_me2 = customtkinter.CTkLabel(
             root_tk,
              text="A five digit code has been send to your Phone number please enter the code in  here",
           bg_color='transparent',
           text_color='green',
           font=('serif, Bold', 19),
                      )
labell_me2.place(                    # creating and placing the  'please enter.....' massage
        relx=0.5,
               rely=0.260,
                anchor=tkinter.CENTER
               )

Entry1 = customtkinter.CTkComboBox(
             root_tk,
             dropdown_hover_color='green',
            values=['1','2','3','4','5','6','7','8','9'],
               border_width=2,
               width=60,
               bg_color='transparent',
               text_color='green',
               border_color='green',
              height=60,                      #creating and placing the 'Entry1' entry
              corner_radius=20,
             )
Entry1.place(
        relx=0.3,
               rely=0.4,
                anchor=tkinter.CENTER
               )
Entry2 = customtkinter.CTkComboBox(
             root_tk,
             dropdown_hover_color='green',
            values=['1','2','3','4','5','6','7','8','9'],
               border_width=2,
               width=60,
               bg_color='transparent',
               text_color='green',
               border_color='green',           #creating and placing the 'Entry2' label
              height=60, 
              
             
              corner_radius=20,
             )
Entry2.place(
        relx=0.4,
               rely=0.4,
                anchor=tkinter.CENTER
               ) 
 
root_tk.mainloop()
