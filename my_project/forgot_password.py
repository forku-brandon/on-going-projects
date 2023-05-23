from tkinter import Image
from customtkinter import*
import customtkinter
import sys
import os
import subprocess
from tkinter import  messagebox
import tkinter
from PIL import Image, ImageTk
root_tk = customtkinter.CTk()
root_tk.iconbitmap(default='hacker.ico')                                       # create CTk window like you do with the Tk window
root_tk.geometry("1200x720")#setting up the geometry of the window screen
root_tk.minsize(920, 520)
root_tk.title('the cyber king => LOGIN')
customtkinter.set_appearance_mode("dark")
bg_image = Image.open("istockpho.jpg").resize((1200, 750))
image_TK = ImageTk.PhotoImage(bg_image)
app =  tkinter.Label(root_tk,
                     text='hahaha',
                       image=image_TK,
                       border=0,
                         )
app.pack()
new_frame= customtkinter.CTkLabel(
             root_tk,
             text='</>',
             width=900,
             height=600,
             
             corner_radius= 40
 )
new_frame.place(
            relx=0.5,
               rely=0.50,
                anchor=tkinter.CENTER
    
 )


def Continue():
    Email=email.get()
    Phone_number=phone_number.get()                             #getting the user email and phone_number
    if Phone_number =='phone number' and Email =='Email':
        messagebox.showwarning("FROM CYBER KING", " ENTER YOUR EMAIL OR PHONE NUMBER")
        # messagebox.showwarning("FROM CYBER KING", "ENTER YOUR Email")
    else:
        print('EMAIL=> '+Email)                    ######################################
        print('PHONE NUMBER=> '+Phone_number)
    if Phone_number =='phone number':
        root_tk.destroy()
        subprocess.Popen([sys.executable, "verify_account.py"])
    elif  Email =='Email':
            root_tk.destroy()
            subprocess.Popen([sys.executable, "verifyn_account.py"])
          
def login():
    root_tk.destroy()
    subprocess.Popen([sys.executable, "login_page.py"])

label_me = customtkinter.CTkButton(
            root_tk,
            text="login",
            command=login,
            border_color='black',
            fg_color='transparent',
              text_color='white',
              hover_color='green',           #the submit button
              border_width=2,
              width=200,
             
               height=60, 
             font=('serif, Bold', 20),
             corner_radius=20,
            )
label_me.place(
            relx=0.6,
              rely=0.80,
               anchor=tkinter.CENTER
               )
def creat_account():
    """Restarts the current program."""
    root_tk.destroy()
    subprocess.Popen([sys.executable, "create_password.py"])
label_me = customtkinter.CTkButton(
            root_tk,
            text="create account",
         # bg_color='transparent',
              border_color='black',
            fg_color='transparent',
              text_color='white',
              hover_color='green',
              border_width=2,                    #the create account button
              width=200,
              command=creat_account,
               height=60, 
             font=('serif, Bold', 20),
             corner_radius=20,
            )
label_me.place(
            relx=0.4,
              rely=0.80,
               anchor=tkinter.CENTER
               )

label_me = customtkinter.CTkButton(
            root_tk,
            text="continue",
         
             border_width=0,
            fg_color='transparent',
              text_color='white',        #the forgot password button
              hover_color='green',
              command=Continue,
              width=400,
               height=60, 
             font=('serif, Bold', 20),
             corner_radius=20,
            )
label_me.place(
            relx=0.5,
              rely=0.70,
               anchor=tkinter.CENTER
               )

email = customtkinter.CTkEntry(
             root_tk,
               border_width=2,
               width=400,
               bg_color='transparent',
               text_color='green',             #entry for the user name
               border_color='green',
                height=60, 
             
              corner_radius=20,
             )
email.insert(0, 'Email')

email.place(
        relx=0.5,
               rely=0.40,
                anchor=tkinter.CENTER
               )
labell_me1 = customtkinter.CTkLabel(
             root_tk,
              text="forgot password",
           bg_color='transparent',          #label for the login
           text_color='green',
           font=('serif, Bold', 40),
                      )
labell_me1.place(
        relx=0.5,
               rely=0.20,
                anchor=tkinter.CENTER
               )
labell_me2 = customtkinter.CTkLabel(
             root_tk,
              text=" enter your email or password ",
           bg_color='transparent',
           text_color='green',                #label for the instruction....
           font=('serif, Bold', 19),
                      )
labell_me2.place(
        relx=0.5,
               rely=0.260,
                anchor=tkinter.CENTER
               )
# labell_me3 = customtkinter.CTkLabel(
#              root_tk,
#               text=" Email",
#            bg_color='transparent',
#            text_color='green',               #label for the user name
#            font=('serif, Bold', 19),
#                       )
# labell_me3.place(
#         relx=0.5,
#                rely=0.330,
#                 anchor=tkinter.CENTER
#                )
labell_me4 = customtkinter.CTkLabel(
             root_tk,
              text=" OR",
           bg_color='transparent',
           text_color='green',                #label for the password
           font=('serif, Bold', 19),
                      )
labell_me4.place(
        relx=0.5,
               rely=0.480,
                anchor=tkinter.CENTER
               )
phone_number = customtkinter.CTkEntry(
             root_tk,
            
               border_width=2,
               width=400,
               bg_color='transparent',
               text_color='green',                        #entry for the password
               border_color='green',
              height=60, 
              corner_radius=20,
             )
phone_number.insert(0, "phone number")
phone_number.place(
        relx=0.5,
               rely=0.580,
                anchor=tkinter.CENTER
               )

root_tk.mainloop()