for i in range(int(input())):
    n = int(input())
    monsters  = input().split()
    
    possible = True
    
        
    for i in range(len(monsters)):
        if monsters[0] == monsters[1] and monsters[0] != '1':
            possible = False
            break 
            
        if i == len(monsters) - 1:
            break
            
        if int(monsters[i]) > int(monsters[i+1]) and i == 0:
            possible = False
            break
        
            
        else:
            continue
        
    if possible == False:
        print('NO')
    else:
        print('YES')
