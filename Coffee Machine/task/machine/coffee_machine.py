class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.state = 'waiting'

    def current_state(self):
        print('\nThe coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.coffee_beans, 'of coffee beans')
        print(self.disposable_cups, 'of disposable cups')
        print(f'${self.money} of money')
        print()

    def buy(self, coffee_type):
        if self.disposable_cups == 0:
            print('Sorry, not enough disposable cups!')
        else:
            if coffee_type == '1':
                if (self.water - 250) < 0:
                    print('Sorry, not enough water!')
                elif (self.coffee_beans - 16) < 0:
                    print('Sorry, not enough coffee beans!')
                else:
                    print('I have enough resources, making you a coffee!')
                    self.water -= 250
                    self.coffee_beans -= 16
                    self.money += 4
                    self.disposable_cups -= 1
            elif coffee_type == '2':
                if (self.water - 350) < 0:
                    print('Sorry, not enough water!')
                elif (self.milk - 75) < 0:
                    print('Sorry, not enough milk!')
                elif (self.coffee_beans - 20) < 0:
                    print('Sorry, not enough coffee beans!')
                else:
                    print('I have enough resources, making you a coffee!')
                    self.water -= 350
                    self.milk -= 75
                    self.coffee_beans -= 20
                    self.money += 7
                    self.disposable_cups -= 1
            elif coffee_type == '3':
                if (self.water - 200) < 0:
                    print('Sorry, not enough water!')
                elif (self.milk - 100) < 0:
                    print('Sorry, not enough milk!')
                elif (self.coffee_beans - 12) < 0:
                    print('Sorry, not enough coffee beans!')
                else:
                    print('I have enough resources, making you a coffee!')
                    self.water -= 200
                    self.milk -= 100
                    self.coffee_beans -= 12
                    self.money += 6
                    self.disposable_cups -= 1

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def work(self, command):
        if self.state == 'waiting':  # state in main menu
            if command == 'remaining':
                self.current_state()
                print('\nWrite action (buy, fill, take, remaining, exit):')
            elif command == 'buy':
                self.state = 'buying'
            elif command == 'fill':
                self.state = 'filling'
            elif command == 'take':
                self.take()
                print('\nWrite action (buy, fill, take, remaining, exit):')
            else:
                print('Unknown command')
        if self.state == 'buying':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            self.state = 'choosing coffee'
        elif self.state == 'choosing coffee':
            if command == 'back':
                self.state = 'waiting'
                print('\nWrite action (buy, fill, take, remaining, exit):')
            else:
                self.buy(command)
                self.state = 'waiting'
                print('\nWrite action (buy, fill, take, remaining, exit):')
        elif self.state == 'filling':
            print('Write how many ml of water do you want to add:')
            self.state = 'adding water'
        elif self.state == 'adding water':
            self.water += int(command)
            print('Write how many ml of milk do you want to add:')
            self.state = 'adding milk'
        elif self.state == 'adding milk':
            self.milk += int(command)
            print('Write how many grams of coffee beans do you want to add:')
            self.state = 'adding beans'
        elif self.state == 'adding beans':
            self.coffee_beans += int(command)
            print('Write how many disposable cups of coffee do you want to add:')
            self.state = 'adding cups'
        elif self.state == 'adding cups':
            self.disposable_cups += int(command)
            self.state = 'waiting'
            print('\nWrite action (buy, fill, take, remaining, exit):')


coffee_machine = CoffeeMachine()
print('Write action (buy, fill, take, remaining, exit):')
action = input()
while action != 'exit':
    coffee_machine.work(action)
    action = input()
