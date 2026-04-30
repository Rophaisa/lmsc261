from pathlib import Path  # 导入路径类
import sys  # 用来调整模块搜索路径
import time  # 用来计算播放经过时间

BASE_DIR = Path(__file__).resolve().parent  # 获取当前脚本所在目录
VENDOR_DIR = BASE_DIR / ".vendor"  # 本地依赖目录路径
WINDOW_WIDTH = 800  # 窗口宽度
WINDOW_HEIGHT = 300  # 窗口高度
IDLE_VIDEO_PATH = BASE_DIR / "background.mp4"  # 待机视频路径
EAT_VIDEO_PATH = BASE_DIR / "eat.mp4"  # 吃饭视频路径
IMAGE_PATH = BASE_DIR / "background.png"  # 静态兜底背景图路径

if VENDOR_DIR.exists():  # 如果本地依赖目录存在
    sys.path.insert(0, str(VENDOR_DIR))  # 优先从项目内加载依赖

from PIL import Image, ImageTk  # 导入图片处理和 Tkinter 图片桥接
import tkinter as tk  # 导入图形界面库

try:  # 尝试导入视频读取库
    import imageio.v2 as imageio  # 用 imageio 读取 mp4 帧
except ImportError:  # 如果导入失败
    imageio = None  # 记为空，后面走兜底逻辑

root = tk.Tk()  # 创建主窗口
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")  # 设置窗口大小
root.title("Beta V1")  # 设置窗口标题
root.resizable(False, False)  # 禁止调整窗口大小

background_image = Image.open(IMAGE_PATH).resize(  # 打开并缩放静态背景图
    (WINDOW_WIDTH, WINDOW_HEIGHT),  # 目标尺寸和窗口一致
    Image.Resampling.BILINEAR,  # 使用双线性缩放
)  # 完成背景图缩放
current_background = ImageTk.PhotoImage(background_image)  # 转成 Tkinter 可显示图片
video_cache = {}  # 缓存已加载过的视频片段
video_frames = []  # 当前正在播放的帧列表
video_after_id = None  # 保存 after 定时器编号
video_fps = 24.0  # 当前片段的帧率默认值
video_duration = 0.0  # 当前片段总时长
video_start_time = 0.0  # 当前片段开始播放的时间点
video_loop = True  # 当前片段是否循环播放
video_on_complete = None  # 当前片段播完后的回调


def eat():  # 点击 Eat 按钮时执行
    print("Eat button clicked")  # 在终端打印调试信息
    play_video(EAT_VIDEO_PATH, loop=False, on_complete=start_background_video)  # 播放吃饭动画，结束后回待机


def sleep():  # 点击 Sleep 按钮时执行
    print("Sleep button clicked")  # 先打印调试信息


def hit():  # 点击 Hit 按钮时执行
    print("Hit button clicked")  # 先打印调试信息


def caress():  # 点击 Caress 按钮时执行
    print("Caress button clicked")  # 先打印调试信息


canvas = tk.Canvas(  # 创建主画布
    root,  # 把画布放进主窗口
    width=WINDOW_WIDTH,  # 画布宽度
    height=WINDOW_HEIGHT,  # 画布高度
    highlightthickness=0,  # 去掉默认高亮边框
)  # 完成画布创建
canvas.pack()  # 把画布显示到窗口里
bg_item = canvas.create_image(0, 0, anchor="nw", image=current_background)  # 在左上角放初始背景图
canvas.tag_lower(bg_item)  # 把背景放到最底层


def stop_video_playback():  # 停止当前视频播放
    global video_after_id  # 需要改全局定时器编号
    global video_on_complete  # 需要清空全局结束回调

    if video_after_id is not None:  # 如果还有未执行的刷新任务
        root.after_cancel(video_after_id)  # 取消这次定时刷新
        video_after_id = None  # 清空定时器记录
    video_on_complete = None  # 清空结束回调


def load_video_frames(video_path):  # 按路径加载一个视频片段
    if not video_path.exists():  # 如果视频文件不存在
        return {"frames": [], "fps": 24.0, "duration": 0.0}  # 返回空片段数据

    if imageio is None:  # 如果视频库不可用
        print("imageio is not available, using background.png instead.")  # 打印兜底提示
        return {"frames": [], "fps": 24.0, "duration": 0.0}  # 返回空片段数据

    frames = []  # 存放转换后的所有帧
    reader = None  # 先准备读取器变量
    fps = 24.0  # 默认帧率
    duration_seconds = 0.0  # 默认时长

    try:  # 尝试读取视频
        reader = imageio.get_reader(str(video_path), format="ffmpeg")  # 创建 ffmpeg 读取器
        meta = reader.get_meta_data()  # 读取视频元数据
        fps = max(1.0, float(meta.get("fps") or 24.0))  # 先从元数据取帧率
        duration_seconds = max(0.0, float(meta.get("duration") or 0.0))  # 先从元数据取时长

        for frame in reader:  # 逐帧遍历视频
            image = Image.fromarray(frame).resize(  # 把数组帧转成并缩放为图片
                (WINDOW_WIDTH, WINDOW_HEIGHT),  # 缩放到窗口尺寸
                Image.Resampling.BILINEAR,  # 使用双线性插值
            )  # 完成单帧缩放
            frames.append(ImageTk.PhotoImage(image))  # 转成 Tkinter 图片后加入列表

        if frames and duration_seconds > 0:  # 如果有有效帧和时长
            fps = max(1.0, len(frames) / duration_seconds)  # 用总帧数和时长重算真实帧率
    except Exception as error:  # 如果读取过程中报错
        print(f"Unable to load video {video_path.name}: {error}")  # 打印错误信息
        frames = []  # 出错时清空帧列表
    finally:  # 无论成功失败都执行收尾
        if reader is not None:  # 如果读取器真的创建成功了
            reader.close()  # 关闭读取器释放资源

    return {"frames": frames, "fps": fps, "duration": duration_seconds}  # 返回片段数据


def get_video_clip(video_path):  # 从缓存获取或首次加载片段
    clip = video_cache.get(video_path)  # 先查缓存里有没有
    if clip is None:  # 如果缓存里还没有
        clip = load_video_frames(video_path)  # 立即加载这个视频片段
        video_cache[video_path] = clip  # 把结果存进缓存
    return clip  # 返回片段数据


def show_video_frame():  # 按当前播放状态显示一帧
    global current_background  # 需要改全局当前背景
    global video_after_id  # 需要记录新的定时器编号
    global video_on_complete  # 可能会清空结束回调

    if not video_frames:  # 如果当前没有可播放的帧
        return  # 直接结束这次刷新

    video_after_id = None  # 当前回调已开始执行，先清空旧编号
    elapsed = time.perf_counter() - video_start_time  # 计算片段已播放多久
    frame_position = elapsed * video_fps  # 算出理论上走到第几帧

    if video_loop:  # 如果当前片段需要循环
        frame_index = int(frame_position) % len(video_frames)  # 用取模回到开头
    else:  # 如果当前片段只播放一次
        frame_index = min(len(video_frames) - 1, int(frame_position))  # 最多停在最后一帧

    current_background = video_frames[frame_index]  # 取出当前要显示的帧
    canvas.itemconfig(bg_item, image=current_background)  # 把背景切换到这帧

    if not video_loop and elapsed >= video_duration:  # 如果单次片段已经播完
        callback = video_on_complete  # 先取出结束回调
        video_on_complete = None  # 立刻清空回调，避免重复执行
        if callback is not None:  # 如果确实有回调函数
            callback()  # 执行回调，比如回到待机视频
        return  # 播完后不再安排下一帧

    frames_until_next = 1.0 - (frame_position - int(frame_position))  # 算出距离下一帧还差多少帧
    next_delay_seconds = frames_until_next / video_fps  # 把剩余帧数换算成秒
    if not video_loop and video_duration > 0:  # 如果是单次片段并且时长有效
        next_delay_seconds = min(  # 取更小的等待时间
            next_delay_seconds,  # 正常到下一帧的等待秒数
            max(0.0, video_duration - elapsed),  # 或者离片段结束剩余的秒数
        )  # 完成单次片段的时间裁剪

    next_delay_ms = max(1, int(next_delay_seconds * 1000))  # 把下一次刷新时间转成毫秒
    video_after_id = root.after(next_delay_ms, show_video_frame)  # 注册下一次帧刷新


def play_video(video_path, loop=True, on_complete=None):  # 切换并播放一个视频片段
    global video_frames  # 需要替换当前帧列表
    global video_fps  # 需要更新当前帧率
    global video_duration  # 需要更新当前片段时长
    global video_start_time  # 需要记录新的开始时间
    global video_loop  # 需要更新循环模式
    global video_on_complete  # 需要登记结束回调

    stop_video_playback()  # 先停掉上一个片段的刷新

    clip = get_video_clip(video_path)  # 取出目标片段的数据
    video_frames = clip["frames"]  # 把当前帧列表切到这个片段
    if not video_frames:  # 如果这个片段没有可用帧
        if on_complete is not None:  # 如果还给了兜底回调
            on_complete()  # 直接执行兜底回调
        return  # 没法播放就结束

    video_fps = clip["fps"]  # 更新当前片段帧率
    video_duration = clip["duration"]  # 更新当前片段时长
    video_start_time = time.perf_counter()  # 记录这个片段的起播时刻
    video_loop = loop  # 记录这个片段是否循环
    video_on_complete = on_complete  # 记录播完后要做什么
    show_video_frame()  # 立即显示第一帧并启动刷新循环


def start_background_video():  # 启动待机背景视频
    play_video(IDLE_VIDEO_PATH, loop=True)  # 播放待机视频并保持循环


def on_close():  # 关闭窗口时执行
    stop_video_playback()  # 先停止所有视频刷新
    root.destroy()  # 再销毁主窗口


def draw_round_button(canvas, x1, y1, x2, y2, radius, color, hover_color, text, text_color, command):  # 画一个自定义圆角按钮
    # 用同一个标签把按钮的图形和文字绑在一起，后面就能一起改颜色和响应点击。
    tag = f"button_{text.lower()}"  # 为当前按钮生成统一标签
    shadow_offset = 3  # 阴影偏移量
    border_width = 2  # 边框厚度
    border_color = "#355126"  # 边框颜色
    shadow_color = "#23311C"  # 阴影颜色

    def build_round_layer(left, top, right, bottom, corner_radius, fill_color, layer_tag):  # 画出一层圆角矩形
        return [  # 返回这一层所有图形的 ID
            canvas.create_rectangle(left + corner_radius, top, right - corner_radius, bottom, fill=fill_color, outline=fill_color, tags=layer_tag),  # 画中间横矩形
            canvas.create_rectangle(left, top + corner_radius, right, bottom - corner_radius, fill=fill_color, outline=fill_color, tags=layer_tag),  # 画中间竖矩形
            canvas.create_oval(left, top, left + 2 * corner_radius, top + 2 * corner_radius, fill=fill_color, outline=fill_color, tags=layer_tag),  # 画左上角圆
            canvas.create_oval(right - 2 * corner_radius, top, right, top + 2 * corner_radius, fill=fill_color, outline=fill_color, tags=layer_tag),  # 画右上角圆
            canvas.create_oval(left, bottom - 2 * corner_radius, left + 2 * corner_radius, bottom, fill=fill_color, outline=fill_color, tags=layer_tag),  # 画左下角圆
            canvas.create_oval(right - 2 * corner_radius, bottom - 2 * corner_radius, right, bottom, fill=fill_color, outline=fill_color, tags=layer_tag),  # 画右下角圆
        ]  # 完成一层圆角矩形

    build_round_layer(  # 先画按钮阴影层
        x1 + shadow_offset,  # 阴影左边界
        y1 + shadow_offset,  # 阴影上边界
        x2 + shadow_offset,  # 阴影右边界
        y2 + shadow_offset,  # 阴影下边界
        radius,  # 阴影层圆角半径
        shadow_color,  # 阴影层颜色
        f"{tag}_shadow",  # 阴影层标签
    )  # 阴影层绘制完成
    border_ids = build_round_layer(x1, y1, x2, y2, radius, border_color, tag)  # 画边框层并保存 ID
    part_ids = build_round_layer(  # 再画内部填充层
        x1 + border_width,  # 填充层左边界向内缩
        y1 + border_width,  # 填充层上边界向内缩
        x2 - border_width,  # 填充层右边界向内缩
        y2 - border_width,  # 填充层下边界向内缩
        max(2, radius - border_width),  # 内层圆角半径略小一点
        color,  # 填充层默认颜色
        tag,  # 填充层沿用按钮标签
    )  # 填充层绘制完成

    canvas.create_text(  # 在按钮中央画文字
        (x1 + x2) / 2,  # 文字水平中心点
        (y1 + y2) / 2,  # 文字垂直中心点
        text=text,  # 显示的按钮文字
        fill=text_color,  # 文字颜色
        font=("Arial", 9, "bold"),  # 文字字体设置
        tags=tag,  # 文字也绑定到按钮同一标签
    )  # 按钮文字绘制完成

    def on_enter(event):  # 鼠标移入按钮时执行
        for part_id in part_ids:  # 遍历内部填充层
            canvas.itemconfig(part_id, fill=hover_color, outline=hover_color)  # 切换成悬停颜色
        for border_id in border_ids:  # 遍历边框层
            canvas.itemconfig(border_id, fill="#446735", outline="#446735")  # 边框也稍微提亮

    def on_leave(event):  # 鼠标移出按钮时执行
        for part_id in part_ids:  # 遍历内部填充层
            canvas.itemconfig(part_id, fill=color, outline=color)  # 恢复默认颜色
        for border_id in border_ids:  # 遍历边框层
            canvas.itemconfig(border_id, fill=border_color, outline=border_color)  # 恢复默认边框色

    canvas.tag_bind(tag, "<Enter>", on_enter)  # 绑定鼠标移入事件
    canvas.tag_bind(tag, "<Leave>", on_leave)  # 绑定鼠标移出事件
    canvas.tag_bind(tag, "<Button-1>", lambda event: command())  # 绑定鼠标左键点击事件



draw_round_button(canvas, 531, 258, 610, 284, 12, "#7AA95C", "#678F4D", "Eat", "#F5F7EE", eat)  # 画 Eat 按钮
draw_round_button(canvas, 616, 258, 695, 284, 12, "#88B86B", "#739D59", "Hit", "#F5F7EE", hit)  # 画 Hit 按钮
draw_round_button(canvas, 701, 258, 780, 284, 12, "#9BC782", "#84AD6D", "Caress", "#F5F7EE", caress)  # 画 Caress 按钮

root.protocol("WM_DELETE_WINDOW", on_close)  # 绑定窗口关闭时的清理逻辑
start_background_video()  # 启动待机背景视频
root.mainloop()  # 进入 Tkinter 主循环
