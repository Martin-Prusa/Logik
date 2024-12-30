class ConsolePrinter:
    """
        Třída pro výpis informací
    """

    def print(self, message):
        """
            Vytiskne text
            Parametry:
                message - string
        """
        print(message)

    def print_line(self):
        """
            Vytiskne čáru
        """
        print('-'*50)

    def print_highlighted(self, message):
        """
            Vytiskne text tučně
            Parametry:
                message - string
        """
        print(f"\033[1m{message}\033[0m")

    def print_game(self, game):
        """
            Vytsikne průběh hry (historii hádaných kombinací)
            Parametry:
                game - list of tuples
                        - tuple (list of int, tuple of int)
                            - list of int - hádaná kombinace
                            - tuple of int - počet správných pozic a správných barev
        """
        for round_number, guess in enumerate(game):
            print(f"{round_number:2}: ", end='')
            for color in guess[0]:
                print(f"{color: 2}", end=' ')
            print(f" | P{guess[1][0]: 2} B{guess[1][1]: 2}")