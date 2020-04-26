number = int(input())
counter = 0
if number == 1:
    print('This number is not prime')
else:
    for i in range(1, number):
        if number % i == 0:
            counter += 1
        if counter > 1:
            print('This number is not prime')
            break
    else:
        print('This number is prime')
