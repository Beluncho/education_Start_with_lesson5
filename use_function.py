def balance_fun():
    balance = 0.0
    buy_story = []
    def refill(balance):
        ref = float(input('enter sum: '))
        balance += ref
        return balance
    pass


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
            balance = refill(balance)
            pass
        elif choice == '2':
            balance = yes_buy(balance)
            pass
        elif choice == '3':
            print(buy_story)
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
    return
