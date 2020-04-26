larger_cats = name = input()
while name != 'MEOW':
    if int(name.split()[-1]) > int(larger_cats.split()[-1]):
        larger_cats = name
    name = input()
print(larger_cats.split()[0])
