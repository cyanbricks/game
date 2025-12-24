label start:
    # 1. 播放开场音乐
    play music "audio/intro_bgm.mp3" fadein 2.0
    
    # 2. 设置初始场景
    scene bg office 
    
    # 3. 进入第一章
    jump chapter_1


# --- 结局判断逻辑 (所有章节结束后都会跳到这里) ---
label ending_judge:
    scene bg office
    # 隐藏所有角色
    hide alice
    hide manager
    hide bob # 如果你也定义了 bob 的图片

    if bug_fixed >= 2:
        "You fixed enough bugs and stayed healthy. (Good Ending)"
    else:
        "The project crashed. (Bad Ending)"

    # 游戏结束，返回主菜单
    return