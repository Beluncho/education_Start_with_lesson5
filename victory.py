import random


def victory():
    name = input('Введите своё имя: ')
    print('Доброго времени суток,', name, ', это историческая викторина')
    print('Вам будет предложено вспомнить дату вступления во власть правителей ХХ века')
    print('Хотите поучавствовать в викторине? да/нет: ')

    answer0 = 'да'
    answer01 = input('Ведите ответ: ')
    print('Рады приветствовать вас в исторической викторине! Вводите дату в формате дд.мм.гггг ')

    while answer01 == 'да':
        answer1 = None
        answer2 = None
        answer3 = None
        answer4 = None
        answer5 = None
        answer6 = None
        answer7 = None
        answer8 = None
        answer9 = None
        answer10 = None
        head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        last_emperor = '01.11.1894'
        minister = '20.06.1917'
        first_star_ck = '09.11.1917'
        star_ck1 = '03.04.1922'
        star_ck2 = '07.09.1953'
        star_ck3 = '14.10.1964'
        star_ck4 = '12.11.1982'
        star_ck5 = '11.04.1984'
        eclipse_ck = '15.03.1985'
        first_president = '25.12.1991'
        ball = 0
        max_ball = 5
        print('Начать викторину/начать заново: да/нет ?')

        answer01 = input('Ведите ответ: ')

        if answer01 == answer0:
            answers = random.sample(head, 5)

            for i in range(len(answers)):
                if answers[i] == 1:
                    answer1 = input('Укажите год начала правления Николая II А.Р: ')  # answer 01.11.1894
                    ball += 1 if answer1 == last_emperor else print('Правильный ответ: первое ноября 1894 года')
                    # if answer1 == last_emperor:
                    #     ball += 1
                    # else:
                    #     ball += 0
                    #     print('Правильный ответ: первое ноября 1894 года')
                if answers[i] == 2:
                    answer2 = input('Укажите год начала правления Керенского А.Ф: ')  # answer 20.06.1917

                    if answer2 == minister:
                        ball += 1
                    else:
                        ball += 0
                        print('Правильный ответ: двадцатого июня 1917 года')
                if answers[i] == 3:
                    answer3 = input('Укажите год начала правления Ленина В.И: ')  # 09.11.1917

                    if answer3 == first_star_ck:
                        ball += 1
                    else:
                        ball += 0
                        print('Правильный ответ: девятого ноября 1917 года')
                if answers[i] == 4:
                    answer4 = input('Укажите год начала правления Сталина И.В: ')  # answer 03.04.1922

                    if answer4 == star_ck1:
                        ball += 1
                    else:
                        ball += 0
                        print('Правильный ответ: третьего апреля 1922 года')
                if answers[i] == 5:
                    answer5 = input('Укажите год начала правления Хрущева Н.С: ')  # answer 07.09.1953

                    if answer5 == star_ck2:
                        ball += 1
                    else:
                        ball += 0
                        print('Правильный ответ: седьмого сентября 1953 года ')
                if answers[i] == 6:
                    answer6 = input('Укажите год начала правления Брежнева Л.И: ')  # answer 14.10.1964

                    if answer6 == star_ck3:
                        ball += 1
                    else:
                        ball += 0
                        print('Правильный ответ: четырнадцатого октября 1964 года')
                if answers[i] == 7:
                    answer7 = input('Укажите год начала правления Андропова Ю.В: ')  # answer 12.11.1982

                    if answer7 == star_ck4:
                        ball += 1
                    else:
                        ball += 0
                        print('Правильный ответ: двенадцатого ноября 1982 года')
                if answers[i] == 8:
                    answer8 = input('Укажите год начала правления Черненко К.У: ')  # answer 11.04.1984

                    if answer8 == star_ck5:
                        ball += 1
                    else:
                        ball += 0
                        print('Правильный ответ: одинадцатого апреля 1984 года')
                if answers[i] == 9:
                    answer9 = input('Укажите год начала правления Горбачева М.С: ')  # answer 15.03.1985

                    if answer9 == eclipse_ck:
                        ball += 1
                    else:
                        ball += 0
                        print('Правильный ответ: пятнадцатого марта 1985 года')
                if answers[i] == 10:
                    answer10 = input('Укажите год начала правления Ельцина Б.Н: ')  # answer 25.12.1991

                    if answer10 == first_president:
                        ball += 1
                    else:
                        ball += 0
                        print('Правильный ответ: двадцатьпятого декабря 1991 года')
        right_ball_perc = ball * 100 / max_ball
        left_ball_perc = 100 - right_ball_perc
        mistake = max_ball - ball
        print('-' * 100)
        print(name)
        print('Итого правельных ответов: ', ball)
        print('Итого не правельных ответов: ', mistake)
        print('Процент правильных ответов: ', right_ball_perc, '%')
        print('Процент не правильных ответов: ', left_ball_perc, '%')
    else:
        print('end')
    return

