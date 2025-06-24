import random

def guess_number_game():
    secret_number = random.randint(1, 10)
    attempts = 0
    
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 105. Попробуй угадать!")
    print('eto zixlo ',secret_number)
    
    while True:
        try:
            guess = int(input("Введите ваше предположение: "))
            attempts += 1
            if guess < secret_number:
                print("Слишком маленькое! Попробуй еще раз.")
            elif guess > secret_number:
                print("Слишком большое! Попробуй еще раз.")
            elif guess == secret_number:
                print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
                break
            elif attempts > 6:
                print('vi proigrali')
        except ValueError:
            print("Пожалуйста, вводите только целые числа!")
            
guess_number_game()