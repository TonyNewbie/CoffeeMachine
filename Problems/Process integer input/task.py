number = int(input())
while number < 101:
    if number < 10:
        number = int(input())
        continue
    print(number)
    number = int(input())
