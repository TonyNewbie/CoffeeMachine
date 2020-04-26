# put your python code here
a = int(input())
b = int(input())
sum_ = 0
amount = 0
for number in range(a, b + 1):
    if number % 3 == 0:
        sum_ += number
        amount += 1
print(sum_ / amount)
