def solution(bandage, health, attacks):
    attacks.append([attacks[-1][0], 0])    
    h_du, h_per_sec, h_add = bandage
    max_health = health # 저장 필요
    
    i = 0
    
    while i < len(attacks) - 1:     
        health -= attacks[i][1]
        
        if health <= 0:
            return -1
        
        h_time = attacks[i+1][0] - attacks[i][0]  - 1
        
        if h_time > 0: # 이부분이 발목
            health += h_per_sec * h_time
            health += (h_time // h_du) * h_add # 아 깜빡 
        
            
        health = min(health, max_health)       
        
        i += 1
            
    return health
             
        
