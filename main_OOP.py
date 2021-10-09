import sys


class CoffeeMachine:
    CUP_OF_ESPRESSO = {'water': 250, 'coffee beans': 16, 'money': -4, 'disposable cups': 1}
    CUP_OF_LATTE = {'water': 350, 'milk': 75, 'coffee beans': 20, 'money': -7, 'disposable cups': 1}
    CUP_OF_CAPPUCCINO = {'water': 200, 'milk': 100, 'coffee beans': 12, 'money': -6, 'disposable cups': 1}
    COFFEES = {'1': CUP_OF_ESPRESSO,
               '2': CUP_OF_LATTE,
               '3': CUP_OF_CAPPUCCINO}
    UNITS = {'water': 'ml', 'milk': 'ml', 'coffee beans': 'grams'}

    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.resources = {'water': water,
                          'milk': milk,
                          'coffee beans': coffee_beans,
                          'disposable cups': disposable_cups,
                          'money': money}

        self.power_on = True
        self.actions = ('buy', 'fill', 'take', 'remaining', 'exit')
        self.state = None
        self.message = None
        self.set_state('menu')

    def set_state(self, val):
        self.state = val
        if val == 'menu':
            self.message = f'Write action ({", ".join(self.actions)}):\n'
        elif val == 'buy':
            self.message = '\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n'
        elif val in ('fill water', 'fill milk', 'fill coffee beans', 'fill cups'):
            if val != 'fill cups':
                self.message = f'Write how many {self.UNITS[val[5:]]} of {val[5:]} you want to add:\n'
            else:
                self.message = 'Write how many disposable coffee cups you want to add:\n'

    def interface(self, user_input):
        if self.state == 'menu':
            if user_input == 'buy':
                self.set_state('buy')
            elif user_input == 'fill':
                print()
                self.set_state('fill water')
            elif user_input == 'take':
                print(f'\nI gave you ${self.resources["money"]}\n')
                self.resources['money'] = 0
            elif user_input == 'remaining':
                self.print_state()
            elif user_input == 'exit':
                sys.exit()
        elif self.state == 'buy':
            if user_input == 'back':
                self.set_state('menu')
            elif user_input in ('1', '2', '3'):
                self.make_coffee(user_input)
                self.set_state('menu')

        elif self.state == 'fill water':
            self.resources['water'] += int(user_input)
            self.set_state('fill milk')
        elif self.state == 'fill milk':
            self.resources['milk'] += int(user_input)
            self.set_state('fill coffee beans')
        elif self.state == 'fill coffee beans':
            self.resources['coffee beans'] += int(user_input)
            self.set_state('fill cups')
        elif self.state == 'fill cups':
            self.resources['disposable cups'] += int(user_input)
            self.set_state('menu')
            print()

    def print_state(self):
        print('\nThe coffee machine has:')
        for key, value in self.resources.items():
            print(f'{value} of {key}')
        print()

    def make_coffee(self, val):
        try:
            for key in self.COFFEES[val]:
                if self.resources[key] - self.COFFEES[val][key] < 0:
                    print(f'Sorry, not enough {key}!\n')
                    raise ValueError
            for key in self.COFFEES[val]:
                self.resources[key] -= self.COFFEES[val][key]
            print('I have enough resources, making you a coffee!\n')
        except ValueError:
            pass


if __name__ == '__main__':
    cm = CoffeeMachine(400, 540, 120, 9, 550)
    while cm.power_on:
        cm.interface(input(cm.message))
