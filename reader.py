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

    def read_number_with_default_value(self, default, min_value=None, max_value=None):
        while True:
            user_input = input()
            if user_input == '':
                return default
            try:
                number = int(user_input)
                if min_value is not None and number < min_value or max_value is not None and number > max_value:
                    self.printer.print(f"Hodnota není v platném rozsahu ({min_value if min_value is not None else '-infinity'})-({max_value if max_value is not None else 'infinity'}).")
                    continue
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
                is_valid_combination = True
                secret = [int(color) for color in secret]
                for color in secret:
                    if not 1 <= color <= colors_count:
                         self.printer.print(f"Barvy musí být v rozmezí 1-{colors_count}.")
                         is_valid_combination = False
                         break
                if is_valid_combination:
                    return secret
            except ValueError:
                self.printer.print("Neplatný vstup. Zadejte čísla oddělená mezerou.")
                continue