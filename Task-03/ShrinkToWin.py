n = int(input())       #input the number
number = n
n_str = str(n)        #converting number to string

count = 0
flag = True
count_digits = 0
if len(str(n)) < 2:    #if its already single digit, no operations required
    print(0)
    
else:
    while True:
        sum_digits = 0      
        for i in str(n):
            sum_digits += int(i)    #extracting each digit, adding to sum_digits
            
        count += 1               #incrementing number of steps
        n = sum_digits
        if len(str(n)) == 1:        #if the length of the sum is 1, breaking the loop else continue
            print(count)
            break
