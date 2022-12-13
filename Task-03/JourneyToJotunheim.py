for i in range(int(input())):     #for loop for number of input test cases
    number_keys = int(input())
    (a, b, c) = map(int, input().split())     #input for keys
    abc = str(a) + str(b) + str(c)            #making a string for with each key concatenated
    
    if a==1 or b==2 or c==3:
        print('NO')                          #if any key is behind its own portal, there's no way to access it
    else:
        if ('1' not in abc) and abc[0] == '0':    #if there's a key behind door 1 and we don't have key 1, can't access
            print('NO')
        elif ('2' not in abc) and abc[1] == '0':    #same for the doors 2 and 3
            print('NO')
        elif ('3' not in abc) and abc[2] == '0':
            print('NO')
        else:
            print('YES')                    #else, possible
