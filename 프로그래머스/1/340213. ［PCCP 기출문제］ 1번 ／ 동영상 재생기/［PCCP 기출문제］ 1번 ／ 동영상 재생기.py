def solution(video_len, pos, op_start, op_end, commands):
    # 변수 위치
    len_h, len_m = map(int, video_len.strip("\"").split(":"))
    vi_len = len_h*60 + len_m
        
    pos_h, pos_m = map(int, pos.strip("\"").split(":"))    
    pos_len = pos_h*60 + pos_m 
        
    start_h, start_m = map(int, op_start.strip("\"").split(":"))
    start_len = start_h*60 + start_m
        
    end_h, end_m = map(int, op_end.strip("\"").split(":"))    
    end_len = end_h*60 + end_m 
    
    for command in commands:
        if start_len <= pos_len and pos_len <=  end_len:
            pos_len = end_len
        
        if command == "prev":
            pos_len -= 10
            if pos_len < 10:
                pos_len = 0        
                
        elif command == "next":
            pos_len += 10
            if (vi_len-10) < pos_len:
                pos_len = vi_len
                
        if start_len <= pos_len and pos_len <=  end_len:
            pos_len = end_len
    
    ho = pos_len//60
    mi = pos_len%60
    
    if ho < 10:
        ho = "0"+str(ho)
    if mi < 10:
        mi = "0"+str(mi)
    
    return f"{ho}:{mi}"

# start_len, pos_len, end_len
# pos_len//60, pos_len%60
