label chapter_1:
    # Alice 登场
    show alice happy at center with dissolve
    voice "audio/voice_en.mp3"
    a "Hi, I am Alice. Welcome to the team."

    # Bob 登场 (Alice 消失)
    hide alice with dissolve
    show manager normal at center with dissolve
    voice "audio/voice_en.mp3"
    b "I am Bob. Let's fix some bugs."

    # --- 第一次选择 ---
    menu:
        "Which bug should we fix first?"

        "Fix the UI bug (Play Video)":
            $ bug_fixed += 1
            
            # === 【看这里！极其优雅的视频调用】 ===
            # 直接调用定义的工具 label，传入视频名字和时长
            call play_video("boom_video", 5.0)
            # ===================================
            
            # 视频播完后，恢复背景音乐
            play music "audio/work_bgm.mp3" fadein 2.0
            scene bg office
            show alice happy at center with dissolve
            voice "audio/voice_en.mp3"
            a "Good choice. UI is important."

        "Fix the Database bug (Bob's Side Story)":
            # 跳转到 Bob 的支线文件
            jump side_bob_story

    # 无论选了哪个，最后都去第二章
    jump chapter_2