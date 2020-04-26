class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = 1 / 2 * self.a * self.b


parameters = input().split()
c = int(parameters[0])
a = int(parameters[1])
b = int(parameters[2])
if c ** 2 == a ** 2 + b ** 2:
    triangle = RightTriangle(c, a, b)
    print(triangle.area)
else:
    print('Not right')
