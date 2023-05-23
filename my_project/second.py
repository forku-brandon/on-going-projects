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

# # w = tk.Label(root, text="Sign Up", font=("Times", "24", "bold"), bg="black", fg="white", padx=350, pady=10)
# # w.pack(padx=10, pady=30)

# # e1 = tk.Entry(root, width=20,   font=("Times", "14", "bold"), bd=3, fg="blue")
# # e1.insert(0, 'Username')
# # e1.pack(padx=150, pady=10)

# # e2 = tk.Entry(root, width=20,   font=("Times", "14", "bold"), bd=3, fg="blue")
# # e2.insert(0, 'Email')
# # e2.pack(padx=150, pady=10)

# # e3 = tk.Entry(root, width=20,   font=("Times", "14", "bold"), bd=3, fg="blue")
# # e3.insert(0, 'Password')
# # e3.pack(padx=150, pady=10)

# # button1 = tk.Button(root, text="Sign Up", width=12, height=1, bg="black",fg="white", bd="8", font=("Helvetica", "12", "bold"))
# # button1.pack(padx=100, pady=20) 

# # root.mainloop()


# """
# Created on Mon May  7 11:09:28 2018

# @author: kedar
# """

# import tkinter as tk

# def signup():

#     root=tk.Toplevel()
#     root.title("My Bank")
#     root.geometry("500x500")

#     # photo=tk.PhotoImage(file="image1.gif")
#     # label = tk.Label(root, image=photo)
#     # label.image = photo
#     # label.pack()
#     # label.place(x=0, y=0, relwidth=1, relheight=1)

#     tfm = tk.Frame(root, width=2000, height=50)
#     tfm.pack(side=tk.TOP)

#     w = tk.Label(tfm, text="MY bank", font=("Times", "24", "bold"), bg="yellow", anchor="e", fg="black", padx=350, pady=10)
#     w.pack(fill="both")

#     bfm = tk.Frame(root, width=2000, height=50, bg="gray")
#     bfm.pack(side=tk.BOTTOM)

#     w = tk.Label(root, text="Sign Up", font=("Times", "24", "bold"), bg="black", fg="white", padx=350, pady=10)
#     w.pack(padx=10, pady=30)

#     e1 = tk.Entry(root, width=20,   font=("Times", "14", "bold"), bd=3, fg="blue")
#     e1.insert(0, 'Username')
#     e1.pack(padx=150, pady=10)

#     e2 = tk.Entry(root, width=20,   font=("Times", "14", "bold"), bd=3, fg="blue")
#     e2.insert(0, 'Email')
#     e2.pack(padx=150, pady=10)

#     e3 = tk.Entry(root, width=20,   font=("Times", "14", "bold"), bd=3, fg="blue")
#     e3.insert(0, 'Password')
#     e3.pack(padx=150, pady=10)

#     button1 = tk.Button(root, text="Sign Up", width=12, height=1, bg="black",fg="white", bd="8", font=("Helvetica", "12", "bold"))
#     button1.pack(padx=100, pady=20) 

#     root.mainloop()
#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("650x250")

#Get the current screen width and height
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

#Print the screen size
print("Screen width:", screen_width)
print("Screen height:", screen_height)

win.mainloop()

