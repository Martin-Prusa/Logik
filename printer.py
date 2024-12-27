class ConsolePrinter:
    def print(self, message):
        print(message)

    def print_line(self):
        print('-'*50)

    def print_highlighted(self, message):
        print(f"\033[1m{message}\033[0m")