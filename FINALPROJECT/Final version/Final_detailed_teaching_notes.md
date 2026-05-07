# `Final.py` 逐行教学笔记

这份笔记对应文件：`FINALPROJECT/Final version/Final.py`

阅读方式建议：

1. 先看“常见单词和标点速查”，把最基础的语法认熟。
2. 再按“逐行解释”对照 `Final.py` 看。
3. 最后回到代码里自己顺着运行流程讲一遍：
   从“创建窗口” -> “读取帧图” -> “播放背景” -> “点击按钮切换动作”。

---

## 常见单词速查

这些词在你的 `Final.py` 里反复出现，先知道它们的大意，后面逐行看会轻松很多。

- `import`：导入模块。
- `from`：从某个模块里取出指定内容。
- `as`：取别名，让后面写起来更短。
- `def`：定义函数。
- `return`：把结果返回给外面。
- `if`：如果条件成立，就执行下面代码。
- `for`：循环，一个一个处理。
- `with`：在一个受控环境里做事，结束后自动收尾。
- `global`：告诉 Python，这里改的是外面的全局变量。
- `lambda`：写一个很短的小函数。
- `None`：空值，表示“现在没有东西”。
- `True`：真。
- `False`：假。
- `not`：取反。
- `is not`：不是同一个值，常用于判断是不是 `None`。
- `in`：在……里面。
- `sorted(...)`：把内容排好顺序。
- `len(...)`：求长度。
- `int(...)`：转成整数。
- `max(...)`：取较大的那个值。
- `print(...)`：在终端输出一行信息。

---

## 常见标点和符号速查
- `#`：注释开始，`#` 后面的内容给人看，Python 运行时会忽略。
- `=`：赋值，把右边结果放进左边变量。
- `()`：函数调用、方法调用，或者把参数包起来。
- `[]`：列表，或者列表下标取值。
- `:`：表示下面要开始一个缩进代码块，比如函数体、`if`、`for`。
- `,`：分隔多个参数、多个变量、多个元素。
- `.`：访问“某个对象里的东西”，比如方法、属性。
- `"`：字符串。
- `'`：也是字符串，这份代码里主要用双引号。
- `_`：变量名的一部分，也常用来让名字更易读，比如 `video_after_id`。
- `+`：加法，或者把数字往右/往下偏移。
- `-`：减法，或者往左/往上收缩。
- `*`：乘法，这里常见于 `2 * r`。
- `/`：在 `Path` 对象里不是除法，而是“拼接路径”。

### 1-6：创建窗口和画布

- L1 `import tkinter as tk`
  `import` 表示导入模块；`tkinter` 是 Python 自带 GUI 库；`as tk` 是给它起别名。  
  这一行的整体作用：后面你可以用更短的 `tk` 来写 `tk.Tk()`、`tk.Canvas()`。

- L2 `root = tk.Tk()`
  `root` 是变量名；`=` 是赋值；`tk.Tk()` 是调用 tkinter 里的主窗口构造器。  
  整体作用：创建整个程序最外层的窗口。

- L3 `root.geometry("1200x450")`
  `root.geometry(...)` 是给窗口设置大小；字符串 `"1200x450"` 的意思是宽 1200、高 450。  
  整体作用：规定窗口初始尺寸。

- L4 `canvas = tk.Canvas(root, width=1200, height=450, )`
  `tk.Canvas(...)` 是创建画布；第一个参数 `root` 表示把画布放进主窗口；`width=` 和 `height=` 是关键字参数；最后那个逗号 `,` 在 Python 里允许保留，方便以后继续加参数。  
  整体作用：准备一个能画图片、文字、图形的区域。

- L5 `canvas.pack()
  `canvas.pack()` 是布局方法；后面的 `#` 注释是写给人看的。  
  整体作用：把刚才创建好的画布真正放到窗口里显示出来。

### 7-19：导入工具和准备路径

- L8 `from pathlib import Path #导入Path，后面用“文件夹/文件名”的方式拼接路径。`
  `from pathlib import Path` 表示只从 `pathlib` 模块里拿 `Path` 这个类。  
  整体作用：后面可以方便地处理文件夹和文件路径。

- L9 `from PIL import Image, ImageTk #Image 负责读图和缩放，ImageTk 负责把 PIL 图片转成 tkinter 能显示的图片对象。`
  `from PIL import ...` 表示从 Pillow 图像库里导入两个工具；逗号 `,` 用来分隔两个名字。  
  整体作用：`Image` 负责打开和缩放图片，`ImageTk` 负责把图片变成 tkinter 可显示对象。


- L11 `BASE_DIR = Path(__file__).resolve().parent
  `__file__` 是 Python 提供的当前文件路径；`Path(__file__)` 把它变成路径对象；`.resolve()` 取绝对路径；`.parent` 取父文件夹。  
  整体作用：拿到 `Final.py` 所在目录，后面 `bg/eat/hit/caress` 都从这里往下找。

- L12 `WINDOW_WIDTH = 1200`
  用常量变量保存窗口宽度。  
  整体作用：后面多处都要用 1200，不必反复手写。

- L13 `WINDOW_HEIGHT = 450`
  用常量变量保存窗口高度。  
  整体作用：和宽度一起作为统一显示尺寸。

- L15 `BG_FRAMES_DIR = BASE_DIR / "bg" #背景待机动画的帧文件夹路径，指向对应工程目录下的bg文件夹。`
  这里的 `/` 不是除法，而是 `Path` 提供的“拼路径”语法。  
  整体作用：得到背景帧文件夹路径。

- L16 `EAT_FRAMES_DIR = BASE_DIR / "eat"`
  整体作用：得到 `eat` 动画帧文件夹路径。

- L17 `HIT_FRAMES_DIR = BASE_DIR / "hit"`
  整体作用：得到 `hit` 动画帧文件夹路径。

- L18 `CARESS_FRAMES_DIR = BASE_DIR / "caress"`
  整体作用：得到 `caress` 动画帧文件夹路径。

### 20-40：读取帧文件夹

- L22 `def load_video_frames(video_path): #定义函数，输入某个帧文件夹路径，输出“这一组图片帧列表”和默认播放帧率`
  `def` 表示定义函数；`load_video_frames` 是函数名；`video_path` 是参数名；`:` 表示函数体开始。  
  整体作用：做一个“输入文件夹，输出帧列表和帧率”的工具函数。

- L23 `frame_files = sorted(video_path.glob("*.png"))`
  `video_path.glob("*.png")` 表示找这个文件夹下所有 `png` 文件；`"*.png"` 里 `*` 是通配符；`sorted(...)` 负责按文件名排序。  
  整体作用：按顺序拿到这组动画的全部图片文件。

- L25 `fps = 24.0`
  这里把帧率固定成 `24.0`。  
  整体作用：默认按每秒 24 帧来播放这一组图片。

- L28 `frames = []`
  `[]` 表示空列表。  
  整体作用：先准备一个空容器，后面每读到一张帧图就往里面放。

- L30 `for frame_file in frame_files:`
  `for` 表示循环；`frame_file` 是每次循环里当前那张图片文件；`in` 表示“从 frame_files 里一个个取”。  
  整体作用：开始逐张处理帧图。

- L32 `with Image.open(frame_file) as image:`
  `Image.open(...)` 打开图片；`with ... as ...` 表示在受控环境里使用资源；`as image` 给打开后的图片对象起名字。  
  整体作用：打开当前这一张图片，并保证用完后自动收尾。

- L34 `image = image.resize((WINDOW_WIDTH, WINDOW_HEIGHT), Image.Resampling.BILINEAR)`
  `resize(...)` 是缩放方法；括号里第一个参数是目标尺寸元组 `(宽, 高)`；第二个参数是缩放算法。  
  整体作用：把每张帧图都缩到和窗口一样大。

- L36 `frames.append(ImageTk.PhotoImage(image))`
  `.append(...)` 表示把一个元素加到列表末尾；`ImageTk.PhotoImage(...)` 把 PIL 图片转成 tkinter 图片对象。  
  整体作用：把当前处理好的帧图加入播放列表。

- L39 `return frames, fps`
  `return` 把结果交回函数外面；逗号表示一次返回两个值。  
  整体作用：把“整组帧图列表”和“这一组帧率”一起返回。

### 41-56：预加载动画和创建背景图层

- L42 `idle_frames, idle_fps = load_video_frames(BG_FRAMES_DIR)`
  左边两个变量用逗号拆开，右边函数返回两个值，所以这是“解包赋值”。  
  整体作用：读取背景动画帧和帧率。

- L44 `eat_frames, eat_fps = load_video_frames(EAT_FRAMES_DIR)`
  整体作用：读取 eat 动画帧和帧率。

- L46 `hit_frames, hit_fps = load_video_frames(HIT_FRAMES_DIR)`
  整体作用：读取 hit 动画帧和帧率。

- L48 `caress_frames, caress_fps = load_video_frames(CARESS_FRAMES_DIR)`
  整体作用：读取 caress 动画帧和帧率。

- L51 `current_image = idle_frames[0]`
  `idle_frames[0]` 表示取背景动画列表中的第 1 张图；Python 下标从 0 开始。  
  整体作用：把程序启动时默认显示图片设成背景动画的第一帧。

- L53 `bg_item = canvas.create_image(0, 0, anchor="nw", image=current_image)`
  `canvas.create_image(...)` 在画布上放一张图片；`0, 0` 是坐标；`anchor="nw"` 表示以左上角作为定位点。  
  整体作用：在画布上创建一个“背景图片对象”，后面动画就是不断换它的内容。

- L55 `canvas.tag_lower(bg_item)`
  `tag_lower(...)` 把某个画布对象压到更底层。  
  整体作用：确保背景图在按钮下面，不会挡住按钮。

### 57-79：停止动画和播放动画

- L58 `video_after_id = None`
  用 `None` 初始化一个变量，表示“目前没有挂着的定时任务”。  
  整体作用：后面用这个变量保存 `root.after(...)` 返回的编号。

- L61 `def stop_video():`
  定义停止动画函数。  
  整体作用：切换动作前，先取消上一个还没执行的下一帧任务。

- L63 `global video_after_id`
  `global` 表示这里要操作外面的全局变量，不是局部变量。  
  整体作用：让函数里能修改最外面的 `video_after_id`

- L65 `if video_after_id is not None:`
  `if` 做条件判断；`is not None` 表示“不是空值”。  
  整体作用：只有当当前真的有 after 定时器时，才去取消。

- L67 `root.after_cancel(video_after_id)`
  `after_cancel(...)` 是 tkinter 的取消定时任务方法。  
  整体作用：取消上一段动画安排好的“下一帧播放”。

- L69 `video_after_id = None`
  取消后把编号清空。  
  整体作用：表示现在没有待执行的下一帧任务。

- L72 `def play_video(frames, fps, loop=False, on_complete=None):`
  这是总播放函数；`frames` 是一组图片；`fps` 是速度；`loop=False` 表示默认不循环；`on_complete=None` 表示默认播完后不额外执行东西。  
  整体作用：统一控制所有动画怎么播放。

- L74 `global video_after_id, current_image`
  用逗号一次声明两个全局变量。  
  整体作用：这个函数里会修改“当前定时器编号”和“当前显示图片”。

- L77 `stop_video()`
  先调用停止函数。  
  整体作用：每次开始新动画前，先把旧动画收掉。

- L79 `delay = max(1, int(1000 / fps))`
  `1000 / fps` 把“每秒几帧”换成“每帧几毫秒”；`int(...)` 取整；`max(1, ...)` 保证最小延迟至少 1 毫秒。  
  整体作用：计算 after 定时器每隔多久切一次帧。

### 81-115：内部播放循环 `show_frame`

- L82 `def show_frame(index):`
  在 `play_video` 里面再定义一个内部函数。  
  整体作用：专门负责“显示第几帧”和“安排下一帧”。

- L84 `global video_after_id, current_image`
  继续声明要改全局状态。  
  整体作用：保证内部函数也能改外层保存的当前图片和定时器编号。

- L87 `current_image = frames[index]`
  从帧列表里拿出当前下标对应的那一张图片。  
  整体作用：决定当前这一帧到底显示什么。

- L89 `canvas.itemconfig(bg_item, image=current_image)`
  `itemconfig(...)` 是修改画布对象配置的方法。  
  整体作用：把背景图对象换成当前帧，于是看起来像动画在播放。

- L92 `next_index = index + 1`
  默认下一帧就是当前帧往后一个。  
  整体作用：先按正常顺序往下走。

- L94 `if next_index >= len(frames):`
  如果下一帧下标已经超过最后一张图，就表示动画播到头了。  
  整体作用：决定是循环、停止，还是触发回调。

- L96 `if loop:`
  检查这段动画是不是循环播放模式。  
  整体作用：背景动画通常就是 `True`

- L98 `next_index = 0`
  播到头时把下标重置成第 0 帧。  
  整体作用：从头开始循环。

- L100 `else:`
  如果不是循环，就走这个分支。

- L102 `video_after_id = None`
  先把定时器编号清掉。  
  整体作用：表示这一段非循环动画结束了，不再继续安排下一帧。

- L104 `if on_complete is not None:`
  检查外面有没有传进来“播完后要执行的函数”。  
  整体作用：比如吃饭动作播完后，要自动回背景。

- L106 `on_complete()`
  调用回调函数。  
  整体作用：执行“播完以后做什么”。

- L108 `return`
  直接结束 `show_frame`。  
  整体作用：不再继续安排下一帧。

- L111 `video_after_id = root.after(delay, lambda: show_frame(next_index))`
  `root.after(delay, ...)` 表示过 `delay` 毫秒后执行某个函数；`lambda: show_frame(next_index)` 是一个临时小函数，等时间到了再去调用 `show_frame`。  
  整体作用：把“下一帧什么时候播放”交给 tkinter 事件循环。

- L114 `show_frame(0)`
  从第 0 帧开始真正启动播放。  
  整体作用：一调用 `play_video`，动画就会立刻开始。

### 116-141：背景函数和按钮动作函数

- L117 `def start_background_video():`
  定义专门启动背景循环的函数。  
  整体作用：方便在程序启动时和动作播完时重复调用。

- L119 `play_video(idle_frames, idle_fps, loop=True)`
  播放背景帧列表，并设置成循环。  
  整体作用：让背景一直动。

- L122 `def eat():`
  定义 Eat 按钮对应的函数。

- L124 `print("Eat button clicked")`
  `print(...)` 是调试输出。  
  整体作用：让你在终端知道点击事件已经触发。

- L126 `play_video(eat_frames, eat_fps, loop=False, on_complete=start_background_video)`
  播放吃饭动画；`loop=False` 表示只播一遍；`on_complete=start_background_video` 表示播完自动回背景。  
  整体作用：实现“点 Eat -> 播一次吃饭 -> 自动回待机”。

- L129 `def hit():`
  定义 Hit 按钮对应的函数。

- L131 `print("Hit button clicked")`
  调试输出。

- L133 `play_video(hit_frames, hit_fps, loop=False, on_complete=start_background_video)`
  播放 hit 动画一次，播完回背景。  
  整体作用：实现“点 Hit -> 播一次 -> 回待机”。

- L136 `def caress():`
  定义 Caress 按钮对应的函数。

- L138 `print("Caress button clicked")`
  调试输出。

- L140 `play_video(caress_frames, caress_fps, loop=False, on_complete=start_background_video)`
  播放 caress 动画一次，播完回背景。  
  整体作用：实现“点 Caress -> 播一次 -> 回待机”。

### 142-247：画胶囊按钮和按钮交互

- L146 `def draw_button(canvas, x1, y1, x2, y2, color, hover_color, text, text_color, command):`
  定义一个通用按钮函数；参数很多，因为它把位置、颜色、文字、点击动作都参数化了。  
  整体作用：以后只要调用这个函数，就能快速画出一个同风格按钮。

- L148 `tag = f"button_{text.lower()}" ...`
  这里用了 `f"..."` 格式化字符串；`text.lower()` 把文字变成小写；前面的 `button_` 是统一前缀。  
  整体作用：给按钮生成一个统一标签，比如 `Eat` 会变成 `button_eat`，后面绑定事件时要用它把“文字 + 边框 + 填充”当成一个整体。

- L150 `shadow_offset = 3`
  设置阴影偏移量。  
  整体作用：让阴影层相对按钮本体稍微往右下移动。对应后面x1 + shadow_offset等等

- L152 `border_width = 2`
  设置边框厚度。

- L154 `border_color = "#355126"`
  设置按钮边框颜色；引号里的内容是十六进制颜色值。

- L156 `shadow_color = "#23311C"`
  设置阴影颜色

- L160 `def build_button(left, top, right, bottom, fill_color, layer_tag):`
  在 `draw_button` 里面再定义一个内部函数，用它专门画“按钮的一层”。  
  整体作用：因为阴影层、边框层、填充层画法一样，只是颜色和坐标不同，所以抽成一个可复用的小函数

- L162 `r = (bottom - top) / 2 ...`
  `bottom - top` 是按钮高度；再除以 `2` 就是半径。  
  整体作用：让左右两个圆头刚好等于按钮高度的一半，从而拼成胶囊形。

- L164 `return [`
  这里开始返回一个列表。

- L166 `canvas.create_rectangle(...)`
  画中间那一段矩形。  
  整体作用：提供按钮主体中间的长条部分。

- L168 `canvas.create_oval(...)`
  画左边圆头。  
  整体作用：让按钮左侧变圆。

- L170 `canvas.create_oval(...)`
  画右边圆头。  
  整体作用：让按钮右侧也变圆。

- L172 `]`
  结束返回的列表。

- L176 `build_button(`
  开始调用 `build_button` 来画阴影层。

- L178 `x1 + shadow_offset,`
  阴影左边比按钮本体右移一点。

- L180 `y1 + shadow_offset,`
  阴影上边比按钮本体下移一点。

- L182 `x2 + shadow_offset,`
  阴影右边界也同步右移。

- L184 `y2 + shadow_offset,`
  阴影下边界也同步下移。

- L186 `shadow_color, f"{tag}_shadow")`
  用阴影颜色，标签名则在原按钮标签后再加 `_shadow`。  
  整体作用：把阴影层单独标出来，不和主按钮混在一起。

- L190 `border_ids = build_button(x1, y1, x2, y2, border_color, tag)`
  用原始坐标和边框颜色再画一层。  
  整体作用：这是按钮真正的边框层，并把图形 ID 保存起来，后面悬停时要改颜色。

- L191 注释行：说明 L190 的作用。

- L192 空行
  视觉分隔。

- L193 `part_ids = build_button(`
  开始画按钮内部填充层。

- L194 注释行：说明 L193 是填充层。

- L195 `x1 + border_width,`
  左边向内缩一点，露出边框。

- L196 注释行：说明 L195 的意义。

- L197 `y1 + border_width,`
  上边向内缩一点。

- L198 注释行：说明 L197 的意义。

- L199 `x2 - border_width,`
  右边向内缩一点。

- L200 注释行：说明 L199 的意义。

- L201 `y2 - border_width,`
  下边向内缩一点。

- L202 注释行：说明 L201 的意义。

- L203 `color, tag)`
  用按钮默认填充颜色，并沿用主按钮标签。  
  整体作用：这一层是你真正看到的按钮颜色。

- L204 注释行：说明 L203 的作用。

- L205 空行
  分隔填充层和文字层。

- L206 `canvas.create_text(`
  开始在按钮中央画文字。

- L207 注释行：说明 L206 的作用。

- L208 `(x1 + x2) / 2,`
  左右中点，保证文字水平居中。

- L209 注释行：说明 L208 的意义。

- L210 `(y1 + y2) / 2,`
  上下中点，保证文字垂直居中。

- L211 注释行：说明 L210 的意义。

- L212 `text=text,`
  把传进来的按钮文字内容放进去。

- L213 注释行：说明 L212 的作用。

- L214 `fill=text_color,`
  设置文字颜色。

- L215 注释行：说明 L214 的作用。

- L216 `font=("Arial", 14, "bold"), tags=tag)`
  `font=(...)` 是字体设置元组；`tags=tag` 让文字也加入按钮同一组标签。  
  整体作用：这样鼠标移到文字上，也会算作移到按钮上。

- L217 注释行：说明 L216 的作用。

- L218 空行
  分隔文字绘制和鼠标交互函数。

- L219 `#鼠标移动交互`
  注释行。

- L220 `def on_enter(event):`
  定义鼠标移入按钮时执行的函数；`event` 是 tkinter 自动传进来的事件对象。  
  整体作用：实现悬停高亮。

- L221 注释行：说明 L220 的作用。

- L222 `for part_id in part_ids:`
  遍历填充层的所有图形。

- L223 注释行：说明 L222 的作用。

- L224 `canvas.itemconfig(part_id, fill=hover_color, outline=hover_color)`
  把填充层改成悬停颜色。  
  整体作用：鼠标移上去时按钮内部会变色。

- L225 注释行：说明 L224 的作用。

- L226 `for border_id in border_ids:`
  再遍历边框层。

- L227 注释行：说明 L226 的作用。

- L228 `canvas.itemconfig(border_id, fill="#446735", outline="#446735")`
  把边框也稍微提亮。  
  整体作用：让悬停状态更明显。

- L229 注释行：说明 L228 的作用。

- L230 空行
  分隔 `on_enter` 和 `on_leave`。

- L231 `def on_leave(event):`
  定义鼠标离开按钮时执行的函数。  
  整体作用：把颜色恢复回默认值。

- L232 注释行：说明 L231 的作用。

- L233 `for part_id in part_ids:`
  再遍历填充层。

- L234 注释行：说明 L233 的作用。

- L235 `canvas.itemconfig(part_id, fill=color, outline=color)`
  恢复填充层默认颜色。

- L236 注释行：说明 L235 的作用。

- L237 `for border_id in border_ids:`
  再遍历边框层。

- L238 注释行：说明 L237 的作用。

- L239 `canvas.itemconfig(border_id, fill=border_color, outline=border_color)`
  恢复边框默认颜色。

- L240 注释行：说明 L239 的作用。

- L241 空行
  分隔交互函数定义和事件绑定。

- L242 `canvas.tag_bind(tag, "<Enter>", on_enter)`
  `tag_bind` 表示把事件绑定到一个标签组；`"<Enter>"` 表示鼠标移入事件。  
  整体作用：只要鼠标进入这个按钮任意组成部分，就执行 `on_enter`。

- L243 注释行：说明 L242 的作用。

- L244 `canvas.tag_bind(tag, "<Leave>", on_leave)`
  把鼠标移出事件绑定到按钮标签。

- L245 注释行：说明 L244 的作用。

- L246 `canvas.tag_bind(tag, "<Button-1>", lambda event: command())`
  `"<Button-1>"` 表示鼠标左键点击；`lambda event: command()` 表示收到点击事件后，去执行外面传进来的按钮函数。  
  整体作用：让不同按钮能复用同一套绘制代码，但点击时执行各自不同的函数。

- L247 注释行：说明 L246 的作用。

### 248-262：创建按钮并启动程序

- L248 空行
  分隔“按钮函数定义”和“真正创建按钮”。

- L249 `#直接输入创建`
  注释行，意思是下面开始直接调用函数生成按钮。

- L250 `draw_button(canvas, 797, 387, 915, 426,"#7AA95C", "#678F4D", "Eat", "#F5F7EE", eat)`
  这是创建第一个按钮：位置从 `(797, 387)` 到 `(915, 426)`；默认色是 `#7AA95C`；悬停色是 `#678F4D`；文字是 `Eat`；文字颜色是 `#F5F7EE`；点击执行 `eat` 函数。  
  整体作用：把 Eat 按钮画到画布上。

- L251 注释行：说明 L250 的作用。

- L252 `draw_button(canvas, 924, 387, 1043, 426, "#5F8E4C", "#4F7840", "Hit", "#F5F7EE", hit)`
  和上面同理，只是位置、颜色和点击动作换成了 Hit。  
  整体作用：创建 Hit 按钮。

- L253 注释行：说明 L252 的作用。

- L254 `draw_button(canvas, 1052, 387, 1170, 426, "#9BC782", "#84AD6D", "Caress", "#F5F7EE", caress)`
  同理，创建 Caress 按钮。

- L255 注释行：说明 L254 的作用。

- L256-L258 空行
  这几行空行只是让文件结尾看起来没那么挤。

- L259 `start_background_video()`
  程序一启动就先调用背景循环函数。  
  整体作用：窗口一打开就开始播放待机动画。

- L260 注释行：说明 L259 的作用。

- L261 `root.mainloop()`
  `mainloop()` 是 tkinter 的事件循环。  
  整体作用：让窗口持续运行，等待点击、刷新画面、处理 after 定时器。如果没有这一行，窗口会一闪而过。

- L262 注释行：说明 L261 的作用。

---

## 运行流程总结

如果把整个程序只讲成 8 步，可以记成这样：

1. 导入 tkinter、Pillow、Path。
2. 创建主窗口和画布。
3. 定义 4 个帧文件夹路径。
4. 用 `load_video_frames()` 把四组帧图读进内存。
5. 在画布上创建一个背景图片对象 `bg_item`。
6. 用 `play_video()` 控制背景图不断换帧。
7. 用 `draw_button()` 画出 3 个胶囊按钮。
8. 点击按钮时播放对应动画，播完自动回背景。

---

## 最值得你现在记住的 10 个知识点

1. `root = tk.Tk()` 是整个窗口的起点。
2. `canvas` 是你这份作业里所有视觉内容的主要舞台。
3. `Path / "文件夹名"` 是路径拼接，不是除法。
4. `sorted(...glob("*.png"))` 用来按顺序拿到所有帧图。
5. `frames = []` 是列表，专门用来存很多帧。
6. `ImageTk.PhotoImage(...)` 是 tkinter 能显示图片的关键。
7. `root.after(...)` 是动画能动起来的核心。
8. `loop=True` 用来做背景循环。
9. `on_complete=start_background_video` 用来做“动作播完回待机”。
10. `tag_bind(...)` 让你手画出来的图形也能像按钮一样响应鼠标。

