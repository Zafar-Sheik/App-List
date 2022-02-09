from cProfile import label
from cgitb import text
from distutils import command
from fileinput import filename
import tkinter as tk 
from tkinter import Canvas, filedialog, Text
import os  #Run apps that added to this app.

root = tk.Tk() #GUI root 
apps = []

if os.path.isfile('save.txt'):
    with open ('save.txt' , 'r') as f :
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()] #if x.strip (white lines) then remove

def addApps():
    for widget in frame.winfo_children():
        widget.destroy() #push updated list to screen

    filename = filedialog.askopenfilename(initialdir="/",title="Select File",
                                          filetypes=(("executables","*.exe"),("all files" , "*.*")))

    apps.append(filename)   
    print(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

#Following code taken from: YouTube 
#Author: Dev Ed
#Url: https://www.youtube.com/watch?v=jE-SpRI3K5g
def runApp () :
    for app in apps:
        os.startfile(app)                            
        
canvas = tk.Canvas(root, height = 500, width = 500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white" )
frame.place(relwidth = 0.8, relheight= 0.8 , relx=0.1, rely=0.1)

btnOpenFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApps)
btnOpenFile.pack()

btnRunApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command= runApp )
btnRunApps.pack()

for app in apps :
    label = tk.Label(frame,text= app)
    label.pack()

root.mainloop()

with open ('save.txt' , 'w') as f :
    for app in apps:
        f.write(app + ',')


