import Tkinter as tk
import ttk

win = tk.Tk()
frame = ttk.Frame()
win.title("Python GUI")


tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab2")

ttk.Label(tab1, text="Hello, this is a tab").grid(column=0, row=0)
ttk.Label(tab2, text="Hello, this is another tab").grid(column=0, row=0)

tabControl.pack(expand=0, fill="both")

win.mainloop()
