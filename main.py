import itertools
import sys


def print_state(state):
    """Display quantity of supplies """
    print('\nThe coffee machine has:')
    for key, value in state.items():
        print(f'{value} of {key}')
    print()


def get_action():
    actions = ('buy', 'fill', 'take', 'remaining', 'exit')
    while True:
        try:
            action = input(f'Write action ({", ".join(actions)}):\n').lower()
            if action in actions:
                return action
            else:
                raise ValueError
        except ValueError:
            print('Unknown action!')


def buy_coffee(state):
    cup_of_espresso = {'water': 250, 'coffee beans': 16, 'money': -4, 'disposable cups': 1}
    cup_of_latte = {'water': 350, 'milk': 75, 'coffee beans': 20, 'money': -7, 'disposable cups': 1}
    cup_of_cappuccino = {'water': 200, 'milk': 100, 'coffee beans': 12, 'money': -6, 'disposable cups': 1}

    coffees = {'1': cup_of_espresso,
               '2': cup_of_latte,
               '3': cup_of_cappuccino}

    while True:
        choice = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
        if choice in ('1', '2', '3'):
            break
        else:
            print('Wrong choice!')
    try:
        for key in coffees[choice]:
            if state[key] - coffees[choice][key] < 0:
                print(f'Sorry, not enough {key}!\n')
                raise ValueError
        for key in coffees[choice]:
            state[key] -= coffees[choice][key]
        print('I have enough resources, making you a coffee!\n')
    except ValueError:
        pass
    return state


def machine_fill(machine_state):
    units = {'water': 'ml', 'milk': 'ml', 'coffee beans': 'grams'}
    # Used itertools islice method to iterate over first four elements of dict
    print()
    for key in dict(itertools.islice(machine_state.items(), 4)):
        if key != 'disposable cups':
            print(f'Write how many {units[key]} of {key} you want to add:')
        else:
            print('Write how many disposable coffee cups you want to add:')
        machine_state[key] += int(input())
    print()
    return machine_state


def main():
    machine_state = {'water': 400, 'milk': 540, 'coffee beans': 120, 'disposable cups': 9, 'money': 550}

    while True:
        action = get_action()
        if action == 'buy':
            machine_state = buy_coffee(machine_state)
        elif action == 'fill':
            machine_state = machine_fill(machine_state)
        elif action == 'take':
            print(f"\nI gave you ${machine_state['money']}\n")
            machine_state['money'] = 0
        elif action == 'remaining':
            print_state(machine_state)
        elif action == 'exit':
            sys.exit()


if __name__ == '__main__':
    main()
