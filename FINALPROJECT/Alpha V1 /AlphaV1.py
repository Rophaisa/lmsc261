import tkinter as tk
root = tk.Tk()
root.geometry("600x600")
root.config(background= "#FFB6C1")


#user inputface 交互按钮
button = tk.Button(root, text="Eat")
button.pack()

button = tk.Button(root, text="Sleep")
button.pack()

button = tk.Button(root, text="Hit")
button.pack()

button = tk.Button(root, text="Stroke")
button.pack()

root.mainloop()