t = int(input())
for i in range(t):
    n = int(input())
    list_heroes = input().split() #levels of heroes in a list
    
    more_than_one = False
    for j in list_heroes:
        if list_heroes.count(j) > 1:
            more_than_one = True
            break 
        else:
            continue
                 
    if '0' in list_heroes:
        print(n - list_heroes.count('0'))  #if 1 or more zeroes in list each hero can be debuffed with the zero
    
    elif more_than_one == True:         #No zeroes and similar hero levels
        print(n)
        
    else:
        print(n+1)                #no zeroes and no similar hero levels
