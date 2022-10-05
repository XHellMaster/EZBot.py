import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkf
import os

main_window = tk.Tk(screenName="Main Screen")
main_window.title('EZ Bot')
bgimg = tk.PhotoImage(file=os.getcwd()+"\\resources\\background.ppm")
bg = ttk.Label(main_window, image=bgimg, anchor=tk.W)
bg.pack()
title = ttk.Label(main_window, text="EZBot: the easiest way to make discord bots", foreground="white", compound="top", font=("Impact", 40))
for name in sorted(tkf.families()):
    print(name)
main_window.mainloop()

