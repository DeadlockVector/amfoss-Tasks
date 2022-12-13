#ARROW REFERENCE
n = int(input())   #input number of points

list_points = []
optimal_list = []
for i in range(n):
    (x, y) = map(int, input().split())    #taking input of each point
    list_points.append([x, y])            #appending each point to a mested list
    
for i in list_points:
    lower = 0                            #for an optimal point, needs to have 1 lower, 1 upper, 1 left, 1 right
    right = 0                            #initialising counter variables
    left = 0
    upper = 0
    for j in list_points:
        if j[0] == i[0] and j[1] < i[1]:         #checking condition for lower, right, left, upper
            lower += 1
        elif j[0] > i[0] and j[1] == i[1]:
            right += 1
        elif j[0] < i[0] and j[1] == i[1]:
            left += 1
        elif j[0] == i[0] and j[1] > i[1]:
            upper += 1
        
    if lower >= 1 and right >= 1 and left >= 1 and upper >= 1:    #checking if it satisifes condition and appending to
        optimal_list.append(i)                                       #optimal list
        
print(len(optimal_list))         #number of optimal points = length of optimal list
