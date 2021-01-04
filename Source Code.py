# necessary  libraries
import tkinter as tk
import os
import shutil
import subprocess
from tkinter import messagebox as tkmb

# default window stuff to make it look nice
Height = 200
Width = 400

root = tk.Tk()
root.title("Pikuniku Save Manager")

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

frame = tk.Frame(root, bg="#b3b3b3")
frame.place(relwidth=0.99, relheight=0.99, relx=0.005, rely=0.005)

# select save button
savelist = [f for f in os.listdir('.\\Pikuniku Saves')]
save = tk.StringVar()
save.set("Select Savestate")
selectsave = tk.OptionMenu(root, save, *savelist)
selectsave.place(relwidth=0.5, relheight=0.15, relx=0.1, rely=0.1)

# open saves folder button
def osffunction():
    subprocess.Popen('explorer ".\\Pikuniku Saves"')


openfolder = tk.Button(root, text="Open saves folder", command=lambda: osffunction())
openfolder.place(anchor='ne', relwidth=0.27, relheight=0.15, relx=0.9, rely=0.1)

# select game version button
version = tk.StringVar()
version.set("Select Version")
selectversion = tk.OptionMenu(root, version, "Steam", "Epic")
selectversion.place(anchor='nw', relwidth=0.27, relheight=0.15, relx=0.1, rely=0.5)

# suidget button functionality
def suidgetfunction():
    subprocess.Popen('explorer "C:\\Program Files (x86)\\Steam\\userdata"')

# steam user id entry (suid), the text above it (suidex) and the button to get it (suidget)
suid = tk.Entry(root)
suid.place(anchor='ne', relwidth=0.5, relheight=0.15, relx=0.9, rely=0.5)
suidex = tk.Label(root, text="User id (steam only)", bg="#b3b3b3", anchor='w')
suidex.place(anchor='se', relwidth=0.5, relheight=0.1, relx=0.9, rely=0.5)
suidget = tk.Button(root, text="get", command=lambda: suidgetfunction())
suidget.place(anchor='se', relwidth=0.1, relheight=0.12, relx=0.9, rely=0.5)

# set save button functionality
def setsavefunction():
    if save.get() == "Select Savestate":
        tkmb.showerror(title="Error", message="Please select a savestate")
    else:
        # Copy the files to the steam save location
        if version.get() == "Steam":
            try:
                originalsteam = r'.\\Pikuniku Saves\\%s'
                originalsteam = originalsteam % (save.get())
                targetsteam = r'C:\\Program Files (x86)\\Steam\\userdata\\%s\\572890\\remote\\PikunikuSaveFile'
                targetsteam = targetsteam % (suid.get())
                shutil.copy(originalsteam, targetsteam)
                tkmb.showinfo(title="Confirmation", message="Done!")
            except:
                tkmb.showerror(title="Error", message="Please enter your steam user id (read the README.txt for more info)")
        elif version.get() == "Epic":
            # Copy the files to the epic save location
            originalepic = r'.\\Pikuniku Saves\\%s'
            originalepic = originalepic % (save.get())
            targetepic = os.getenv('APPDATA')
            targetepic = targetepic + "\\..\\LocalLow\\Sectordub\\Pikuniku\\saves\\PikunikuSaveFile_Epic"
            shutil.copy(originalepic, targetepic)
            tkmb.showinfo(title="Confirmation", message="Done!")
        else:
            tkmb.showerror(title="Error", message="Please select a platform")


# export current save button functionality
def expsavefunction():
    if version.get() == "Steam":
        currsavesteam = r'C:\\Program Files (x86)\\Steam\\userdata\\%s\\572890\\remote'
        currsavesteam = currsavesteam % (suid.get())
        shutil.copy(currsavesteam, r'.\\Pikuniku Saves\\Exported Save (Steam))')
        tkmb.showinfo(title="Confirmation", message="Done!")
    elif version.get() == "Epic":
        currsaveepic = os.getenv('APPDATA')
        currsaveepic = currsaveepic + "\\..\\LocalLow\\Sectordub\\Pikuniku\\saves\\PikunikuSaveFile_Epic"
        shutil.copy(currsaveepic, r'.\\Pikuniku Saves\\Exported Save (Epic)')
        tkmb.showinfo(title="Confirmation", message="Done!")
    else:
        tkmb.showerror(title="Error", message="Please select a platform")

# set save button
setsave = tk.Button(root, text="Set selected save", command=lambda: setsavefunction())
setsave.place(relwidth=0.3, relheight=0.15, relx=0.1, rely=0.8)

# export current save button
exportsave = tk.Button(root, text="Export current save", command=lambda: expsavefunction())
exportsave.place(anchor='ne', relwidth=0.3, relheight=0.15, relx=0.9, rely=0.8)


root.mainloop()
