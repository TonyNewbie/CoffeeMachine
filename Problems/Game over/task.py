scores = input().split()
# put your python code here
right_answers = 0
wrong_answers = 0
for score in scores:
    if score == 'C':
        right_answers += 1
    else:
        wrong_answers += 1
        if wrong_answers == 3:
            print('Game over')
            print(right_answers)
            break
else:
    print('You won')
    print(right_answers)
