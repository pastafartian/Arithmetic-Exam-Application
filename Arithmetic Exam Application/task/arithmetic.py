import random


def equation_creator():
    n1 = str(random.randint(2, 9))
    n2 = str(random.randint(2, 9))
    operator = str(operator_randomizer())
    return n1 + ' ' + operator + ' ' + n2


def square_generator():
    return random.randint(11, 29)


def operator_randomizer():
    r = random.randint(1, 3)
    if r == 1:
        return '+'
    elif r == 2:
        return '-'
    else:
        return '*'


def user_guess(calculation):
    while True:
        guess = input()
        # lowercase_guess = guess.lower()
        # alpha = lowercase_guess.islower()
        if guess != '':
            try:
                int(guess)
                break
            except ValueError:
                print('Incorrect format.')
        else:
            print('Incorrect format.')
    if int(guess) == calculation:
        print('Right!')
        return 0
    else:
        print('Wrong!')
        return 1


correct_answers = 0

test_type = int(input('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29'''))

if test_type == 1:
    for _ in range(5):
        problem = equation_creator()
        print(problem)
        answer = eval(problem)

        correctness = user_guess(answer)
        if correctness == 0:
            correct_answers += 1
elif test_type == 2:
    for _ in range(5):
        square = square_generator()
        answer = pow(square, 2)

        print(square)
        correctness = user_guess(answer)
        if correctness == 0:
            correct_answers += 1

print(f'Your mark is {correct_answers}/5')

save = str.lower(input('Would you like to save your result to the file? Enter yes or no.'))

if save == 'yes' or save == 'y':
    result_file = open('results.txt', 'a')
    username = input('What is your name?')

    if test_type == 1:
        descriptor = '1 (simple operations with numbers 2-9)'
    else:
        descriptor = '2 (integral squares 11-29)'
    result_file.write(f'{username}: {correct_answers}/5 in level {descriptor}.')
    print('The results are saved in "results.txt".')

    result_file.close()
else:
    exit()
