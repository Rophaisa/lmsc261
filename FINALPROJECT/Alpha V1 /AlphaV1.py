import tkinter as tk
root = tk.Tk()
root.geometry("1200x450")

canvas = tk.Canvas(root, width=1200, height=450, )
canvas.pack()

#按钮eat
def eat():
    print("Eat button clicked")
#按钮caress
def caress():
    print("Caress button clicked")
#按钮hit
def hit():
    print("Hit button clicked")

#创建画圆角按钮函数（整体）到时候塞进去
def drawbutton(canvas, x1, y1, x2, y2, color, hover_color, text, text_color, command):
    tag = f"button_{text.lower()}" #给这个按钮起一个标签名, f是格式化字符串，文字变小写
    shadow_offset = 3 #阴影偏移
    border_width = 2 #边框粗细
    border_color = "#355126" #边框颜色
    shadow_color = "#23311C" #每个按钮阴影颜色

    height = y2 - y1
    radius = height / 2

    #Layer1 建立半圆
    def buildcapsule(left, top, right, bottom, fill_color, layer_tag):
        r = (bottom - top) / 2
        return [
            canvas.create_rectangle(left + r, top, right - r, bottom, fill=fill_color, outline=fill_color, tags=layer_tag),
            canvas.create_oval(left, top, left + 2 * r, bottom, fill=fill_color, outline=fill_color, tags=layer_tag),
            canvas.create_oval(right - 2 * r, top, right, bottom, fill=fill_color, outline=fill_color, tags=layer_tag),
        ]

    
    buildcapsule(
        x1 + shadow_offset,
        y1 + shadow_offset,
        x2 + shadow_offset,
        y2 + shadow_offset,
        shadow_color, f"{tag}_shadow")


    border_ids = buildcapsule(x1, y1, x2, y2, border_color, tag)

    part_ids = buildcapsule(
        x1 + border_width,
        y1 + border_width,
        x2 - border_width,
        y2 - border_width,
        color, tag)

    canvas.create_text(
        (x1 + x2) / 2,
        (y1 + y2) / 2,
        text=text,
        fill=text_color,
        font=("Arial", 14, "bold"), tags=tag)

    def on_enter(event):
        for part_id in part_ids:
            canvas.itemconfig(part_id, fill=hover_color, outline=hover_color)
        for border_id in border_ids:
            canvas.itemconfig(border_id, fill="#446735", outline="#446735")

    def on_leave(event):
        for part_id in part_ids:
            canvas.itemconfig(part_id, fill=color, outline=color)
        for border_id in border_ids:
            canvas.itemconfig(border_id, fill=border_color, outline=border_color)

    canvas.tag_bind(tag, "<Enter>", on_enter)
    canvas.tag_bind(tag, "<Leave>", on_leave)
    canvas.tag_bind(tag, "<Button-1>", lambda event: command())

drawbutton(canvas, 797, 387, 915, 426,"#7AA95C", "#678F4D", "Eat", "#F5F7EE", eat)
drawbutton(canvas, 924, 387, 1043, 426, "#5F8E4C", "#4F7840", "Hit", "#F5F7EE", hit)
drawbutton(canvas, 1052, 387, 1170, 426, "#9BC782", "#84AD6D", "Caress", "#F5F7EE", caress)



root.mainloop()