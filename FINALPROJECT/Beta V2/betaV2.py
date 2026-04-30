from pathlib import Path

from PIL import Image, ImageTk
import tkinter as tk

BASE_DIR = Path(__file__).resolve().parent

root = tk.Tk()
root.geometry("800x300")
root.resizable(False, False)

image_path = BASE_DIR / "background.png"
image = Image.open(image_path).resize((800, 300))
bg_image = ImageTk.PhotoImage(image)


def eat():
    print("Eat button clicked")


def sleep():
    print("Sleep button clicked")


def hit():
    print("Hit button clicked")


def caress():
    print("Caress button clicked")


canvas = tk.Canvas(root, width=800, height=300, highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=bg_image)


def draw_round_button(canvas, x1, y1, x2, y2, radius, color, hover_color, text, text_color, command):
    # 用同一个标签把按钮的图形和文字绑在一起，后面就能一起改颜色和响应点击。
    tag = f"button_{text.lower()}"
    shadow_offset = 3
    border_width = 2
    border_color = "#355126"
    shadow_color = "#23311C"

    def build_round_layer(left, top, right, bottom, corner_radius, fill_color, layer_tag):
        return [
            canvas.create_rectangle(left + corner_radius, top, right - corner_radius, bottom, fill=fill_color, outline=fill_color, tags=layer_tag),
            canvas.create_rectangle(left, top + corner_radius, right, bottom - corner_radius, fill=fill_color, outline=fill_color, tags=layer_tag),
            canvas.create_oval(left, top, left + 2 * corner_radius, top + 2 * corner_radius, fill=fill_color, outline=fill_color, tags=layer_tag),
            canvas.create_oval(right - 2 * corner_radius, top, right, top + 2 * corner_radius, fill=fill_color, outline=fill_color, tags=layer_tag),
            canvas.create_oval(left, bottom - 2 * corner_radius, left + 2 * corner_radius, bottom, fill=fill_color, outline=fill_color, tags=layer_tag),
            canvas.create_oval(right - 2 * corner_radius, bottom - 2 * corner_radius, right, bottom, fill=fill_color, outline=fill_color, tags=layer_tag),
        ]

    build_round_layer(
        x1 + shadow_offset,
        y1 + shadow_offset,
        x2 + shadow_offset,
        y2 + shadow_offset,
        radius,
        shadow_color,
        f"{tag}_shadow",
    )
    border_ids = build_round_layer(x1, y1, x2, y2, radius, border_color, tag)
    part_ids = build_round_layer(
        x1 + border_width,
        y1 + border_width,
        x2 - border_width,
        y2 - border_width,
        max(2, radius - border_width),
        color,
        tag,
    )

    canvas.create_text(
        (x1 + x2) / 2,
        (y1 + y2) / 2,
        text=text,
        fill=text_color,
        font=("Arial", 9, "bold"),
        tags=tag,
    )

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


draw_round_button(canvas, 446, 258, 525, 284, 12, "#7AA95C", "#678F4D", "Eat", "#F5F7EE", eat)
draw_round_button(canvas, 531, 258, 610, 284, 12, "#88B86B", "#739D59", "Sleep", "#F5F7EE", sleep)
draw_round_button(canvas, 616, 258, 695, 284, 12, "#5F8E4C", "#4F7840", "Hit", "#F5F7EE", hit)
draw_round_button(canvas, 701, 258, 780, 284, 12, "#9BC782", "#84AD6D", "Caress", "#F5F7EE", caress)

root.mainloop()
