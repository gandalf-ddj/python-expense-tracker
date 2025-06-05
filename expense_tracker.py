def new():
    item = input('\nWhat did you purchase?')
    price = input('\nHow much did you pay for the item?')
    with open('expenses.txt', 'a') as file:
        file.write(item + ',' + price + '\n')
        print('\nExpense saved to file!')

def view():
    total = 0.0
    with open('expenses.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            item, price = line.strip().split(',')
            total += float(price)
    print(f'\n Total spent: ${total:.2f}')

keep_going = True
while keep_going:
    user_choice = input('\nWhat would you like to do?\n1 - Add a new expense\n2 - View total expenses\n3 - Exit\n')
    if user_choice == '1':
        new()
    elif user_choice == '2':
        view()
    elif user_choice == '3':
        print('Goodbye!')
        keep_going = False
    else:
        print('Invalid input, try again.')