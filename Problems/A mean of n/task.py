number_of_values = int(input())
sum_ = 0
values = [int(input()) for i in range(number_of_values)]
for value in values:
    sum_ += value
print(sum_ / number_of_values)
