from tkinter import Image
from customtkinter import*
import customtkinter
import tkinter
import sys
import os
import subprocess
from tkinter import  messagebox
import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
root_tk = customtkinter.CTk()  #create CTk window like you do with the Tk window
root_tk.iconbitmap(default='hacker.ico')  
root_tk.geometry("1200x720")#setting up the geometry of the window screen
root_tk.minsize(920, 520)
root_tk.title('the cyber king => authentication process')
customtkinter.set_appearance_mode("dark")
bg_image = Image.open("backgroundd.jpg").resize((1200, 750))
image_TK = ImageTk.PhotoImage(bg_image)
app =  tkinter.Label(root_tk,
                     text='hahaha',
                       image=image_TK,
                       border=0,
         )
app.pack()
labell_me1 = customtkinter.CTkLabel(
              root_tk,
               text="AUTHENTICATION",
            bg_color='transparent',
            text_color='green',     #creating the authentication lebel
            font=('serif, Bold', 40),
                       )
labell_me1.place(
         relx=0.27,        #displaying the authenticaftion lebel
                rely=0.060,
                 anchor=tkinter.CENTER
                )
labell_me2 = customtkinter.CTkLabel(
              root_tk,
               text=" before we create you an account we need some of your personal information for authentication purposes\nthis is useful if incase you forget your login credentials\n this imformation may stand as your back up password ",
            bg_color='transparent',
            text_color='green',
            font=('serif, Bold', 19),
                       )
labell_me2.place(                    #creating and placing the  'instruction massage...' massage
         relx=0.47,
         rely=0.130,
         anchor=tkinter.CENTER
                )
vallues1 = []
with open('best game.txt') as inFile:
     vallues1 = [line for line in inFile]

best_game =customtkinter.CTkComboBox(
            root_tk,
            values=vallues1,
            border_width=2,
            width=600,
            bg_color='transparent',   #getting the users best game imput
            text_color='green',
            border_color='green',
            height=50, 
            corner_radius=20,
             dropdown_hover_color='green',
             dropdown_fg_color='black',
            
             )
best_game.place(
        relx=0.27,
               rely=0.30,       
                anchor=tkinter.CENTER
               )
vallues2 = []
with open('year of birth.txt') as inFile:
     vallues2 = [line for line in inFile]

year_of_birth = customtkinter.CTkComboBox(
             root_tk,
            values=vallues2,
            border_width=2,
            width=600,
            bg_color='transparent',   #getting the users year of birth
            text_color='green',
            border_color='green',
            height=50, 
            corner_radius=20,
             dropdown_hover_color='green',
             dropdown_fg_color='black'
             )
year_of_birth.place(
        relx=0.27,
               rely=0.470,
                anchor=tkinter.CENTER
               )
vallues3 = []
with open('best dish.txt') as inFile:
     vallues3 = [line for line in inFile]

best_dish = customtkinter.CTkEntry(
             root_tk,
          #   values=vallues3,
            border_width=2,

            width=600,
            bg_color='transparent',   #getting the users best dish
            text_color='green',
            border_color='green',
            height=50, 
            corner_radius=20,
          #    dropdown_hover_color='green',
          #    dropdown_fg_color='black'
             )
             
best_dish.insert(0, 'Enter your Email Or Phone number')
best_dish.place(
        relx=0.27,
               rely=0.740,
                anchor=tkinter.CENTER
               )
vallues4 = []
with open('places.txt') as inFile:
     vallues4 = [line for line in inFile]

places_you_love_going = customtkinter.CTkComboBox(
             root_tk,
            values=vallues4,
            border_width=2,
            width=600,
            bg_color='transparent',   #getting the users  input
            text_color='green',
            border_color='green',
            height=50, 
            corner_radius=20,
            dropdown_hover_color='green',
            dropdown_fg_color='black'
             )
places_you_love_going.place(
        relx=0.27,
               rely=0.650,
                anchor=tkinter.CENTER
               )
vallues5 = []
with open('languages.txt') as inFile:
     vallues5 = [line for line in inFile]

languages = customtkinter.CTkComboBox(
             root_tk,
            values=vallues5,
            border_width=2,

            width=600,
            bg_color='transparent',   #getting the number of languages
            text_color='green',
            border_color='green',
            height=50, 
            corner_radius=20,
             dropdown_hover_color='green',
             dropdown_fg_color='black'
             )
languages.place(
        relx=0.27,
               rely=0.560,
                anchor=tkinter.CENTER
               )
vallues6 = []
with open('country.txt') as inFile:
     vallues6 = [line for line in inFile]

country = customtkinter.CTkComboBox(
             root_tk,
            values=vallues6,
            border_width=2,
            width=600,
            bg_color='transparent',   #getting the users country
            text_color='green',
            border_color='green',
            height=50, 
            corner_radius=20,
             dropdown_hover_color='green',
             dropdown_fg_color='black'
             )
country.place(
        relx=0.27,
               rely=0.3850,
                anchor=tkinter.CENTER
               )
vallues7 = []
with open('bed time.txt') as inFile:
     vallues7 = [line for line in inFile]
wake_up_from_bed = customtkinter.CTkComboBox(
             root_tk,
            values=vallues7,
            border_width=2,
            width=600,
            bg_color='transparent',   #getting the users country
            text_color='green',
            border_color='green',
            height=50, 
            corner_radius=20,
             dropdown_hover_color='green',
             dropdown_fg_color='black'
             )
wake_up_from_bed.place(
        relx=0.27,
               rely=0.220,
                anchor=tkinter.CENTER  )

def get_input( ):
      Country=country.get()
      Wake_up_from_bed=wake_up_from_bed.get()
      Languages=languages.get()
      Places_you_love_going=  places_you_love_going.get()
      Best_dish=best_dish.get()
      Year_of_birth=year_of_birth.get()
      Best_game=best_game.get()
      if   Country ==vallues6[0]:
        messagebox.showwarning("FROM CYBER KING", "Enter your country")
      elif Wake_up_from_bed== vallues7[0]:
              messagebox.showwarning("FROM CYBER KING", "Enter your bed time")
      elif Languages==vallues5[0]:
               messagebox.showwarning("FROM CYBER KING", "Enter the number of languages you speak")
      elif  Places_you_love_going==vallues4[0]:
               messagebox.showwarning("FROM CYBER KING", "Enter the place you which to visit")
      elif   Best_dish=='Enter your Email Or Phone number':
             messagebox.showwarning("FROM CYBER KING", "Enter your Email Or phone number")
      elif     Year_of_birth==vallues2[0]:
               messagebox.showwarning("FROM CYBER KING", "Enter your year of birth")
      elif     Best_game==vallues1[0]:
                   messagebox.showwarning("FROM CYBER KING", "Enter your best sporting game")
      else:
              print('country => '+Country)
              print( 'bed time=> '+Wake_up_from_bed)
              print( 'language=> '+Languages)
              print('country to be visited=> '+Places_you_love_going) ##########################################
              print( 'email/number=> '+Best_dish)
              print('year of birth=> '+Year_of_birth)
              print('best game=> '+Best_game)

create_account = customtkinter.CTkButton(
            root_tk,
            text="CONTINUE",
         bg_color='transparent',
              border_color='black',
            fg_color='black',    #creating the 'create account' button
              text_color='white',
              hover_color='green',
              border_width=2,
              width=300,
               height=60, 
             font=('serif, Bold', 20),
             corner_radius=20,
             command= get_input
            )
create_account.place(
            relx=0.27,    #dispaying the creat account button
              rely=0.840,
               anchor=tkinter.CENTER
)
 
root_tk.mainloop()