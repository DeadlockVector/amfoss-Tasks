#Count number of zeroes after first non zero number
#Total = number of zeroes + sum of non-zero numbers except last number

for i in range(int(input())):
    n = int(input())
    list_watertanks = input().split()        #taking input for each test case
    
    #number_zero = list_watertanks.count('0')
    l1 = []
    s = 0
    
    for i in range(len(list_watertanks)):      
        if list_watertanks[i] != '0':            #finding first non zero element in the list
            index = i
            break

    for x in range(index, len(list_watertanks)-1):
        l1.append(list_watertanks[x])           #appending all elements, starting from index into l1
    
    for j in l1:
        s += int(j)                           #adding each value to s(sum)
    
    print(s + l1.count('0'))         #final value is sum + number of zeroes
