from PIL import Image, ImageTk

import tkinter as tk
root = tk.Tk()
root.geometry("800x300")
#读取图片
image = Image.open("background.png")

#调整图片大小
image = image.resize((800, 300))
bg_image = ImageTk.PhotoImage(image)


bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


#user inputface 交互按钮
#eat
def eat():
    print("Eat button clicked")

eat_button = tk.Button(root, text="Eat", command=eat)
eat_button.place(x=150, y=265)

#sleep
def sleep():
    print("Sleep button clicked")

sleep_button = tk.Button(root, text="Sleep", command=sleep)
sleep_button.place(x=300, y=265)

#hit
def hit():
    print("Hit button clicked")

Hit_button = tk.Button(root, text="Hit", command=hit)
Hit_button.place(x=450, y=265)

#stroke
def stroke():
    print("Stroke button clicked")

Stroke_button = tk.Button(root, text="Stroke", command=stroke)
Stroke_button.place(x=600, y=265)

root.mainloop()
