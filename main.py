from random import *

repeat_or_not = 'y'
while repeat_or_not == 'y':
    print(
        '', 'Добро пожаловать в числовую угадайку!', '',
        'Оптимальный диапазон для игры от 1 до 100, но Вы можете увеличить его.',
        'Введите целое положительное число n, где n граница диапазона от 1 до n.', sep='\n'
    )


    def is_valid(boundary_num):
        """
        Проверяет правильность введённых пользователем данных
        в range_boundary.
        """
        range_numbers = [str(i) for i in range(0, 10)]
        return len([j for j in boundary_num if range_numbers.count(j)]) == len(boundary_num) if True else False


    range_boundary = 0
    completion_of_verification = 1
    while completion_of_verification == 1:
        range_boundary = input()
        if is_valid(range_boundary) and int(range_boundary) > 1:
            range_boundary = int(range_boundary)
            completion_of_verification = 0
        else:
            print('Не верное значение границы диапазона!',
                  'Введите целое положительное число n, где n граница диапазона от 1 до n.', sep='\n'
                  )

    random_num = randint(1, range_boundary)
    print(random_num)


    def is_valid_2(user_num_valid):
        """
        Проверяет правильность введённых пользователем данных
        в user_num.
        """
        range_numbers = [str(i) for i in range(0, 10)]
        return len([j for j in user_num if range_numbers.count(j)]) == len(user_num_valid) if True else False


    counter = 7
    counter_2 = 0
    print(f'Введите предполагаемое число от 1 до {range_boundary} (у Вас 7 попыток!):')

    while counter > 0:
        user_num = input()
        counter_2 += 1
        if is_valid_2(user_num) and counter > 0 and int(user_num) <= range_boundary:
            user_num = int(user_num)
            if user_num > random_num:
                counter -= 1
                if counter > 0:
                    print('Введённое Вами число больше загаданного.',
                          f'Введите предполагаемое число от 1 до '
                          f'{range_boundary} (у Вас {counter} попытка(ок)!):', sep='\n'
                          )
            elif user_num < random_num:
                counter -= 1
                if counter > 0:
                    print('Введённое Вами число меньше загаданного.',
                          f'Введите предполагаемое число от 1 до '
                          f'{range_boundary} (у Вас {counter} попыкта(ок)!):', sep='\n'
                          )
            elif user_num == random_num:
                counter = 0
        else:
            print(f'А может быть все-таки введём целое число от 1 до {range_boundary}?',
                  f'(у Вас {counter} попыток!):'
                  )
        if counter == 0 and user_num == random_num:
            print(f'Победа! Вы угадали загаданное число с {counter_2} попытки(ок)!', '',
                  'Спасибо, что играли в числовую угадайку. Сыграем ещё раз?',
                  'Введите y/n для новой игры или выхода из программы соответственно', sep='\n'
                  )
        elif counter == 0 and user_num != random_num:
            print('К сожалению, Вы не угадали загаданное число. Сыграем ещё раз?',
                  'Введите y/n для новой игры или выхода из программы соответственно:', sep='\n'
                  )


    def is_valid_3(user_correct_text):
        """
        Проверяет правильность введённых пользователем данных
        в repeat_or_not.
        """
        correct_text = ['y', 'n']
        return correct_text.count(user_correct_text) if True else False


    completion_of_verification = 1
    while completion_of_verification == 1:
        repeat_or_not = input()
        if is_valid_3(repeat_or_not):
            completion_of_verification = 0
        else:
            print('Введено не верное значение! Попробуйте ещё раз!',
                  'Введите y/n для новой игры или выхода из программы соответственно:', sep='\n'
                  )
