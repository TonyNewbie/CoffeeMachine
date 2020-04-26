number = input()
minimum = float(number)
while number != '.':
    if float(number) < minimum:
        minimum = float(number)
    number = input()
print(minimum)
