import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(initialdir='/home/zubakker/Pictures')
print(file_path)
