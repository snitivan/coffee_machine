"""coffee_volume = int(input('Write how many cups of coffee you will need: > '))
water = coffee_volume * 200
milk = coffee_volume * 50
coffee = coffee_volume * 15

print(f'For {coffee_volume} cups of coffee you will need:')
print(f'{water} ml of water')
print(f'{milk} ml of milk')
print(f'{coffee} g of coffee beans')"""
'''one_cup = [200, 50, 15]
water_has = int(input('Write how many ml of water the coffee machine has: > '))
milk_has = int(input('Write how many ml of milk the coffee machine has: > '))
coffee_has = int(input('Write how many grams of coffee beans the coffee machine has: > '))
coffee_volume = int(input('Write how many cups of coffee you will need: > '))

water_v = f'Write how many ml of water the coffee machine has: \n> {water_has}'
milk_v =  f'Write how many ml of milk the coffee machine has: \n> {milk_has}'
coffee_v = f'Write how many grams of coffee beans the coffee machine has: \n> {coffee_has}'
print(water_v)
print(milk_v)
print(coffee_v)
all_cup = list(map(lambda x: x * coffee_volume, one_cup))  # volume of resources
need_sources = [water_has, milk_has, coffee_has]
can_make_cups = []
for i in range(len(all_cup)):
    v = need_sources[i] // one_cup[i]
    can_make_cups.append(v)
over_cup = min(can_make_cups) - coffee_volume
if all_cup[0] <= water_has and all_cup[1] <= milk_has and all_cup[2] <= coffee_has\
        and coffee_volume >= min(can_make_cups):
    print('Yes, I can make that amount of coffee')
elif all_cup[0] >= water_has or all_cup[1] >= milk_has or all_cup[2] >= coffee_has:
    print(f'No, I can make only {min(can_make_cups)} cups of coffee')
else:
    print(f'Yes, I can make that amount of coffee(and even {over_cup} more than that)')'''
# func_coffee
"""water_has = 400
milk_has = 540
coffee_has = 120
cups_has = 9
money_in_bank = 550


def what_has():
    print(f'\nThe coffee machine has:\n{water_has} of water\n{milk_has} of milk\n{coffee_has} of coffee beans\n'
          f'{cups_has} of disposable cups\n{money_in_bank} of money')


def buy_coffee():
    coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
    global water_has, milk_has, coffee_has, cups_has, money_in_bank
    espresso_cup = [250, 16]
    latte_cup = [350, 75, 20]
    cappuccino = [200, 100, 12]
    has_sources = [water_has, milk_has, coffee_has]
    can_make_cups = []
    if coffee == str(1):
        all_cup = espresso_cup
        can_make_cups.append(has_sources[0] // all_cup[0])
        can_make_cups.append(has_sources[2] // all_cup[1])
        if all_cup[0] <= water_has and all_cup[1] <= coffee_has:
            water_has -= 250
            coffee_has -= 16
            cups_has -= 1
            money_in_bank += 4
            print('I have enough resources, making you a coffee!')
        elif all_cup[0] >= water_has:
            print('Sorry, not enough water!')
        elif all_cup[1] >= coffee_has:
            print('Sorry, not enough coffee beans!')
    elif coffee == str(2):
        all_cup = latte_cup
        can_make_cups.append(has_sources[0] // all_cup[0])
        can_make_cups.append(has_sources[1] // all_cup[1])
        can_make_cups.append(has_sources[2] // all_cup[2])
        if all_cup[0] <= water_has and all_cup[1] <= milk_has and all_cup[2] <= coffee_has:
            water_has -= 350
            milk_has -= 75
            coffee_has -= 20
            cups_has -= 1
            money_in_bank += 7
            print('I have enough resources, making you a coffee!')
        elif all_cup[0] >= water_has:
            print('Sorry, not enough water!')
        elif all_cup[1] >= milk_has:
            print('Sorry, not enough milk!')
        elif all_cup[2] >= coffee_has:
            print('Sorry, not enough coffee beans!')
    elif coffee == str(3):
        all_cup = cappuccino
        can_make_cups.append(has_sources[0] // all_cup[0])
        can_make_cups.append(has_sources[1] // all_cup[1])
        can_make_cups.append(has_sources[2] // all_cup[2])
        if all_cup[0] <= water_has and all_cup[1] <= milk_has and all_cup[2] <= coffee_has:
            water_has -= 200
            milk_has -= 100
            coffee_has -= 12
            cups_has -= 1
            money_in_bank += 6
            print('I have enough resources, making you a coffee!')
        elif all_cup[0] >= water_has:
            print('Sorry, not enough water!')
        elif all_cup[1] >= milk_has:
            print('Sorry, not enough milk!')
        elif all_cup[2] >= coffee_has:
            print('Sorry, not enough coffee beans!')
    elif coffee == 'back':
        pass
    else:
        print('Please write a number from 1-3')


def fill_action():
    water = int(input('Write how many ml of water do you want to add: '))
    milk = int(input('Write how many ml of milk do you want to add: '))
    coffee = int(input('Write how many grams of coffee beans do you want to add: '))
    cups = int(input('Write how many disposable cups of coffee do you want to add: '))
    global water_has, milk_has, coffee_has, cups_has
    water_has += water
    milk_has += milk
    coffee_has += coffee
    cups_has += cups


def take_money():
    global money_in_bank
    print(f'I gave you ${money_in_bank}')
    money_in_bank = 0


while True:
    action = input('\nWrite action (buy, fill, take, remaining, exit):\n> ')

    if action == 'buy':
        buy_coffee()
    elif action == 'fill':
        fill_action()
    elif action == 'take':
        take_money()
    elif action == 'remaining':
        what_has()
    elif action == 'exit':
        break
"""


class CoffeeMachine():
    def __init__(self, water_has, milk_has, coffee_has, cups_has, money_in_bank):
        self.water_has = water_has
        self.milk_has = milk_has
        self.coffee_has = coffee_has
        self.cups_has = cups_has
        self.money_in_bank = money_in_bank

    def buy_coffee(self, cof):
        espresso_cup = [250, 16]
        latte_cup = [350, 75, 20]
        cappuccino = [200, 100, 12]
        has_sources = [self.water_has, self.milk_has, self.coffee_has]
        can_make_cups = []
        if cof == str(1):
            all_cup = espresso_cup
            can_make_cups.append(has_sources[0] // all_cup[0])
            can_make_cups.append(has_sources[2] // all_cup[1])
            if all_cup[0] <= self.water_has and all_cup[1] <= self.coffee_has:
                self.water_has -= 250
                self.coffee_has -= 16
                self.cups_has -= 1
                self.money_in_bank += 4
                print('I have enough resources, making you a coffee!')
            elif all_cup[0] >= self.water_has:
                print('Sorry, not enough water!')
            elif all_cup[1] >= self.coffee_has:
                print('Sorry, not enough coffee beans!')
        elif cof == str(2):
            all_cup = latte_cup
            can_make_cups.append(has_sources[0] // all_cup[0])
            can_make_cups.append(has_sources[1] // all_cup[1])
            can_make_cups.append(has_sources[2] // all_cup[2])
            if all_cup[0] <= self.water_has and all_cup[1] <= self.milk_has and all_cup[2] <= self.coffee_has:
                self.water_has -= 350
                self.milk_has -= 75
                self.coffee_has -= 20
                self.cups_has -= 1
                self.money_in_bank += 7
                print('I have enough resources, making you a coffee!')
            elif all_cup[0] >= self.water_has:
                print('Sorry, not enough water!')
            elif all_cup[1] >= self.milk_has:
                print('Sorry, not enough milk!')
            elif all_cup[2] >= self.coffee_has:
                print('Sorry, not enough coffee beans!')
        elif cof == str(3):
            all_cup = cappuccino
            can_make_cups.append(has_sources[0] // all_cup[0])
            can_make_cups.append(has_sources[1] // all_cup[1])
            can_make_cups.append(has_sources[2] // all_cup[2])
            if all_cup[0] <= self.water_has and all_cup[1] <= self.milk_has and all_cup[2] <= self.coffee_has:
                self.water_has -= 200
                self.milk_has -= 100
                self.coffee_has -= 12
                self.cups_has -= 1
                self.money_in_bank += 6
                print('I have enough resources, making you a coffee!')
            elif all_cup[0] >= self.water_has:
                print('Sorry, not enough water!')
            elif all_cup[1] >= self.milk_has:
                print('Sorry, not enough milk!')
            elif all_cup[2] >= self.coffee_has:
                print('Sorry, not enough coffee beans!')
        elif cof == 'back':
            pass
        else:
            print('Please write a number from 1-3')

    def fill_action(self, w, m, c, cup):
        self.water_has += w
        self.milk_has += m
        self.coffee_has += c
        self.cups_has += cup

    def take_money(self):
        print(f'I gave you ${self.money_in_bank}')
        self.money_in_bank = 0

    def what_has(self):
        print(f'\nThe coffee machine has:\n{self.water_has} of water\n{self.milk_has} of milk\n'
              f'{self.coffee_has} of coffee beans\n'
              f'{self.cups_has} of disposable cups\n{self.money_in_bank} of money')


machine_has = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    action = input('\nWrite action (buy, fill, take, remaining, exit):\n> ')
    if action == 'buy':
        coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n>')
        machine_has.buy_coffee(coffee)
    elif action == 'fill':
        water = int(input('Write how many ml of water do you want to add: '))
        milk = int(input('Write how many ml of milk do you want to add: '))
        coffee = int(input('Write how many grams of coffee beans do you want to add: '))
        cups = int(input('Write how many disposable cups of coffee do you want to add: '))
        machine_has.fill_action(water, milk, coffee, cups)
    elif action == 'take':
        machine_has.take_money()
    elif action == 'remaining':
        machine_has.what_has()
    elif action == 'exit':
        break

