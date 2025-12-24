# ==========================================
# 1. 初始化配置 (字体、语言、快捷键)
# ==========================================
init python:
    # --- 全局强制字体 (防止中文变框框) ---
    style.default.font = "SourceHanSansSC-Regular.otf"
    style.say_dialogue.font = "SourceHanSansSC-Regular.otf"
    style.say_label.font = "SourceHanSansSC-Regular.otf"
    style.button_text.font = "SourceHanSansSC-Regular.otf"
    style.label_text.font = "SourceHanSansSC-Regular.otf"

    # --- L键切换语言逻辑 ---
    def toggle_language():
        if _preferences.language == None:
            renpy.change_language("schinese")
            renpy.notify("Language: Chinese") # 屏幕左上角会弹提示
        else:
            renpy.change_language(None)
            renpy.notify("Language: English") # 屏幕左上角会弹提示
        renpy.restart_interaction()

    config.keymap['toggle_language'] = ['L', 'l']
    config.underlay.append(renpy.Keymap(toggle_language=toggle_language))

# ==========================================
# 2. 角色定义
# ==========================================
define a = Character("Alice", color="#c8ffc8")
define b = Character("Bob", color="#c8c8ff")
define m = Character("Manager", color="#ffcc00")

# ==========================================
# 3. 变量定义
# ==========================================
default bug_fixed = 0

# ==========================================
# 4. 图片资源映射
# ==========================================
image bg office = "images/bg_office.jpg"
image alice happy = "images/char_a.png"
image manager normal = "images/manager_normal.png"

# 视频定义 (WebM 格式)
image boom_video = Movie(play="videos/explosion.webm", size=(1920, 1080), loop=False)

# ==========================================
# 5. 【核心工具】通用视频播放函数
# ==========================================
# 以后你要播视频，只要写： call play_video("boom_video", 5.0)
label play_video(video_img, duration=5.0):
    # 1. 停止音乐
    stop music fadeout 1.0
    
    # 2. 移除对话框 (让界面干净)
    window hide
    
    # 3. 【关键修改】清空现场！
    # scene black 会移除所有背景和人物，确保没有任何东西残留
    scene black with dissolve

    # 4. 播放视频
    show expression video_img as current_video
    
    # 5. 等待播放结束
    $ renpy.pause(duration, hard=True)

    # 6. 移除视频
    hide current_video
    
    # 此时屏幕是全黑的，等待外部代码恢复场景
    return