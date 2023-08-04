
class SimpleChatBot:
    def __init__(self):
        self.name: str = "PythonBot"
        self.creation_date: int = 2021

    def greet(self):
        print(f'Hello! My name is {self.name}.\nI was created in {self.creation_date}.')

    @staticmethod
    def get_username():
        username: str = input('Please, remind me your name.\n')
        print(f'What a great name you have, {username}!')

    @staticmethod
    def guess_user_age():
        age = False
        while not age:
            print('Let me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.')
            try:
                age: int = (int(input()) * 70 + int(input()) * 21 + int(input()) * 15) % 105
                print(f"Your age is {age}; that's a good time to start programming!")
            except ValueError:
                print("ONLY integers allowed. Try again")

    @staticmethod
    def count_to_number():
        num = False
        while not num:
            try:
                num: int = int(input('Now I will prove to you that I can count to any number you want.\n'))
                for n in range(num + 1):
                    print(n, '!')
            except ValueError:
                print("ONLY integers allowed. Try again")

    @staticmethod
    def test_user_knowledge():
        print("""Let's test your programming knowledge.
    Why do we use methods?
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.""")

        while input() != "1":
            print('Please, try again.')
        print('Completed, have a nice day!')


def main():
    bot = SimpleChatBot()
    bot.greet()
    SimpleChatBot.get_username()
    SimpleChatBot.guess_user_age()
    SimpleChatBot.count_to_number()
    SimpleChatBot.test_user_knowledge()
    print('Congratulations, have a nice day!')


if __name__ == '__main__':
    main()
