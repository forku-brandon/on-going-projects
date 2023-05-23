# from tkinter import Image
from customtkinter import*
import customtkinter
import tkinter
import sys
import os
import subprocess
from PIL import Image, ImageTk




root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window
# root_tk.iconbitmap(default='hacker.ico')  
root_tk.geometry("1366x768")#setting up the geometry of the window screen
root_tk.minsize(1020, 620)
# root_tk.attributes('-fullscreen', True)
root_tk.title('the cyber king')
customtkinter.set_appearance_mode("dark")
bg_image = Image.open("hackers.jpg").resize((1100, 700))
image_TK = ImageTk.PhotoImage(bg_image)

app =  tkinter.Label(root_tk,
                     text='hahaha',
                       image=image_TK,
                       border=0,
)
app.pack()
class GUI:
    #creating an object(GUI)
    
    def __init__(self, root_tk):#initualing a functin and assigning it a variable called 'root_tk'
        Frame1 = customtkinter.CTkFrame( #creating  the framework that will take the size of the window
            root_tk
            )
        Frame1.pack()
        frame2 = customtkinter.CTkFrame(
            Frame1,
            width=100,
            height=720
           
            )
        frame2.pack(
             pady=20,
             padx=20,
            
            )
        
      
        frame3 = customtkinter.CTkFrame(
            root_tk, 
            width=500,
              height=725
              )
        frame3.pack()

        frame3.place(
            anchor="w",
            relx=0.0, 
            rely=0.5,
            relwidth=0.2,
            relheight=1
            )
        self.test()

 
    #     self.switch = customtkinter.CTkSwitch(
    #         master=root_tk, 
    #         text="Dark Mode", 
    #         command=self.theme_change
    #         )
    #     self.switch.toggle(1)
    #     self.switch.place(
    #         relx=0.05,
    #         rely=0.05
    #           )
    
    def test(self):
        
        def restart_program():
          """Restarts the current program."""
          root_tk.destroy()
          subprocess.Popen([sys.executable, "login_page.py"])
       
        self.label_width = customtkinter.CTkButton(
            root_tk,
            text="GET STARTED",
            command= restart_program,
            border_color='black',
            fg_color='transparent',
              text_color='white',
              hover_color='green',
              border_width=2,
              width=400,
               height=60, 
             font=('serif, Bold', 20),
             corner_radius=20
            )
        self.label_width.place(
            relx=0.5,
              rely=0.50,
               anchor=tkinter.CENTER
                )
        self.label_me = customtkinter.CTkButton(
            root_tk,
            text="GET UPDATES",
           # bg_color='transparent',
              border_color='black',
            fg_color='transparent',
              text_color='white',
              hover_color='green',
              border_width=2,
              width=400,
               height=60, 
             font=('serif, Bold', 20),
             corner_radius=20,
            )
        self.label_me.place(
            relx=0.5,
              rely=0.60,
               anchor=tkinter.CENTER
                )
        self.label_me = customtkinter.CTkButton(
            root_tk,
            text="ABOUT THIS TOOL",
         # bg_color='transparent',
              border_color='black',
            fg_color='transparent',
              text_color='white',
              hover_color='green',
              border_width=2,
              width=400,
               height=60, 
             font=('serif, Bold', 20),
             corner_radius=20,
            )
        self.label_me.place(
            relx=0.5,
              rely=0.70,
               anchor=tkinter.CENTER
                )
        
        bg_button = customtkinter.CTkImage(
            dark_image=Image.open("ethical hacker.jpeg"), 
            size=(300,850)
            )
        self.button_add_Face = customtkinter.CTkLabel(
             root_tk,
            text='</.>',
             text_color='green',
             font=('arial Bold', 21), 
             image=bg_button,
             ) 
        self.button_add_Face.place(
              relx=0.09, rely=0.56,
                anchor=tkinter.CENTER
                 )
    #     def theme_change(self):
    #      if self.switch.get() == 1:
    #          customtkinter.set_appearance_mode("dark")
    # #     else:
    #         customtkinter.set_appearance_mode("light")
    #    
bg_button = customtkinter.CTkImage(
            dark_image=Image.open("the.png"), 
            size=(850,280)
)
welcome = customtkinter.CTkLabel(
            root_tk,
           text='</>',
            font=('italic', 40),
            text_color= 'green',
            width=20, 
            height=50,
            image=bg_button
)
welcome.place(
                    relx=0.563,
                   rely=0.20,
                   anchor=tkinter.CENTER
                   )

#hackers.jpg
im = customtkinter.CTkImage(
            dark_image=Image.open("hackers.jpg"), 
            size=(290,780)
)
app = customtkinter.CTkLabel(
            root_tk,
           text='</>',
            font=('italic', 40),
            text_color= 'green',
            width=20, 
            height=50,
            image=im
)
app.place( relx =0.9,
          rely=0.0)
start = GUI(root_tk)
root_tk.mainloop()
