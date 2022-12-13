n = int(input())
l1 = input().split()
list_groups = []

number_cars = 0
sum_students = 0


for i in l1:
    list_groups.append(int(i))
    
x = len(list_groups)
list_groups.sort()

while True:
    if len(list_groups) == 0:
        break
        
    for i in list_groups:
        sum_students += i
        list_groups.remove(i)
        
        if sum_students > 4:
            list_groups.append(i)
            list_groups.sort()
            sum_students = 0
            number_cars += 1
            break
            
        elif sum_students == 4:
            sum_students = 0
            number_cars += 1
            break
        
        elif sum_students < 4 :
            break
    
print(number_cars)
