# Beta V1 工程超级详细学习笔记

说明：这份笔记默认“这个工程”指当前目录 `FINALPROJECT/Beta V1` 里的这一套内容，也就是以 [betaV1.py](/Users/rophasia/Documents/GitHub/lmsc261/FINALPROJECT/Beta%20V1/betaV1.py:1) 为核心的 Tkinter 小项目。

目标：把这个工程从“目录结构”到“每一段逻辑”，再到“每个关键单词和标点符号的作用”，尽量拆到初学者能跟读、能模仿、能自己改。

2026-04-28 当前版本同步说明：

- 这份笔记已经同步到“待机背景视频 + `Eat` 一次性动作视频”的版本。
- 当前代码会循环播放 `background.mp4` 作为待机动画。
- 点击 `Eat` 按钮后，会播放一次 `eat.mp4`。
- `eat.mp4` 播完以后，会自动回到 `background.mp4` 的待机循环。
- 如果你在下面看到旧概念和这里冲突，以这里和当前 [betaV1.py](/Users/rophasia/Documents/GitHub/lmsc261/FINALPROJECT/Beta%20V1/betaV1.py:1) 为准。

---

## 1. 这个工程里有什么

当前目录大致包含这些内容：

- `betaV1.py`
  这是主程序。运行它，窗口就会打开，背景会循环播放视频，按钮会显示出来。
- `background.mp4`
  这是待机背景视频资源。程序会把它当作 idle 动画循环播放。
- `eat.mp4`
  这是吃饭动作视频资源。点击 `Eat` 按钮后，会完整播放一遍，然后回到待机背景视频。
- `background.png`
  这是静态背景兜底图。如果视频读不了，程序至少还能显示这张图，不至于一打开就报错崩掉。
- `.vendor/`
  这是“项目本地依赖目录”。里面放了 `imageio`、`imageio-ffmpeg`、`numpy`、`Pillow` 等库。
  这样做的好处是：就算系统 Python 没装这些库，这个项目也能自己从 `.vendor` 里找依赖。
- `__pycache__/`
  这是 Python 自动生成的字节码缓存目录。不是你手写的业务逻辑文件。

这说明这个工程不是一个纯静态脚本，而是一个“代码 + 资源 + 本地依赖”的完整小项目。

---

## 2. 这个工程整体在做什么

这个工程做的事，可以分成 11 步：

1. 导入需要的模块。
2. 计算当前脚本所在目录，并拼出待机视频、吃饭视频、图片、依赖目录的路径。
3. 如果本地依赖目录存在，就把它插入 Python 的模块搜索路径。
4. 创建 Tkinter 主窗口。
5. 先加载一张静态背景图，保证界面有初始画面。
6. 把视频片段按路径缓存起来，避免同一个视频每次触发都重新解码。
7. 尝试读取 `background.mp4`，把它逐帧解码成一组待机动画帧。
8. 通过 `root.after(...)` 周期性切换这些帧，让背景看起来像在播放视频。
9. 画出四个圆角按钮，并绑定鼠标悬停和点击事件。
10. 当用户点击 `Eat` 时，切换到 `eat.mp4` 单次播放，结束后自动回归待机动画。
11. 进入 Tkinter 的事件循环，持续等待用户操作和定时刷新。

更口语一点地说：

- `betaV1.py` 先搭出一个窗口。
- 再把一张图先垫底。
- 然后如果视频能加载成功，就不停把背景换成待机视频的下一帧。
- 当你点 `Eat` 时，程序会临时切到吃饭动画，播完再回到待机。
- 同时保留四个按钮，让你可以点击交互。

---

## 3. 运行顺序总览

如果你直接运行 [betaV1.py](/Users/rophasia/Documents/GitHub/lmsc261/FINALPROJECT/Beta%20V1/betaV1.py:1)，执行顺序大致是：

1. 先执行所有顶层导入语句。
2. 再执行所有常量和全局变量赋值。
3. 创建 Tkinter 主窗口 `root`。
4. 创建 `canvas` 并把初始背景图放上去。
5. 定义很多函数，但定义函数时并不会立刻执行函数体。
6. 在文件最底部调用 `draw_round_button(...)` 四次，把四个按钮画出来。
7. 调用 `root.protocol(...)` 注册关闭窗口时要执行的清理动作。
8. 调用 `start_background_video()`，开始准备和播放待机背景视频。
9. 调用 `root.mainloop()`，正式进入图形界面的循环。
10. 当用户后面点击 `Eat` 时，再触发 `play_video(EAT_VIDEO_PATH, loop=False, on_complete=start_background_video)`。

理解这一点很重要：

- “定义函数”不等于“执行函数”。
- 真正开始播放待机视频，是在最下面执行了 `start_background_video()` 之后。
- 真正让窗口持续响应事件，是在执行了 `root.mainloop()` 之后。
- 真正切到吃饭动画，是在点击 `Eat` 按钮之后。

---

## 4. 学这个工程前，先认识常见语法符号

下面这些符号在这个工程里反复出现：

- `=`：赋值。把右边的值放进左边变量。
- `.`：访问对象的属性或方法。
- `()`：函数调用、方法调用，或者把表达式包起来。
- `[]`：列表，或者列表索引。
- `{}`：这里主要出现在 f-string 里，表示要把表达式结果塞进字符串。
- `:`：用于 `if`、`def`、`try`、`except`、`for` 等语句的开头，表示下一行开始进入一个缩进代码块。
- `,`：分隔参数、元素或多个导入项。
- `"`：字符串边界。
- `f"..."`：格式化字符串，字符串里可以直接写表达式。
- `%`：取模。常用来“循环回到开头”。
- `*`：乘法。
- `/`：这里既有普通除法，也有 `Path` 对象重载出来的“路径拼接”。
- `-`：减法，或者负号。
- `+`：加法。
- `#`：注释起始符号。

再提醒一个经常混淆的点：

- `VENDOR_DIR = BASE_DIR / ".vendor"` 这一行里的 `/` 不是普通数学除法。
- 因为 `BASE_DIR` 是 `Path` 对象，所以这里的 `/` 被 `pathlib` 特殊处理成了“路径拼接”。

---

## 5. 逐行、逐词、逐逻辑说明

下面开始按当前代码版本逐行解释。

空行的统一说明：

- 空行本身没有业务逻辑。
- 它的作用是把“导入区”“配置区”“窗口区”“函数区”“调用区”隔开。
- 对初学者来说，空行很重要，因为它让代码阅读更有层次。

---

### 第 1 行

代码：`from pathlib import Path`

单词说明：

- `from`：表示“从某个模块里取内容”。
- `pathlib`：Python 标准库里的路径处理模块。
- `import`：导入关键字。
- `Path`：`pathlib` 中的一个类，用来更安全、更清晰地表示文件路径。

标点和空格说明：

- 这一行没有逗号、括号这类符号型标点。
- 主要靠空格把 `from`、`pathlib`、`import`、`Path` 分开。

逻辑说明：

- 导入 `Path` 后，后面就能写 `BASE_DIR / "background.mp4"` 这种很自然的路径拼接写法。
- 这比手工拼字符串路径更稳，也更不容易出错。

---

### 第 2 行

代码：`import sys`

单词说明：

- `import`：导入关键字。
- `sys`：Python 的系统模块，可以访问解释器运行环境的一些信息。

标点说明：

- 没有额外标点，只有空格。

逻辑说明：

- 这里导入 `sys`，是为了后面改 `sys.path`。
- `sys.path` 是 Python 搜索模块的目录列表。
- 你把 `.vendor` 插进去之后，Python 才能从项目本地目录里找到 `imageio` 这些库。

---

### 第 3 行

代码：`import time`

单词说明：

- `import`：导入关键字。
- `time`：时间模块。

逻辑说明：

- 这个工程用 `time.perf_counter()` 计算“从开始播放到现在过去了多久”。
- 有了这个时间差，程序才能知道此刻应该显示第几帧视频。

---

### 第 5 行

代码：`BASE_DIR = Path(__file__).resolve().parent`

单词说明：

- `BASE_DIR`：基础目录，通常用全大写表示“配置值”或“常量”。
- `Path`：把路径包装成 `Path` 对象。
- `__file__`：Python 里表示“当前脚本文件路径”的特殊变量。
- `resolve()`：把路径解析成完整的绝对路径。
- `parent`：取当前路径的父目录，也就是脚本所在文件夹。

标点说明：

- `=`：把右侧结果赋值给 `BASE_DIR`。
- `(` `)`：调用 `Path(...)`。
- `.`：访问对象的方法或属性。
- `__file__` 两侧的双下划线是 Python 特殊名字的命名形式。

逻辑说明：

- 这行代码的最终结果不是文件本身，而是 `betaV1.py` 所在的目录。
- 后面读视频、读图片、找 `.vendor`，都从这个目录出发。
- 这样不管你从哪个终端目录启动脚本，路径都更稳定。

---

### 第 6 行

代码：`VENDOR_DIR = BASE_DIR / ".vendor"`

单词说明：

- `VENDOR_DIR`：本地依赖目录。
- `BASE_DIR`：上面算出来的项目目录。
- `".vendor"`：目录名字符串。

标点说明：

- `=`：赋值。
- `/`：这里不是普通除法，而是 `Path` 的路径拼接操作。
- `"`：字符串边界。

逻辑说明：

- 最终得到的是 `FINALPROJECT/Beta V1/.vendor` 这个目录。
- 这个目录里放的是项目自己携带的第三方依赖。

---

### 第 7 行

代码：`WINDOW_WIDTH = 800`

单词说明：

- `WINDOW_WIDTH`：窗口宽度。
- `800`：整数，表示宽 800 像素。

标点说明：

- `=`：赋值。

逻辑说明：

- 后面窗口大小、背景大小、画布大小都会引用它。
- 这样如果以后你想改宽度，只需要改一处。

---

### 第 8 行

代码：`WINDOW_HEIGHT = 300`

单词说明：

- `WINDOW_HEIGHT`：窗口高度。
- `300`：整数，表示高 300 像素。

逻辑说明：

- 和上一行一样，是统一管理尺寸的常量。

---

### 第 9 行

代码：`IDLE_VIDEO_PATH = BASE_DIR / "background.mp4"`

单词说明：

- `IDLE_VIDEO_PATH`：待机视频文件路径。
- `BASE_DIR`：工程目录。
- `"background.mp4"`：待机视频文件名。

标点说明：

- `=`：赋值。
- `/`：路径拼接。
- `"`：字符串。

逻辑说明：

- 程序会把这个视频当作 idle 背景动画循环播放。

---

### 第 10 行

代码：`EAT_VIDEO_PATH = BASE_DIR / "eat.mp4"`

单词说明：

- `EAT_VIDEO_PATH`：吃饭动作视频文件路径。
- `"eat.mp4"`：吃饭视频文件名。

逻辑说明：

- 点击 `Eat` 按钮后，程序会切到这个视频，并只播放一遍。

---

### 第 11 行

代码：`IMAGE_PATH = BASE_DIR / "background.png"`

单词说明：

- `IMAGE_PATH`：静态背景图路径。
- `"background.png"`：图片文件名。

逻辑说明：

- 这是一个兜底资源。
- 如果视频不可用，程序至少还能显示一张图。

---

### 第 12 行

代码：`if VENDOR_DIR.exists():`

单词说明：

- `if`：条件判断关键字。
- `VENDOR_DIR`：本地依赖目录。
- `exists()`：检查这个路径是否存在。

标点说明：

- `.`：调用 `Path` 对象的方法。
- `(` `)`：方法调用。
- `:`：表示下面会跟一个缩进代码块，只有条件成立才执行。

逻辑说明：

- 如果 `.vendor` 目录真的存在，才去把它加入模块搜索路径。
- 如果不存在，就跳过，不会报错。

---

### 第 13 行

代码：`sys.path.insert(0, str(VENDOR_DIR))`

单词说明：

- `sys`：系统模块。
- `path`：Python 的模块搜索路径列表。
- `insert`：在指定位置插入元素。
- `0`：列表最前面的位置。
- `str`：把 `Path` 对象转成字符串。
- `VENDOR_DIR`：本地依赖目录。

标点说明：

- `.`：先访问 `sys.path`，再调用 `insert(...)`。
- `(` `)`：函数调用。
- `,`：分隔参数。

逻辑说明：

- 这行的意思是：把 `.vendor` 放到模块搜索路径最前面。
- 放在最前面意味着 Python 会优先从这里找模块。
- 这样就算系统环境里没有装 `imageio`，这个项目也能从自己的 `.vendor` 里导入。

---

### 第 15 行

代码：`from PIL import Image, ImageTk`

单词说明：

- `PIL`：Pillow 图像库的包名来源。
- `Image`：处理图片的核心对象。
- `ImageTk`：把 Pillow 图片转换成 Tkinter 能显示的图像对象。

标点说明：

- `,`：分隔两个导入项。

逻辑说明：

- `Image` 用来打开图片、缩放图片、把视频帧转成图片。
- `ImageTk` 用来把这些图片真正显示在 Tkinter 画布上。

---

### 第 16 行

代码：`import tkinter as tk`

单词说明：

- `tkinter`：Python 自带的图形界面库。
- `as`：起别名。
- `tk`：`tkinter` 的简写。

逻辑说明：

- 后面写 `tk.Tk()`、`tk.Canvas(...)` 会更短、更清楚。

---

### 第 18 行

代码：`try:`

单词说明：

- `try`：表示“尝试执行下面的代码”。

标点说明：

- `:`：说明下面会有一个缩进代码块。

逻辑说明：

- 这是异常处理结构的开始。
- 如果导入 `imageio` 失败，不想让整个程序直接崩掉，就可以用 `try/except` 包起来。

---

### 第 19 行

代码：`import imageio.v2 as imageio`

单词说明：

- `imageio.v2`：`imageio` 库里的 v2 接口。
- `as imageio`：导入后仍然叫 `imageio`，方便后面使用。

标点说明：

- `.`：访问子模块 `v2`。

逻辑说明：

- 程序需要 `imageio` 去读取 `mp4` 视频帧。

---

### 第 20 行

代码：`except ImportError:`

单词说明：

- `except`：捕获异常。
- `ImportError`：导入失败时常见的异常类型。

标点说明：

- `:`：下面是异常发生时执行的代码块。

逻辑说明：

- 如果 `imageio` 没装好，或者导入失败，就走下一行。

---

### 第 21 行

代码：`imageio = None`

单词说明：

- `imageio`：变量名。
- `None`：空值，表示“当前没有可用对象”。

逻辑说明：

- 这是一种很常见的“失败兜底”写法。
- 后面只要判断 `imageio is None`，就知道视频功能当前不可用。

---

### 第 23 行

代码：`root = tk.Tk()`

单词说明：

- `root`：主窗口变量名。
- `tk`：`tkinter` 的别名。
- `Tk`：创建主窗口的类或入口。

标点说明：

- `=`：赋值。
- `.`：访问 `Tk`。
- `(` `)`：调用。

逻辑说明：

- 这一行真正创建了整个 GUI 应用的主窗口。

---

### 第 24 行

代码：`root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")`

单词说明：

- `geometry`：设置窗口几何尺寸的方法。
- `f"..."`：格式化字符串。
- `WINDOW_WIDTH`：窗口宽。
- `x`：这里不是乘法，而是 Tkinter 几何字符串里的字面字符。
- `WINDOW_HEIGHT`：窗口高。

标点说明：

- `.`：调用窗口方法。
- `(` `)`：调用。
- `{}`：在 f-string 里插入变量值。
- `"`：字符串边界。

逻辑说明：

- 这行运行后，实际传给 Tkinter 的是 `"800x300"` 这样的字符串。

---

### 第 25 行

代码：`root.title("Beta V1")`

单词说明：

- `title`：设置窗口标题。
- `"Beta V1"`：标题文字。

逻辑说明：

- 这会显示在窗口标题栏上。

---

### 第 26 行

代码：`root.resizable(False, False)`

单词说明：

- `resizable`：设置窗口能不能被拖动改变大小。
- `False`：布尔假值。

标点说明：

- `,`：分隔横向和纵向两个参数。

逻辑说明：

- 两个 `False` 分别表示横向不能拉伸、纵向也不能拉伸。
- 这样能避免背景和按钮布局被拉坏。

---

### 第 28 行到第 31 行

代码：

```python
background_image = Image.open(IMAGE_PATH).resize(
    (WINDOW_WIDTH, WINDOW_HEIGHT),
    Image.Resampling.BILINEAR,
)
```

这四行是一个完整表达式，只是换行写开了。

第 28 行单词说明：

- `background_image`：背景图片变量。
- `Image.open(...)`：打开图片文件。
- `IMAGE_PATH`：要打开的图片路径。
- `resize(...)`：缩放图片。

第 29 行说明：

- `(WINDOW_WIDTH, WINDOW_HEIGHT)`：一个二元元组，表示目标尺寸。
- 小括号包住两个值，逗号把两个值分开。

第 30 行说明：

- `Image.Resampling.BILINEAR`：指定缩放时用双线性采样。
- `Resampling` 是 Pillow 里管理重采样算法的枚举容器。
- `BILINEAR` 表示一种缩放插值算法，比最简单的最近邻平滑一些。

第 31 行说明：

- `)`：关闭 `resize(...)` 这次函数调用。

整体逻辑说明：

- 先打开 `background.png`。
- 再把它缩成和窗口一样的尺寸。
- 这个图片是最开始显示的背景，也是视频不可用时的保底背景。

---

### 第 32 行

代码：`current_background = ImageTk.PhotoImage(background_image)`

单词说明：

- `current_background`：当前正在显示的背景图对象。
- `ImageTk.PhotoImage(...)`：把 Pillow 图片转换成 Tkinter 可显示的图像对象。

逻辑说明：

- Tkinter 画布不能直接吃 Pillow 的 `Image` 对象。
- 必须先转成 `PhotoImage`。

---

### 第 33 行

代码：`video_cache = {}`

单词说明：

- `video_cache`：视频缓存字典。
- `{}`：空字典。

逻辑说明：

- 这个字典会记住已经解码好的视频片段。
- 比如 `background.mp4` 和 `eat.mp4` 第一次加载后，后面再次播放就不必重新逐帧解码。

---

### 第 34 行

代码：`video_frames = []`

单词说明：

- `video_frames`：视频帧列表。
- `[]`：空列表。

逻辑说明：

- 后面加载视频时，每一帧都会变成一张 `PhotoImage`，然后放进这个列表。

---

### 第 35 行

代码：`video_after_id = None`

单词说明：

- `video_after_id`：保存 `root.after(...)` 返回的定时任务编号。
- `None`：一开始还没有定时任务，所以先设为空。

逻辑说明：

- 后面如果要停止视频播放，需要拿这个编号去取消定时器。

---

### 第 36 行

代码：`video_fps = 24.0`

单词说明：

- `video_fps`：视频播放帧率。
- `24.0`：浮点数默认值。

逻辑说明：

- 这是一个初始值。
- 后面真正读到视频元数据和总帧数后，会重新计算更准确的帧率。

---

### 第 37 行

代码：`video_duration = 0.0`

单词说明：

- `video_duration`：当前视频片段总时长。
- `0.0`：初始浮点值。

逻辑说明：

- 当播放一次性动画时，程序需要知道它什么时候结束。

---

### 第 38 行

代码：`video_start_time = 0.0`

单词说明：

- `video_start_time`：视频开始播放时刻。
- `0.0`：初始浮点值。

逻辑说明：

- 以后会把真正的起始时间记录进来。
- 播放某一帧时，会用“当前时间 - 起始时间”算出已经播了多久。

---

### 第 39 行到第 40 行

代码：

```python
video_loop = True
video_on_complete = None
```

说明：

- `video_loop`：当前片段是否循环播放。
- `True` 表示循环，适合待机背景视频。
- `video_on_complete`：当前片段播完以后要执行的回调函数。
- `None` 表示默认没有额外回调。

逻辑说明：

- 这两个变量是“待机动画”和“动作动画”共用同一套播放器的关键。
- 待机动画用 `loop=True`。
- `eat.mp4` 这种动作动画用 `loop=False`，并且播完后执行 `start_background_video`。

---

### 第 43 行到第 56 行

这里定义了 4 个按钮回调函数：

- `eat()`
- `sleep()`
- `hit()`
- `caress()`

它们的结构几乎一样。

以第 39 行和第 40 行为例：

代码：

```python
def eat():
    print("Eat button clicked")
    play_video(EAT_VIDEO_PATH, loop=False, on_complete=start_background_video)
```

单词说明：

- `def`：定义函数。
- `eat`：函数名。
- `print`：向终端输出文字。
- `"Eat button clicked"`：输出内容。
- `play_video(...)`：切换到指定视频片段播放。
- `EAT_VIDEO_PATH`：吃饭动作视频路径。
- `loop=False`：这次不要循环。
- `on_complete=start_background_video`：播完后回到待机背景动画。

标点说明：

- `(` `)`：`eat()` 这里表示函数没有参数；`print(...)` 这里表示函数调用。
- `:`：函数体从下一行缩进开始。
- `"`：字符串。

逻辑说明：

- `Eat` 按钮不再只是打印一句话。
- 它现在会触发 `eat.mp4` 播放一次。
- 由于你已经把 `eat.mp4` 做成了末尾能无缝接回背景，所以这个回调会在吃饭动画结束后自动重新进入待机循环。
- 这里的 `print(...)` 还保留着，方便你在终端观察有没有触发点击。

`sleep()`、`hit()`、`caress()` 的结构完全同理，只是输出文本不同。

---

### 第 55 行到第 60 行

代码：

```python
canvas = tk.Canvas(
    root,
    width=WINDOW_WIDTH,
    height=WINDOW_HEIGHT,
    highlightthickness=0,
)
```

逐项说明：

- `canvas`：画布变量名。
- `tk.Canvas(...)`：创建 Tkinter 画布组件。
- `root`：表示这个画布属于主窗口。
- `width=WINDOW_WIDTH`：画布宽度 800。
- `height=WINDOW_HEIGHT`：画布高度 300。
- `highlightthickness=0`：去掉默认高亮边框厚度。

标点说明：

- `=` 在 `width=...` 这种写法里是关键字参数赋值。
- `,` 分隔各个参数。
- 最后一行单独一个 `)`，表示结束多行函数调用。

逻辑说明：

- 背景图、视频帧、按钮图形、按钮文字，都是画在这个 `canvas` 上的。

---

### 第 61 行

代码：`canvas.pack()`

单词说明：

- `pack`：Tkinter 的一种布局管理方法。

逻辑说明：

- 创建画布对象不等于把它显示出来。
- `pack()` 才是把它放进窗口布局里。

---

### 第 62 行

代码：`bg_item = canvas.create_image(0, 0, anchor="nw", image=current_background)`

单词说明：

- `bg_item`：背景图像对象在画布上的 ID。
- `create_image`：在画布上创建图片项。
- `0, 0`：图片放置坐标。
- `anchor="nw"`：以图片左上角作为锚点。
- `image=current_background`：要显示的图片对象。

标点说明：

- `,`：分隔位置参数和关键字参数。
- `"nw"`：字符串，表示 north-west，也就是左上角。

逻辑说明：

- 先把初始背景图放到画布上。
- 后面播放视频时，不是不断新建新的图片项，而是更新这个已存在项的图像内容。

---

### 第 63 行

代码：`canvas.tag_lower(bg_item)`

单词说明：

- `tag_lower`：把某个画布项放到底层。
- `bg_item`：背景图像项。

逻辑说明：

- 背景必须在最底层。
- 否则后画出来的按钮有可能被背景盖住，或者层级关系混乱。

---

### 第 70 行到第 76 行

代码：

```python
def stop_video_playback():
    global video_after_id
    global video_on_complete

    if video_after_id is not None:
        root.after_cancel(video_after_id)
        video_after_id = None
    video_on_complete = None
```

第 70 行：

- `def stop_video_playback():`
- 定义一个“停止当前视频播放调度”的函数。

第 71 行到第 72 行：

- `global video_after_id`
- `global video_on_complete`
- `global` 表示下面操作的是全局变量，不是新建局部变量。

第 74 行：

- `if video_after_id is not None:`
- `is not None` 表示“它现在确实有值，不是空”。

第 75 行：

- `root.after_cancel(video_after_id)`
- 取消之前注册的 Tkinter 定时任务。

第 76 行到第 77 行：

- `video_after_id = None`
- `video_on_complete = None`
- 这表示当前没有待执行的视频刷新任务，也没有待触发的结束回调。

整体逻辑说明：

- 不管是从待机切到吃饭，还是从吃饭切回待机，都需要先把上一个片段的定时任务停掉。
- 这个函数就是负责做那一步清理。

---

### 第 79 行到第 107 行

这是视频加载核心函数：

```python
def load_video_frames(video_path):
    ...
```

和旧版最大的不同是：

- 旧版只会加载一个固定的背景视频。
- 当前版会根据传进来的 `video_path` 去加载任意片段。
- 所以它既可以加载 `background.mp4`，也可以加载 `eat.mp4`。

它做的事是：

1. 检查传进来的视频路径是否存在。
2. 检查 `imageio` 是否可用。
3. 打开对应视频。
4. 读取元数据。
5. 遍历每一帧。
6. 把每一帧缩放到窗口大小。
7. 把每一帧转换成 Tkinter 可显示的 `PhotoImage`。
8. 存进 `frames` 列表。
9. 重新计算这个片段更准确的实际帧率。
10. 返回一个字典，而不是只返回帧列表。

这个返回字典的结构是：

```python
{
    "frames": [...],
    "fps": ...,
    "duration": ...,
}
```

这样做的意义是：

- `frames` 负责真正显示画面。
- `fps` 负责决定播放节奏。
- `duration` 负责判断一次性动画什么时候结束。

特别注意：

- 旧版笔记里说它“返回整组帧列表”，那是以前的实现。
- 当前版本里，它返回的是“一个包含帧、帧率、时长的片段对象字典”。

---

### 第 110 行到第 114 行

代码：

```python
def get_video_clip(video_path):
    clip = video_cache.get(video_path)
    if clip is None:
        clip = load_video_frames(video_path)
        video_cache[video_path] = clip
    return clip
```

说明：

- `get_video_clip(...)` 是缓存入口。
- 它会先去 `video_cache` 里看这个视频之前有没有加载过。
- 如果已经加载过，就直接拿缓存。
- 如果还没加载，就调用 `load_video_frames(video_path)` 去解码，并把结果记进缓存。

逻辑意义：

- 第一次点击 `Eat` 时，程序可能需要先准备 `eat.mp4` 的帧。
- 第二次再点时，就可以更快，因为它已经在缓存里了。

---

### 第 117 行到第 149 行

这是当前版本真正的“通用播放器”核心：

```python
def show_video_frame():
    ...
```

这版和旧版相比，多了两个关键能力：

1. 支持循环播放。
2. 支持只播一次，然后触发结束回调。

关键变量：

- `video_loop`
  表示当前片段是否循环。
- `video_on_complete`
  表示当前片段播放结束后要执行什么函数。
- `video_duration`
  表示当前片段总时长。

核心流程：

1. 先确认 `video_frames` 不是空的。
2. 计算当前已经过了多少时间。
3. 用 `elapsed * video_fps` 算出理论帧位置。
4. 如果是循环片段，就用 `% len(video_frames)` 回绕。
5. 如果是单次片段，就用 `min(...)` 把帧索引卡在最后一帧。
6. 把 `bg_item` 的图像换成当前帧。
7. 如果这是单次片段，并且已经播到时长末尾，就执行 `video_on_complete`。
8. 如果还没播完，就继续用 `root.after(...)` 安排下一次刷新。

最重要的逻辑分叉：

- 待机背景视频：
  `loop=True`
  所以会一直循环。
- `eat.mp4`：
  `loop=False`
  所以播到结尾就停。
- 播完以后又因为设置了 `on_complete=start_background_video`，所以它停下的同时会重新进入待机。

这就是“点一下吃饭，播一遍动作，再回到背景待机”的核心原理。

---

### 第 152 行到第 171 行

代码：

```python
def play_video(video_path, loop=True, on_complete=None):
    ...
```

说明：

- `play_video(...)` 是现在的统一播放入口。
- 你以后无论想播待机、吃饭、睡觉还是别的动作，原则上都应该走这个函数。

它的职责是：

1. 先调用 `stop_video_playback()` 停掉上一段片段。
2. 用 `get_video_clip(video_path)` 拿到目标视频的缓存数据。
3. 把当前全局播放器状态切换到这个新片段。
4. 写入 `video_fps`、`video_duration`、`video_start_time`、`video_loop`、`video_on_complete`。
5. 调用 `show_video_frame()` 正式开始刷新。

逻辑意义：

- 旧版只有“启动背景视频”这一个入口。
- 当前版已经变成“任意视频片段都能播放”的结构了。

---

### 第 174 行到第 175 行

代码：

```python
def start_background_video():
    play_video(IDLE_VIDEO_PATH, loop=True)
```

说明：

- `start_background_video()` 现在变成了一个很薄的包装函数。
- 它不再自己负责加载帧和启动计时。
- 它只是明确表示：“请播放待机视频，而且要循环。”

这样写的好处是：

- 名字仍然很直观。
- 但底层逻辑复用了更通用的 `play_video(...)`。

---

### 第 178 行到第 180 行

代码：

```python
def on_close():
    stop_video_playback()
    root.destroy()
```

说明：

- 这是窗口关闭时要执行的函数。
- 和旧版相比，关闭时不再调用旧名字 `stop_background_video()`，而是调用更通用的 `stop_video_playback()`。
- 因为当前程序关闭时，未必正在播的是待机背景，也可能正播到 `eat.mp4`。

逻辑说明：

- 先清理当前视频调度，再销毁窗口，是比较稳的收尾顺序。

---

### 第 147 行到第 208 行

这是整个工程里最复杂的图形绘制函数：

```python
def draw_round_button(...):
    ...
```

它的目标不是调用 Tkinter 默认按钮，而是自己用矩形、圆形、文字拼出一个圆角按钮。

这段逻辑的核心思想是：

1. 先画阴影层。
2. 再画边框层。
3. 再画内部填充层。
4. 再把文字放上去。
5. 再绑定鼠标进入、离开、点击事件。

这样你就得到一个有立体感、可悬停变色、可点击的自定义按钮。

#### 第 147 行

代码：`def draw_round_button(canvas, x1, y1, x2, y2, radius, color, hover_color, text, text_color, command):`

参数说明：

- `canvas`：画到哪个画布上。
- `x1, y1`：左上角坐标。
- `x2, y2`：右下角坐标。
- `radius`：圆角半径。
- `color`：按钮默认填充色。
- `hover_color`：鼠标悬停时填充色。
- `text`：按钮文字。
- `text_color`：文字颜色。
- `command`：点击按钮时执行的函数。

标点说明：

- 参数之间用 `,` 分隔。
- 行尾 `:` 表示函数体开始。

#### 第 148 行

代码：`# 用同一个标签把按钮的图形和文字绑在一起，后面就能一起改颜色和响应点击。`

说明：

- 这是注释。
- `#` 后面的内容不会被 Python 执行。
- 它是在给读代码的人解释设计思路。

#### 第 149 行

代码：`tag = f"button_{text.lower()}"`

说明：

- `tag`：按钮的统一标签。
- `text.lower()`：把按钮文字转成小写。
- 如果 `text` 是 `"Eat"`，这里会得到 `"eat"`。
- 最终 `tag` 类似 `"button_eat"`。

逻辑作用：

- 这个标签会同时绑定到按钮的图形和文字上。
- 这样只用一个标签就能给整组对象加事件。

#### 第 150 行到第 153 行

代码：

```python
shadow_offset = 3
border_width = 2
border_color = "#355126"
shadow_color = "#23311C"
```

说明：

- `shadow_offset`：阴影偏移量。
- `border_width`：边框厚度。
- `border_color`：边框颜色。
- `shadow_color`：阴影颜色。

逻辑说明：

- 这些都是按钮外观参数。
- 单独提成变量，后面改样式更方便。

#### 第 155 行

代码：`def build_round_layer(left, top, right, bottom, corner_radius, fill_color, layer_tag):`

说明：

- 这是 `draw_round_button` 里面的一个内部函数。
- 它专门负责画出“一整层圆角矩形”。

内部函数的意义：

- 你要画阴影层、边框层、填充层，它们的形状构造方式几乎一样。
- 所以抽成一个小函数，避免重复写很多遍。

#### 第 156 行到第 163 行

代码：

```python
return [
    canvas.create_rectangle(...),
    canvas.create_rectangle(...),
    canvas.create_oval(...),
    canvas.create_oval(...),
    canvas.create_oval(...),
    canvas.create_oval(...),
]
```

这段是“圆角按钮如何拼出来”的几何核心。

为什么不是直接一个圆角矩形？

- 因为 Tkinter 的 `Canvas` 没有一个特别顺手的原生“圆角矩形”方法。
- 所以这里手工拼：
  - 一个横向中间矩形
  - 一个纵向中间矩形
  - 四个角上的圆

具体拆解：

- 第 157 行那个 `create_rectangle(...)`
  负责中间横条。
- 第 158 行那个 `create_rectangle(...)`
  负责中间竖条。
- 第 159 行
  负责左上角圆。
- 第 160 行
  负责右上角圆。
- 第 161 行
  负责左下角圆。
- 第 162 行
  负责右下角圆。
- 第 163 行的 `]`
  表示列表结束。

为什么要 `return [...]`：

- 每次 `canvas.create_...(...)` 都会返回一个画布对象 ID。
- 把这些 ID 存在列表里，后面悬停时才能逐个改颜色。

#### 第 165 行到第 173 行

代码：

```python
build_round_layer(
    x1 + shadow_offset,
    y1 + shadow_offset,
    x2 + shadow_offset,
    y2 + shadow_offset,
    radius,
    shadow_color,
    f"{tag}_shadow",
)
```

说明：

- 这是在画阴影层。
- 之所以坐标都加上 `shadow_offset`，是为了让阴影比按钮本体稍微向右下偏一点。

逻辑作用：

- 产生立体感。

#### 第 174 行

代码：`border_ids = build_round_layer(x1, y1, x2, y2, radius, border_color, tag)`

说明：

- 这是画边框层。
- 返回的那些图形 ID 保存到 `border_ids`。

#### 第 175 行到第 183 行

代码：

```python
part_ids = build_round_layer(
    x1 + border_width,
    y1 + border_width,
    x2 - border_width,
    y2 - border_width,
    max(2, radius - border_width),
    color,
    tag,
)
```

说明：

- 这是画内部填充层。
- 它比边框层略微向里缩进，所以看起来像边框包住了中间内容。
- `max(2, radius - border_width)` 表示内层圆角半径不要小到离谱，至少保留 2。

#### 第 185 行到第 192 行

代码：

```python
canvas.create_text(
    (x1 + x2) / 2,
    (y1 + y2) / 2,
    text=text,
    fill=text_color,
    font=("Arial", 9, "bold"),
    tags=tag,
)
```

说明：

- 这是在按钮中心画文字。
- `(x1 + x2) / 2`：求水平中心点。
- `(y1 + y2) / 2`：求垂直中心点。
- `text=text`：显示按钮文字。
- `fill=text_color`：文字颜色。
- `font=("Arial", 9, "bold")`：字体设置。
- `tags=tag`：让文字也加入同一个按钮标签组。

逻辑重点：

- 文字也要带上同一个 `tag`。
- 否则鼠标移到文字上时，事件可能只作用到文字，不作用到按钮图形，交互体验会割裂。

#### 第 194 行到第 198 行

代码：

```python
def on_enter(event):
    for part_id in part_ids:
        canvas.itemconfig(part_id, fill=hover_color, outline=hover_color)
    for border_id in border_ids:
        canvas.itemconfig(border_id, fill="#446735", outline="#446735")
```

说明：

- 这是鼠标进入按钮区域时执行的函数。
- `event` 是 Tkinter 事件对象，虽然这里没直接用它，但事件回调函数通常要接这个参数。
- 第一段循环把内部填充层改成悬停颜色。
- 第二段循环把边框层也改成稍亮一点的颜色。

#### 第 200 行到第 204 行

代码：

```python
def on_leave(event):
    for part_id in part_ids:
        canvas.itemconfig(part_id, fill=color, outline=color)
    for border_id in border_ids:
        canvas.itemconfig(border_id, fill=border_color, outline=border_color)
```

说明：

- 这是鼠标移开按钮时执行的函数。
- 它把颜色恢复成默认状态。

#### 第 206 行到第 208 行

代码：

```python
canvas.tag_bind(tag, "<Enter>", on_enter)
canvas.tag_bind(tag, "<Leave>", on_leave)
canvas.tag_bind(tag, "<Button-1>", lambda event: command())
```

逐项说明：

- `tag_bind(...)`：给某个标签组绑定事件。
- `"<Enter>"`：鼠标进入。
- `"<Leave>"`：鼠标离开。
- `"<Button-1>"`：鼠标左键单击。
- `lambda event: command()`：创建一个小匿名函数，接住 Tkinter 传进来的 `event`，然后真正调用你传进来的业务函数 `command()`。

为什么点击这里用 `lambda`：

- Tkinter 绑定点击事件时，会自动把 `event` 参数传给回调。
- 但你这里的 `eat()`、`sleep()` 这些函数没有参数。
- 所以要用 `lambda event: command()` 做一层适配。

---

### 第 211 行到第 214 行

代码：

```python
draw_round_button(canvas, 446, 258, 525, 284, 12, "#7AA95C", "#678F4D", "Eat", "#F5F7EE", eat)
draw_round_button(canvas, 531, 258, 610, 284, 12, "#88B86B", "#739D59", "Sleep", "#F5F7EE", sleep)
draw_round_button(canvas, 616, 258, 695, 284, 12, "#5F8E4C", "#4F7840", "Hit", "#F5F7EE", hit)
draw_round_button(canvas, 701, 258, 780, 284, 12, "#9BC782", "#84AD6D", "Caress", "#F5F7EE", caress)
```

说明：

- 这是四次实际创建按钮。
- 参数顺序完全对应 `draw_round_button(...)` 的定义。

以第一行为例：

- `canvas`：画到这个画布上。
- `446, 258, 525, 284`：按钮矩形范围。
- `12`：圆角半径。
- `"#7AA95C"`：默认颜色。
- `"#678F4D"`：悬停颜色。
- `"Eat"`：文字。
- `"#F5F7EE"`：文字颜色。
- `eat`：点击后执行的函数。

后面三行同理，只是位置、颜色、文字、回调函数不同。

---

### 第 216 行

代码：`root.protocol("WM_DELETE_WINDOW", on_close)`

单词说明：

- `protocol`：设置窗口协议处理。
- `"WM_DELETE_WINDOW"`：窗口关闭事件名。
- `on_close`：关闭时调用的函数。

逻辑说明：

- 这行的意思是：当用户点击窗口关闭按钮时，不要直接粗暴退出，而是先走 `on_close()` 这套清理逻辑。

---

### 第 217 行

代码：`start_background_video()`

逻辑说明：

- 正式启动背景视频。
- 如果视频加载失败，这个函数会很安静地退出，界面仍保留静态背景图。

---

### 第 218 行

代码：`root.mainloop()`

单词说明：

- `mainloop`：主事件循环。

逻辑说明：

- 这是 Tkinter 应用的心跳。
- 没有这一行，窗口会一闪而过，或者根本不进入正常交互状态。
- 有了它，Tkinter 才会持续处理：
  - 鼠标移动
  - 鼠标点击
  - 定时器回调
  - 窗口刷新
  - 关闭事件

---

## 6. 这个工程里最关键的逻辑链

如果你只记 5 条主线，最该记的是这 5 条：

### 主线 1：资源定位

- 用 `BASE_DIR = Path(__file__).resolve().parent` 找到当前工程目录。
- 再从这个目录去拼视频、图片、依赖路径。

意义：

- 让程序不依赖“你从哪一个终端目录运行它”。

### 主线 2：本地依赖注入

- 如果 `.vendor` 存在，就 `sys.path.insert(0, str(VENDOR_DIR))`。

意义：

- 项目自带依赖，不强迫全局 Python 环境必须预装。

### 主线 3：视频预加载

- `load_video_frames(video_path)` 会把指定片段读成很多 `PhotoImage`。
- `get_video_clip(video_path)` 会把结果缓存起来。

意义：

- 播放时更顺。
- 同一个动作第二次播放时更快。
- 缺点是第一次加载某个新片段时会稍慢、内存占用也会更高。

### 主线 4：按时间轴选帧

- `elapsed * video_fps` 算出理论帧位置。
- 循环片段用 `int(...) % len(video_frames)` 回绕。
- 单次片段用 `min(...)` 卡到最后一帧，并在结束时触发回调。

意义：

- 即使某次回调稍微晚了，也不会单纯“傻傻地只加 1 帧”，而是按真实经过时间去追当前应该显示的画面。
- 这也是 `Eat` 动画能“播一遍就回到待机”的关键。

### 主线 5：Tkinter 事件循环

- `root.after(...)` 负责安排下一次刷新。
- `root.mainloop()` 负责让整套 GUI 活起来。

意义：

- GUI 程序不是靠 `while True` 死循环硬刷的。
- 更标准的方式是把工作交给事件系统。

---

## 7. 这个工程为什么这样设计

### 为什么先显示 `background.png`

因为视频加载不是瞬间完成的。

如果不先放一张图：

- 窗口刚打开时可能是空白。
- 视频读失败时界面可能完全没有背景。

先放静态图，是一个很实用的用户体验兜底。

### 为什么把视频帧预加载到列表里

因为“边播边解码边缩放”通常更卡。

预加载的好处：

- 播放更平滑。
- 每次刷新时只需要换图，不需要重复做重计算。

代价：

- 启动时要等待一点时间。
- 会占内存。

### 为什么要自己画按钮，而不是直接用 `tk.Button`

因为 `tk.Button` 的视觉风格比较受系统默认样式影响。

自己在 `Canvas` 上拼按钮的好处：

- 位置控制更自由。
- 样式更统一。
- 可以更轻松做阴影、边框、悬停变色。

---

## 8. 这个工程里最值得你模仿的写法

### 写法 1：把路径统一抽成常量

好处：

- 易改。
- 易读。
- 不容易把字符串路径写散到各处。

### 写法 2：有兜底逻辑

例如：

- `imageio` 导入失败就回退到静态图。
- 视频不存在就直接返回空帧列表。

这叫“防御式编程”。

### 写法 3：资源加载和播放分离

- `load_video_frames(...)` 负责准备片段数据。
- `get_video_clip(...)` 负责缓存管理。
- `play_video(...)` 负责切换当前片段。
- `show_video_frame()` 负责真正刷帧显示。

这样结构更清楚。

### 写法 4：复杂图形用辅助函数抽象

- `build_round_layer(...)` 就是一个很典型的内部辅助函数。

### 写法 5：把关闭窗口的清理逻辑显式写出来

- `root.protocol("WM_DELETE_WINDOW", on_close)`

很多初学者会忽略这一层，但这是好习惯。

---

## 9. 你接下来最适合练的修改题

如果你想真正学会，不要只看笔记，最好改几次代码。

建议你按下面顺序练：

1. 把窗口大小改成 `1000x400`，并同步调整按钮位置。
2. 给 `sleep()` 再接一个 `sleep.mp4`，让它也像 `Eat` 一样播完回待机。
3. 给 `hit()` 接一个只播放一次的动作视频，并让它播完回待机。
4. 把按钮文字字体改大，并尝试换一种颜色主题。
5. 在界面上加一个数值，比如“mood: 100”。
6. 给 `caress()` 加一个短暂的按钮闪光效果。

你每改一次，最好都问自己：

- 这个变量是全局还是局部？
- 这个函数是现在执行，还是以后被回调执行？
- 这个对象是 Pillow 图片，还是 Tkinter 图片？
- 这个坐标是在窗口里，还是在画布里？

---

## 10. 最后给这份工程下一个“人话定义”

如果把整个工程翻译成人话，它其实就是：

“先找自己的目录，找到待机视频、吃饭视频、图片和依赖；再创建一个固定大小的 Tkinter 窗口；先放一张背景图；如果本地视频能读，就把不同视频片段拆成很多帧并缓存起来；平时循环播放 `background.mp4`；点击 `Eat` 时临时切到 `eat.mp4` 播一遍；播完后自动回到待机；最后在背景上画四个带阴影和悬停效果的圆角按钮，并进入 GUI 事件循环。”

如果你已经能理解上面这句话，再回头看代码，你会发现：

- 代码不再是一堆陌生符号。
- 它已经变成了一连串很具体的动作。

这就是“会读代码”的开始。
