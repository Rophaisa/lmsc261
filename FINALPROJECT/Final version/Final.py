import tkinter as tk
root = tk.Tk()
root.geometry("1200x450")
canvas = tk.Canvas(root, width=1200, height=450, )
canvas.pack() #把画布真正显示到窗口里，不pack的话画布不会出现。

#导入工具，创建路径
from pathlib import Path #导入Path，后面用“文件夹/文件名”的方式拼接路径。
from PIL import Image, ImageTk #Image 负责读图和缩放，ImageTk 负责把 PIL 图片转成 tkinter 能显示的图片对象。

BASE_DIR = Path(__file__).resolve().parent #拿到当前这个 Python 文件所在的文件夹，后面所有帧文件夹都从这里开始找。
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 450

BG_FRAMES_DIR = BASE_DIR / "bg" #背景待机动画的帧文件夹路径，指向对应工程目录下的bg文件夹。
EAT_FRAMES_DIR = BASE_DIR / "eat"
HIT_FRAMES_DIR = BASE_DIR / "hit"
CARESS_FRAMES_DIR = BASE_DIR / "caress"


#帧列表读取函数
def load_video_frames(video_path): #定义函数，输入某个帧文件夹路径，输出“这一组图片帧列表”和默认播放帧率
    frame_files = sorted(video_path.glob("*.png"))
    # 解释：读取这个文件夹里所有 png 图片，并按文件名排序，确保动画顺序正确。
    fps = 24.0
    # 解释：先把这一组动画的默认播放速度设为每秒 24 帧。

    frames = []
    # 解释：准备一个空列表，后面把每一张转好的图片帧依次装进去。
    for frame_file in frame_files:
        # 解释：按顺序遍历文件夹里的每一张 png 帧图。
        with Image.open(frame_file) as image:
            # 解释：打开当前这张图片，并在 with 结束后自动关闭文件。
            image = image.resize((WINDOW_WIDTH, WINDOW_HEIGHT), Image.Resampling.BILINEAR)
            # 解释：把当前图片缩放成和窗口一样大，BILINEAR 是一种比较平滑的缩放方式。
        frames.append(ImageTk.PhotoImage(image))
        # 解释：把 PIL 图片转成 tkinter 能显示的图片对象，再追加进 frames 列表。

    return frames, fps
    # 解释：把整组帧列表和对应的帧率一起返回给外面使用。

idle_frames, idle_fps = load_video_frames(BG_FRAMES_DIR)
# 解释：读取背景待机动画文件夹，得到背景动画的所有帧和它的播放帧率。
eat_frames, eat_fps = load_video_frames(EAT_FRAMES_DIR)
# 解释：读取吃饭动画文件夹，得到 eat 动画的所有帧和它的播放帧率。
hit_frames, hit_fps = load_video_frames(HIT_FRAMES_DIR)
# 解释：读取 hit 动画文件夹，得到击打动画的所有帧和它的播放帧率。
caress_frames, caress_fps = load_video_frames(CARESS_FRAMES_DIR)
# 解释：读取 caress 动画文件夹，得到抚摸动画的所有帧和它的播放帧率。

current_image = idle_frames[0]
# 解释：先把当前正在显示的图片设成背景动画的第 1 帧，程序启动时就能先看到一张图。
bg_item = canvas.create_image(0, 0, anchor="nw", image=current_image)
# 解释：在画布左上角创建一张图片对象，后面动画播放时就是不断替换这张图。
canvas.tag_lower(bg_item)
# 解释：把背景图片压到最底层，这样后面画出来的按钮才能显示在它上面。

video_after_id = None
# 解释：先准备一个变量保存 after 定时器的编号，后面停止动画时要靠它取消定时任务。

def stop_video():
    # 解释：定义一个停止当前动画播放的函数，切换动画前会先调用它。
    global video_after_id
    # 解释：声明下面要修改的是外面的全局变量 video_after_id，不是函数里的临时变量。
    if video_after_id is not None:
        # 解释：如果当前真的存在一个尚未执行的 after 定时任务，就进入这里。
        root.after_cancel(video_after_id)
        # 解释：取消上一次安排好的下一帧播放任务，避免两个动画同时往前跑。
        video_after_id = None
        # 解释：取消成功后把编号清空，表示当前没有挂着的定时任务了。

def play_video(frames, fps, loop=False, on_complete=None):
    # 解释：定义通用播放函数，输入一组帧、播放速度、是否循环、播完后要做什么。
    global video_after_id, current_image
    # 解释：声明下面会修改全局的定时器编号和当前正在显示的图片对象。

    stop_video()
    # 解释：每次切换动画前先停掉上一段，避免不同动画互相打架。
    delay = max(1, int(1000 / fps))
    # 解释：把“每秒多少帧”换算成“每帧隔多少毫秒”，after 用的是毫秒单位。

    def show_frame(index):
        # 解释：这是内部小函数，负责真正显示某一帧，并安排下一帧。
        global video_after_id, current_image
        # 解释：这里也要改全局变量，所以再声明一次 global。

        current_image = frames[index]
        # 解释：从 frames 列表里取出当前索引对应的那一张图片，作为当前显示帧。
        canvas.itemconfig(bg_item, image=current_image)
        # 解释：把画布上的背景图片对象换成这一帧，于是视觉上就像动画在动。

        next_index = index + 1
        # 解释：先把下一帧索引默认设成“当前帧 + 1”。
        if next_index >= len(frames):
            # 解释：如果下一帧已经超过这组动画的最后一张，就说明这段动画要结束了。
            if loop:
                # 解释：如果这一段动画设置成循环播放，就走这里。
                next_index = 0
                # 解释：把索引重新跳回第 0 张，从头开始继续循环。
            else:
                # 解释：如果不是循环动画，就说明这段动画播完要停下。
                video_after_id = None
                # 解释：先把定时器编号清空，表示这段动画不再安排下一帧。
                if on_complete is not None:
                    # 解释：如果外面还传进来了“播完后回调函数”，就走这里。
                    on_complete()
                    # 解释：执行播完后的动作，比如 eat/hit/caress 播完后切回背景。
                return
                # 解释：结束这次 show_frame，不再往下安排新帧。

        video_after_id = root.after(delay, lambda: show_frame(next_index))
        # 解释：告诉 tkinter 过 delay 毫秒后再次调用 show_frame，并去显示下一帧。

    show_frame(0)
    # 解释：从第 0 帧开始播放当前这段动画。

def start_background_video():
    # 解释：定义一个专门启动背景待机动画的函数，后面多个地方都会复用。
    play_video(idle_frames, idle_fps, loop=True)
    # 解释：播放背景帧列表，并把 loop 设成 True，让背景动画一直循环。

def eat():
    # 解释：定义 Eat 按钮被点击时要执行的函数。
    print("Eat button clicked")
    # 解释：先在终端打印一句调试信息，方便你确认点击事件有没有触发。
    play_video(eat_frames, eat_fps, loop=False, on_complete=start_background_video)
    # 解释：播放 eat 动画一次，播完后自动调用 start_background_video 回到待机背景。

def hit():
    # 解释：定义 Hit 按钮被点击时要执行的函数。
    print("Hit button clicked")
    # 解释：先在终端打印一句调试信息，方便排查按钮有没有点到。
    play_video(hit_frames, hit_fps, loop=False, on_complete=start_background_video)
    # 解释：播放 hit 动画一次，播完以后自动切回背景循环动画。

def caress():
    # 解释：定义 Caress 按钮被点击时要执行的函数。
    print("Caress button clicked")
    # 解释：先打印调试信息，方便确认这个按钮函数有被调用。
    play_video(caress_frames, caress_fps, loop=False, on_complete=start_background_video)
    # 解释：播放 caress 动画一次，结束后自动回到背景动画。




#创建画圆角按钮函数（整体）到时候塞进去  左上角x1y1, 右下角x2y2, 按钮颜色，鼠标移动上去颜色，按钮文字，文字颜色，点下去执行的命令
def draw_button(canvas, x1, y1, x2, y2, color, hover_color, text, text_color, command):
    # 解释：定义一个通用按钮绘制函数，把按钮位置、颜色、文字和点击动作都参数化。
    tag = f"button_{text.lower()}" #按钮由多个图形拼起来，挂上同一个标签，后面就能把它们当成一个整体处理。给这个按钮起一个标签名, f是格式化字符串，文字变小写
    # 解释：给这个按钮生成统一标签，比如 Eat 会变成 button_eat，后面绑定事件时会用到。
    shadow_offset = 3 #阴影偏移
    # 解释：设置阴影层相对按钮本体向右下偏移多少像素。
    border_width = 2 #边框粗细
    # 解释：设置边框厚度，后面用它决定内层按钮向里缩多少。
    border_color = "#355126" #边框颜色
    # 解释：定义按钮边框默认颜色。
    shadow_color = "#23311C" #每个按钮阴影颜色
    # 解释：定义按钮阴影层颜色，让按钮有一点立体感。

    #开始画, 左上右下角边界，颜色，这一涂层的标签
    def build_button(left, top, right, bottom, fill_color, layer_tag):
        # 解释：定义一个内部小函数，专门画“胶囊形”的某一层图形。
        r = (bottom - top) / 2 #按钮的矩形的高度，用高度除以二就是半圆半径
        # 解释：按钮高度的一半就是左右圆头的半径，这样才能拼成胶囊形状。
        return [
            # 解释：返回一个列表，里面装这一层每个图形的 ID，后面换颜色时会用到。
            canvas.create_rectangle(left + r, top, right - r, bottom, fill=fill_color, outline=fill_color, tags=layer_tag), #画矩形
            # 解释：先画中间的长方形部分，左右各留出一个半圆的空间。
            canvas.create_oval(left, top, left + 2 * r, bottom, fill=fill_color, outline=fill_color, tags=layer_tag), #左圆
            # 解释：再画左边的圆头，让按钮左端变成圆角胶囊形。
            canvas.create_oval(right - 2 * r, top, right, bottom, fill=fill_color, outline=fill_color, tags=layer_tag), #右圆
            # 解释：最后画右边的圆头，和中间矩形拼成完整胶囊按钮。
        ]
        # 解释：把当前这一层的所有图形 ID 返回出去。

    #调用build的函数去画阴影
    build_button(
        # 解释：开始调用 build_button 先画按钮最底下的阴影层。
        x1 + shadow_offset,
        # 解释：阴影层左边界比按钮本体向右偏移 shadow_offset 像素。
        y1 + shadow_offset,
        # 解释：阴影层上边界比按钮本体向下偏移 shadow_offset 像素。
        x2 + shadow_offset,
        # 解释：阴影层右边界也同步向右偏移，保持整体形状不变。
        y2 + shadow_offset,
        # 解释：阴影层下边界也同步向下偏移，形成右下方的投影效果。
        shadow_color, f"{tag}_shadow")
        # 解释：这一层使用阴影颜色，并用单独的 shadow 标签标记出来。

    #继续画轮廓
    border_ids = build_button(x1, y1, x2, y2, border_color, tag)
    # 解释：再画按钮的边框层，并把这一层所有图形的 ID 保存到 border_ids 里。

    part_ids = build_button(
        # 解释：继续画按钮内部真正显示颜色的填充层。
        x1 + border_width,
        # 解释：填充层左边向里缩 border_width，边框才会露出来。
        y1 + border_width,
        # 解释：填充层上边也向里缩同样的宽度。
        x2 - border_width,
        # 解释：填充层右边向里缩，保持左右边框厚度一致。
        y2 - border_width,
        # 解释：填充层下边也向里缩，保持上下边框厚度一致。
        color, tag)
        # 解释：这一层使用按钮默认填充颜色，并且和按钮本体共用同一个标签。

    canvas.create_text(
        # 解释：在按钮的中央添加文字，让用户知道这个按钮的功能。
        (x1 + x2) / 2,
        # 解释：文字的 x 坐标取左右边界中点，保证水平居中。
        (y1 + y2) / 2,
        # 解释：文字的 y 坐标取上下边界中点，保证垂直居中。
        text=text,
        # 解释：显示的文字内容来自外面传进来的 text 参数。
        fill=text_color,
        # 解释：文字颜色来自外面传进来的 text_color 参数。
        font=("Arial", 14, "bold"), tags=tag)
        # 解释：设置文字字体样式，并把文字也归到按钮同一个标签里。

    #鼠标移动交互
    def on_enter(event):
        # 解释：定义鼠标移入按钮区域时执行的悬停效果函数。
        for part_id in part_ids:
            # 解释：依次遍历填充层里的每一个图形 ID。
            canvas.itemconfig(part_id, fill=hover_color, outline=hover_color)
            # 解释：把填充层颜色改成 hover_color，形成鼠标移上去时的高亮效果。
        for border_id in border_ids:
            # 解释：再依次遍历边框层里的每一个图形 ID。
            canvas.itemconfig(border_id, fill="#446735", outline="#446735")
            # 解释：把边框也稍微提亮一点，让悬停状态更明显。

    def on_leave(event):
        # 解释：定义鼠标离开按钮区域时执行的恢复效果函数。
        for part_id in part_ids:
            # 解释：依次遍历填充层，把它们恢复成默认颜色。
            canvas.itemconfig(part_id, fill=color, outline=color)
            # 解释：把填充层恢复成初始按钮颜色。
        for border_id in border_ids:
            # 解释：依次遍历边框层，把它们也恢复成初始颜色。
            canvas.itemconfig(border_id, fill=border_color, outline=border_color)
            # 解释：把边框颜色恢复成原本的 border_color。

    canvas.tag_bind(tag, "<Enter>", on_enter)
    # 解释：把鼠标移入事件绑定到这个按钮标签上，移进去时调用 on_enter。
    canvas.tag_bind(tag, "<Leave>", on_leave)
    # 解释：把鼠标移出事件绑定到这个按钮标签上，离开时调用 on_leave。
    canvas.tag_bind(tag, "<Button-1>", lambda event: command())
    # 解释：把鼠标左键点击事件绑定到按钮标签上，点击时执行传进来的 command 函数。

#直接输入创建
draw_button(canvas, 797, 387, 915, 426,"#7AA95C", "#678F4D", "Eat", "#F5F7EE", eat)
# 解释：在画布上创建第一个 Eat 按钮，位置、颜色和点击后执行的函数都在这里传进去。
draw_button(canvas, 924, 387, 1043, 426, "#5F8E4C", "#4F7840", "Hit", "#F5F7EE", hit)
# 解释：在画布上创建第二个 Hit 按钮，点击它会播放 hit 动画。
draw_button(canvas, 1052, 387, 1170, 426, "#9BC782", "#84AD6D", "Caress", "#F5F7EE", caress)
# 解释：在画布上创建第三个 Caress 按钮，点击它会播放 caress 动画。



start_background_video()
# 解释：程序启动后先立刻开始播放背景待机动画，这样窗口一打开就不是静止图。
root.mainloop()
# 解释：进入 tkinter 的事件循环，窗口、按钮点击和动画播放都会在这里持续运行。
