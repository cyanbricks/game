label side_bob_story:
    # 既然是 Bob 的支线，只显示 Bob
    hide alice
    show manager normal at center with dissolve
    
    voice "audio/voice_en.mp3"
    b "Backend is the backbone of the app."
    b "Let me show you the server logs."
    
    "Bob shows you a pile of complex code..."
    
    $ bug_fixed += 1
    
    b "See? Solid as a rock."
    
    # 支线结束，跳回主线（第二章）
    jump chapter_2