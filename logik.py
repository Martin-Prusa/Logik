from random import randint


class Logik:
    def __init__(self, player, colors_count, positions_count, secret=None, debug=False):
        self.player = player
        self.colors_count = colors_count
        self.positions_count = positions_count
        self.secret = self.generate_secret() if secret is None else secret
        if debug:
            print(self.secret)
        self.history = []
        self.win = False

    def generate_secret(self):
        return [randint(1, self.colors_count) for _ in range(self.positions_count)]
    
    def check_combination(self, combination):
        if self.win:
            return
        
        correct_positions = sum(s == g for s, g in zip(self.secret, combination))
        correct_colors = sum(min(self.secret.count(color), combination.count(color)) for color in set(self.secret)) - correct_positions

        return correct_positions, correct_colors

    def next_turn(self):
        combination = self.player.get_next_combination(history=self.history)
        
        assert combination is not None, "Není nastavena kombinace"
        assert len(combination) == len(self.secret), "Chybný počet pozic"
        assert not self.win, "Hra skončila"

        result = self.check_combination(combination)
        self.history.append((combination, result))
        self.win = result[0] == self.positions_count