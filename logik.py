from random import randint


class Logik:
    def __init__(self, player, colors_count, positions_count, secret=None):
        self.player = player
        self.colors_count = colors_count
        self.positions_count = positions_count
        self.secret = self.generate_secret() if secret is None else secret

        self.history = []
        self.status = 1 # 1 - running, 2 - win, 3 - lose

    def generate_secret(self):
        return [randint(1, self.colors_count) for _ in range(self.positions_count)]
    
    def check_combination(self, combination):
        if self.status != 1:
            return
        
        assert combination == None or len(combination) != len(self.secret), "Chybný počet pozic"