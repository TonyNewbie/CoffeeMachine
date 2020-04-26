number_of_values = int(input())
values = [int(input()) for i in range(number_of_values)]
for value in values:
    if value % 7 == 0:
        print(value * value)
