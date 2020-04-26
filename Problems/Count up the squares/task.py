sum1, sum2 = 0, 0
while True:
    num = int(input())
    sum1 += num
    sum2 += num ** 2
    if sum1 == 0:
        print(sum2)
        break
