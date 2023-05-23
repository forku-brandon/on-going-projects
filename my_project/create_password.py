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
bg_image = Image.open("hackers.jpg").resize((1200, 750))
image_TK = ImageTk.PhotoImage(bg_image)
app =  tkinter.Label(root_tk,                            #displaying the background image
                     text='hahaha',
                       image=image_TK,
                       border=0,
                         )
app.pack()

def create():
          User_name=user_name.get()
          Password=password.get()
          Confirm_password= confirm_password.get()                       #getting the user name and password
          
          if User_name =='':
                 messagebox.showwarning("FROM CYBER KING", "ENTER USER NAME")
         
          elif Password =='':
                messagebox.showwarning("FROM CYBER KING", "ENTER PASSWORD")
        
          elif Confirm_password =='':
                 messagebox.showwarning("FROM CYBER KING", " CONFIRM YOUR PASSWORD")
          
          elif Password != Confirm_password:
                messagebox.showwarning("FROM CYBER KING", "CONFIRM YOUR PASSWORD CORRECTLY")
         
          else:
           print('usser name=> '+User_name)                            ####################################
           print('password=> '+Password)
           print('password confirm = TRUE')
           root_tk.destroy()
           subprocess.Popen([sys.executable, "authentication.py"])

new_frame= customtkinter.CTkLabel(
             root_tk,
             text='</>',
             width=900,
             height=600,  #the dark frame of the login
             
             corner_radius= 40
              )
new_frame.place(
            relx=0.5,    #dispay of the dark frame
               rely=0.50,
                anchor=tkinter.CENTER
    
             )
def login():
    """Restarts the current program."""
    root_tk.destroy()
    subprocess.Popen([sys.executable, "login_page.py"])

login = customtkinter.CTkButton(
            root_tk,
            text="login",
            command=login,
            fg_color='transparent',
            text_color='white',     # creating the login button
            hover_color='green',
            border_width=0,
            width=200,
            height=40, 
            font=('serif, Bold', 20),
            corner_radius=20,
            )
login.place(
            relx=0.6,
              rely=0.880,      #dispaying the login button
               anchor=tkinter.CENTER
               )

create_account = customtkinter.CTkButton(
            root_tk,
            text="create account",
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
              rely=0.80,
               anchor=tkinter.CENTER
               )

user_name = customtkinter.CTkEntry(
             root_tk,
            
               border_width=2,
               width=400,
               bg_color='transparent',   #getting the users imput
               text_color='green',
               border_color='green',
                height=60, 
             
              corner_radius=20,
             )
user_name.place(
        relx=0.5,
               rely=0.40,       #displaying the user input
                anchor=tkinter.CENTER
               )
labell_me1 = customtkinter.CTkLabel(
             root_tk,
              text="create account",
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
              text=" please enter the information bellow",
           bg_color='transparent',
           text_color='green',
           font=('serif, Bold', 19),
                      )
labell_me2.place(                    # creating and placing the  'please enter.....' massage
        relx=0.5,
               rely=0.260,
                anchor=tkinter.CENTER
               )
labell_me3 = customtkinter.CTkLabel(
             root_tk,
              text=" user name",
           bg_color='transparent',
           text_color='green',
           font=('serif, Bold', 19),
                      )            #creating and placing the 'user name' label
labell_me3.place(
        relx=0.5,
               rely=0.330,
                anchor=tkinter.CENTER
               )
labell_me4 = customtkinter.CTkLabel(
             root_tk,
              text=" password",
           bg_color='transparent',
           text_color='green',            #creating and placing the 'password' label
           font=('serif, Bold', 19),
                      )
labell_me4.place(
        relx=0.5,
               rely=0.480,
                anchor=tkinter.CENTER
               )
password = customtkinter.CTkEntry(
             root_tk,
            
               border_width=2,
               width=400,
               bg_color='transparent',
               text_color='green',
               border_color='green',
              height=60,                      #creating and placing the 'password' entry
              
              show='#',
              corner_radius=20,
             )
password.place(
        relx=0.5,
               rely=0.550,
                anchor=tkinter.CENTER
               )
confirm_password = customtkinter.CTkEntry(
             root_tk,
            
               border_width=2,
               width=400,
               bg_color='transparent',
               text_color='green',
               border_color='green',           #creating and placing the 'confirm_password' label
              height=60, 
              
              show='#',
              corner_radius=20,
             )
confirm_password.place(
        relx=0.5,
               rely=0.70,
                anchor=tkinter.CENTER
               )

labell_me5 = customtkinter.CTkLabel(
             root_tk,
              text="  confirm password",
           bg_color='transparent',
           text_color='green',                    #creating and placing the 'confirm password' label
           font=('serif, Bold', 19),
                      )
labell_me5.place(
        relx=0.5,
               rely=0.630,
                anchor=tkinter.CENTER
               )
labell_me3 = customtkinter.CTkLabel(
             root_tk,
              text=" already have and account",
           bg_color='transparent',
           text_color='green',                  #creating and placing the 'already have.....' label
           font=('serif, Bold', 19),
                      )
labell_me3.place(
        relx=0.4,
               rely=0.890,
                anchor=tkinter.CENTER
               )
 
root_tk.mainloop()
