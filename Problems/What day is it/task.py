offset = int(input())
if offset + 10 >= 24:
    print('Wednesday')
elif offset + 10 < 0:
    print('Monday')
else:
    print('Tuesday')
