
class SimpleChatBot:
    def __init__(self):
        self.name: str = "PythoBot"
        self.creation_date: int = 2021

    def greet(self):
        print(f'Hello! My name is {self.name}.\nI was created in {self.creation_date}.')

    @staticmethod
    def get_username():
        username: str = input('Please, remind me your name.\n')
        print(f'What a great name you have, {username}!')

    @staticmethod
    def guess_user_age():
        print('Let me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.')
        try:
            reminder_by_3, reminder_by_5, reminder_by_7 = int(input()), int(input()), int(input())
            age: int = (reminder_by_3 * 70 + reminder_by_5 * 21 + reminder_by_7 * 15) % 105
            print(f"Your age is {age}; that's a good time to start programming!")
        except ValueError:
            print("ONLY integers allowed. Try again")
            return SimpleChatBot.guess_user_age()

    @staticmethod
    def count_to_number():
        try:
            num: int = int(input('Now I will prove to you that I can count to any number you want.\n'))
            for n in range(num + 1):
                print(n, '!')
        except ValueError:
            print("ONLY integers allowed. Try again")
            return SimpleChatBot.count_to_number()

    @staticmethod
    def test_user_knowledge():
        print("""Let's test your programming knowledge.
    Why do we use methods?
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.""")

        while True:
            answer: str = input()
            if answer != "1":
                print('Please, try again.')
            else:
                print('Completed, have a nice day!')
                break


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
