class ConsolePrinter:
    def print(self, message):
        print(message)

    def print_line(self):
        print('-'*50)

    def print_highlighted(self, message):
        print(f"\033[1m{message}\033[0m")

    def print_game(self, game):
        for round_number, guess in enumerate(game):
            print(f"{round_number:2}: ", end='')
            for color in guess[0]:
                print(f"{color: 2}", end=' ')
            print(f" | {guess[1][0]: 2}, {guess[1][1]: 2}   (správné pozice, správné barvy)")