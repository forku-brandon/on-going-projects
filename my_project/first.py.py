# # import tkinter as tk

# # class Page(tk.Frame):
# #     def __init__(self, *args, **kwargs):
# #         tk.Frame.__init__(self, *args, **kwargs)
# #     def show(self):
# #         self.lift()

# # class Page1(Page):
# #    def __init__(self, *args, **kwargs):
# #        Page.__init__(self, *args, **kwargs)
# #        label = tk.Label(self, text="This is page 1")
# #        label.pack(side="top", fill="both", expand=True)

# # class Page2(Page):
# #    def __init__(self, *args, **kwargs):
# #        Page.__init__(self, *args, **kwargs)
# #        label = tk.Label(self, text="This is page 2")
# #        label.pack(side="top", fill="both", expand=True)

# # class Page3(Page):
# #    def __init__(self, *args, **kwargs):
# #        Page.__init__(self, *args, **kwargs)
# #        label = tk.Label(self, text="This is page 3")
# #        label.pack(side="top", fill="both", expand=True)

# # class MainView(tk.Frame):
# #     def __init__(self, *args, **kwargs):
# #         tk.Frame.__init__(self, *args, **kwargs)
# #         p1 = Page1(self)
# #         p2 = Page2(self)
# #         p3 = Page3(self)

# #         buttonframe = tk.Frame(self)
# #         container = tk.Frame(self)
# #         buttonframe.pack(side="top", fill="x", expand=False)
# #         container.pack(side="top", fill="both", expand=True)

# #         p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
# #         p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
# #         p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

# #         b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
# #         b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
# #         b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

# #         b1.pack(side="left")
# #         b2.pack(side="left")
# #         b3.pack(side="left")

# #         p1.show()

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     main = MainView(root)
# #     main.pack(side="top", fill="both", expand=True)
# #     root.wm_geometry("400x400")
# #     root.mainloop()



# # from tkinter import *
# # import webbrowser

# # root = Tk()

# # new = 1
# # url = "https://www.google.com"

# # def openweb():
# #     webbrowser.open(url,new=new)

# # Btn = Button(root, text = "This opens Google",command=openweb)
# # Btn.pack()

# # root.mainloop()


# # import tkinter as tk
# # from tkinter import ttk
# # from tkinter import filedialog as fd
# # from tkinter.messagebox import showinfo

# # # create the root window
# # root = tk.Tk()
# # root.title('Tkinter Open File Dialog')
# # root.resizable(False, False)
# # root.geometry('300x150')


# # def select_file():
# #     filetypes = (
# #         ('text files', '*.txt'),
# #         ('All files', '*.*')
# #     )

# #     filename = fd.askopenfilename(
# #         title='Open a file',
# #         initialdir='/',
# #         filetypes=filetypes)

# #     showinfo(
# #         title='Selected File',
# #         message=filename
# #     )


# # # open button
# # open_button = ttk.Button(
# #     root,
# #     text='Open a File',
# #     command=select_file
# # )

# # open_button.pack(expand=True)


# # # run the application
# # root.mainloop()
# # import tkinter as tk

# # root=tk.Tk()
# # root.title("My Bank")
# # root.geometry("500x500")

# # photo=tk.PhotoImage(file="the.png")
# # label = tk.Label(root, image=photo)
# # label.image = photo
# # label.pack()
# # label.place(x=0, y=0, relwidth=1, relheight=1)

# # tfm = tk.Frame(root, width=2000, height=50)
# # tfm.pack(side=tk.TOP)

# # w = tk.Label(tfm, text="MY bank", font=("Times", "24", "bold"), bg="yellow", anchor="e", fg="black", padx=350, pady=10)
# # w.pack(fill="both")

# # bfm = tk.Frame(root, width=2000, height=50, bg="gray")
# # bfm.pack(side=tk.BOTTOM)

# # w = tk.Label(root, text="Main Menu", font=("Times", "24", "bold"), bg="black", fg="white", padx=350, pady=10)
# # w.pack(padx=10, pady=30)

# # button1 = tk.Button(root, text="Sign Up", width=12, height=1, bg="black",fg="white", bd="8", font=("Helvetica", "12", "bold"))
# # button1.pack(padx=10, pady=10) 

# # button2 = tk.Button(root, text="Sign In",  width=12, height=1, 
# # bg="black",fg="white", bd="8",  font=("Helvetica", "12", "bold"))
# # button2.pack(padx=10, pady=10)

# # button3 = tk.Button(root, text="Admin Sign In", width=12, height=1, bg="black",fg="white", bd="8",  font=("Helvetica", "12", "bold"))
# # button3.pack(padx=10, pady=10)

# # button4 = tk.Button(root, text="Quit!",  width=5, height=1, bg="black",fg="white", bd="10",  font=("Helvetica", "12", "bold"))
# # button4.pack(padx=10, pady=10)

# # root.mainloop()

# import second
# import tkinter as tk



# root=tk.Toplevel()
# root.title("My Bank")
# root.geometry("500x500")

# # photo=tk.PhotoImage(file="image1.gif")
# # label = tk.Label(root, image=photo)
# # label.image = photo
# # label.pack()
# # label.place(x=0, y=0, relwidth=1, relheight=1)

# tfm = tk.Frame(root, width=2000, height=50)
# tfm.pack(side=tk.TOP)

# w = tk.Label(tfm, text="MY bank", font=("Times", "24", "bold"), bg="yellow", anchor="e", fg="black", padx=350, pady=10)
# w.pack(fill="both")

# bfm = tk.Frame(root, width=2000, height=50, bg="gray")
# bfm.pack(side=tk.BOTTOM)

# w = tk.Label(root, text="Main Menu", font=("Times", "24", "bold"), bg="black", fg="white", padx=350, pady=10)
# w.pack(padx=10, pady=30)

# button1 = tk.Button(root, text="Sign Up", command=lambda : second.signup() , width=12, height=1, bg="black",fg="white", bd="8", font=("Helvetica", "12", "bold"))
# button1.pack(padx=10, pady=10) 

# button2 = tk.Button(root, text="Sign In",  width=12, height=1, 
# bg="black",fg="white", bd="8",  font=("Helvetica", "12", "bold"))
# button2.pack(padx=10, pady=10)

# button3 = tk.Button(root, text="Admin Sign In", width=12, height=1, bg="black",fg="white", bd="8",  font=("Helvetica", "12", "bold"))
# button3.pack(padx=10, pady=10)

# button4 = tk.Button(root, text="Quit!",  width=5, height=1, bg="black",fg="white", bd="10",  font=("Helvetica", "12", "bold"))
# button4.pack(padx=10, pady=10)

# root.mainloop()
#Import the tkinter library
from tkinter import *

#Create an instance of tkinter frame
win = Tk()

#Set the geometry
win.geometry("650x250")

#Add a text label and add the font property to it
label= Label(win, text= "Hello World!", font=('Times New Roman bold',20))
label.pack(padx=10, pady=10)

#Create a fullscreen window
win.attributes('-fullscreen', True)

win.mainloop()
