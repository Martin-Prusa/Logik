from random import randint


class Logik:
    """
        Třída reprezentující logiku hry Mastermind.
    """

    def __init__(self, player, colors_count, positions_count, secret=None, debug=False):
        """
            Inicializace hry.
            Parametry:
                player: instance třídy Player (třída s metodou get_next_combination)
                colors_count: počet barev
                positions_count: počet pozic
                secret: tajná kombinace (None=generuje se náhodně)
                debug: výpis tajné kombince (False=nevypisuje se, True=vypisuje se)
        """
        self.player = player
        self.colors_count = colors_count
        self.positions_count = positions_count
        self.secret = self.generate_secret() if secret is None else secret
        if debug:
            print(self.secret)

        # Historie tahů, kde každý tah obsahuje kombinaci a její zhodnocení.
        self.history = []

        # Hra skončila
        self.win = False

    def generate_secret(self):
        """
            Generuje náhodnou tajnou kombinaci. Podle počtu barev a pozic.
        """
        return [randint(1, self.colors_count) for _ in range(self.positions_count)]
    
    def check_combination(self, combination):
        """
            Zhodnotí zadanou kombinaci.
            Parametry:
                combination: zadaná kombinace pro zhodnocení (int[])
            Return:
                tuple: (počet správně umístěných barev, počet správných barev na špatném místě)
        """
        if self.win:
            return
        
        correct_positions = sum(s == g for s, g in zip(self.secret, combination))
        correct_colors = sum(min(self.secret.count(color), combination.count(color)) for color in set(self.secret)) - correct_positions

        return correct_positions, correct_colors

    def next_turn(self):
        """
            Provede další tah hry. Získá kombinaci od hráče, zhodnotí ji a uloží do historie.
        """
        combination = self.player.get_next_combination(history=self.history)
        
        assert combination is not None, "Není nastavena kombinace"
        assert len(combination) == len(self.secret), "Chybný počet pozic"
        assert not self.win, "Hra skončila"

        result = self.check_combination(combination)
        self.history.append((combination, result))
        self.win = result[0] == self.positions_count