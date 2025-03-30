import random

class Game():
    def __init__(self):
        self.secret_num = None
        self.MAX_TRY = 10
        self.list_random = []
        self.TRY_USER = 0

    def Secret_list_num(self):
        self.secret_num = random.randint(100, 999)
        return self.secret_num

    def main(self):
        print('Игра в которой нужно угадать число по подсказкам \n'
              'у тебя есть 10 попыток на отгадку числа')
        a = input("Желаешь начать? - (y/n) - ")

        if a.lower() == 'y':
            print('Начинаем!')
            self.secret_num = self.Secret_list_num()
            # print(self.secret_num)
            calc = 0
            for calc in range(1, self.MAX_TRY + 1):
                self.TRY_USER += 1
                print("Попытка номер - ", calc, "\n")
                answer = input('Введите число - ')
                if len(answer) != 3 or not answer.isdigit():
                    print('Пожалуйста, используйте трех значные числа')
                    continue
                else:
                    # print(self.secret_num)
                    if answer == str(self.secret_num):
                        print("Вы угадали число!")
                        break
                    else:
                        for i in str(answer):
                            count = set(answer).intersection(set(str(self.secret_num)))
                    print("Количество совпадений совпадение", len(count))
                if self.TRY_USER == 10:
                    print("Попытки закончились число было - ", self.secret_num)
                if a.lower() == 'n':
                    print("Игра закончилась, спасибо!")



if __name__ == '__main__':
        game_instance = Game()
        game_instance.main()







