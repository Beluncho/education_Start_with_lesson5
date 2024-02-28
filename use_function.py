import os
import pickle
import json

from decorator_example import add_sep



def balance_fun():
    balance = 0.0
    buy_story = []
    BALANCE_FILE_NAME = 'balance.data'
    BUY_FILE_NAME = 'buy_story.data'

    if os.path.exists(BALANCE_FILE_NAME):
        with open(BALANCE_FILE_NAME, 'r') as f:
            balance = json.load(f)
    if os.path.exists(BUY_FILE_NAME):
        with open(BUY_FILE_NAME, 'rb') as f:
            buy_story = pickle.load(f)

    @add_sep
    def refill(balance):
        ref = float(input('enter sum: '))
        balance += ref
        return balance
    pass


    @add_sep
    def yes_buy(balance):
        buy = float(input('enter buy sum:'))

        if buy > balance:
            print('not enough money!')
        else:
            balance -= buy
            name = input('name your buy: ')
            buy_story.append((name, buy))
        return balance
    pass

    while True:
        print('1. пополнение счета ')
        print('2. покупка ')
        print('3. история покупок ')
        print('4. выход ')
        print('Ваш баланс:', balance)
        choice = input('Выберите пункт меню')
        if choice == '1':
            try:
                balance = refill(balance)
            except ValueError:
                print("Введите цифры")
            pass
        elif choice == '2':
            try:
                balance = yes_buy(balance)
            except ValueError:
                print('error')
            pass
        elif choice == '3':
            print(buy_story)
            pass
        elif choice == '4':
            with open(BALANCE_FILE_NAME, 'w') as f:
                json.dump(balance, f)
                with open(BUY_FILE_NAME, 'wb') as f:
                    pickle.dump(buy_story, f)
            break
        else:
            print('Неверный пункт меню')
    return

