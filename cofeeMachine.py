resources = {
    'Water': {
        'value': 700,
        'unit': 'ml'
    },
    'Milk': {
        'value': 600,
        'unit': 'ml'
    },
    'Coffee': {
        'value': 300,
        'unit': 'g'
    },
    'Money': {
        'value': 0,
        'unit': '$'
    },
}
coffee_requirements = {
    'expresso': {
        'Money': 250,
        'Water': 100,
        'Milk': 100,
        'Coffee': 50,
    },
    'latte': {
        'Money': 300,
        'Water': 100,
        'Milk': 200,
        'Coffee': 50,
    },
    'cappuccino': {
        'Money': 350,
        'Water': 50,
        'Milk': 100,
        'Coffee': 100,
    },
}

money_var = {
    100: 0,
    50: 0,
    20: 0,
    5: 0,
    1: 0
}


def report(resources_dict):
    for key in resources_dict:
        if key == 'Money':
            print(f"{key} : {resources_dict[key]['unit']}{resources_dict[key]['value']}")
        else:
            print(f"{key} : {resources_dict[key]['value']}{resources_dict[key]['unit']}")


def take_money(my_money_var):
    total = 0
    for key in my_money_var:
        val = int(input(f"Insert {key}Rs: "))
        total += (val * key)
    return total


def is_sufficient_resources(coffee, cups):
    my_resources = resources.copy()
    for key in my_resources:
        if key == 'Money':
            continue
        if my_resources[key]['value'] >= (coffee_requirements[coffee][key] * cups):
            my_resources[key]['value'] -= (coffee_requirements[coffee][key] * cups)
        else:
            return False

    resources.update(my_resources)
    return True


while True:
    choice = input("What would you like? (expresso,latte or cappuccino): ")
    if choice == 'report':
        report(resources)
    elif choice == 'expresso' or choice == 'latte' or choice == 'cappuccino':
        no_of_cups = int(input("How many cups would you like to have? : "))
        total_money = take_money(money_var)
        required_money = no_of_cups * coffee_requirements[choice]['Money']
        if total_money < required_money:
            print("Entered money is not sufficient")
        elif not is_sufficient_resources(choice, no_of_cups):
            print("Insufficient resources")
        else:
            print(f"Enjoy your {choice} . and your take your change {total_money - required_money}")
            resources['Money']['value'] += required_money
    elif choice == 'off':
        print("Machine turns off")
        break
    else:
        print("You entered wrong choice")
