number = input()
counter = 0
sum_ = 0
while number != '.':
    sum_ += int(number)
    counter += 1
    number = input()
print(sum_ / counter)
