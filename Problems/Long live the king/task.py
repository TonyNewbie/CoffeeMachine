column = int(input())
row = int(input())
if column == 1 and row == 1:
    print(3)
elif column == 8 and row == 8:
    print(3)
elif column == 1 and row == 8:
    print(3)
elif column == 8 and row == 1:
    print(3)
elif column == 1 and row <= 7:
    print(5)
elif column <= 7 and row == 1:
    print(5)
elif column == 8 and row <= 7:
    print(5)
elif column <= 7 and row == 8:
    print(5)
else:
    print(8)
