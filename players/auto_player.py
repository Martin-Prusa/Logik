import random

class AutoPlayer:
    def __init__(self, positions_count, colors_count):
        self.positions_count = positions_count
        self.colors_count = colors_count
        self.sorted_combination = [1] * positions_count
        self.change_index = 0

    def get_correct_sorted_combination(self, history):
       l = self.sorted_combination.copy()
       random.shuffle(l)
       return l

    def get_next_combination(self, history):
        if len(history) == 0:
            return self.sorted_combination.copy()
        
        self.change_index = history[-1][1][0] + history[-1][1][1]

        for i in range(self.change_index, self.positions_count):
            self.sorted_combination[i] += 1
        
        return self.get_correct_sorted_combination(history)