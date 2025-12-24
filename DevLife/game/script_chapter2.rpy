label chapter_2:
    # 确保音乐是对的（如果从视频那边过来可能需要恢复，如果从Bob那边过来可能已经有了）
    play music "audio/work_bgm.mp3" if_changed
    
    scene bg office
    show alice happy at center with dissolve
    
    voice "audio/voice_en.mp3"
    a "It's getting late. (Chapter 2 Begins)"
    
    menu:
        "What should we eat?"

        "Order Pizza":
            hide alice
            show manager normal at center with dissolve
            voice "audio/voice_en.mp3"
            b "I love Pizza!"

        "Eat Salad":
            $ bug_fixed += 1
            voice "audio/voice_en.mp3"
            a "Healthy choice."

    # 剧情结束，去结局判断
    jump ending_judge