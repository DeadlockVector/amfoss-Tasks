#WHY ARE THERE 20 TEST CASES

(money, number_men) = map(int, input().split())

if number_men > money:
    print(-1)

elif money%2 == 0:
    if (money/2)%number_men == 0:
        print(money//2)
    else:
        for i in range(1, money//2+1):
            if ((money/2)+i)%number_men == 0:
                print((money//2)+i)
                break
            else:
                print(-1)
                
elif money%2 != 0:
    if (money//2 +1)%number_men == 0:
        print(money//2 + 1)
    else:
        for i in range(1, money//2+2):
            if ((money//2+1) + i)%number_men == 0:
                print((money//2+1)+i)
                break
            else:
                print(-1)
else:
    print(-1)
