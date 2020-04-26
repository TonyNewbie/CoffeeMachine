money = int(input())
count = 0
if money >= 6789:
    count = money // 6789
    print(count, 'sheep')
elif money >= 3848:
    count = money // 3848
    if count > 1:
        print(count, 'cows')
    else:
        print(count, 'cow')
elif money >= 1296:
    count = money // 1296
    if count > 1:
        print(count, 'pigs')
    else:
        print(count, 'pig')
elif money >= 678:
    count = money // 678
    if count > 1:
        print(count, 'goats')
    else:
        print(count, 'goat')
elif money >= 23:
    count = money // 23
    if count > 1:
        print(count, 'chickens')
    else:
        print(count, 'chicken')
else:
    print('None')
