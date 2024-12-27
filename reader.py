class ConsoleReader:
    def __init__(self, printer):
        self.printer = printer
    
    def read_number(self):
        while True:
            user_input = input()
            try:
                number = int(user_input)
                return number
            except ValueError:
                self.printer.print("Neplatný vstup, prosím zadejte číslo.")

    def read_number_with_default_value(self, default):
        while True:
            user_input = input()
            if user_input == '':
                return default
            try:
                number = int(user_input)
                return number
            except ValueError:
                self.printer.print("Neplatný vstup, zadejte číslo.")

    def read_combination(self, positions_count, colors_count):
        while True:
            user_input = input()
            secret = user_input.split()
            if len(secret) != positions_count:
                self.printer.print(f"Zadejte přesně {positions_count} pozic.")
                continue
            try:
                secret = [int(color) for color in secret]
                for color in secret:
                    if not 1 <= color <= colors_count:
                         self.printer.print(f"Barvy musí být v rozmezí 1-{colors_count}.")
                         continue
                return secret
            except ValueError:
                self.printer.print("Neplatný vstup. Zadejte čísla oddělená mezerou.")
                continue