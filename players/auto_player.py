import random
from itertools import permutations

class AutoPlayer:
    def __init__(self, positions_count, colors_count):
        self.positions_count = positions_count
        self.colors_count = colors_count
        self.sorted_combination = [1] * positions_count
        self.change_index = 0
        self.permutations = None

    def get_correct_sorted_combination(self, history):
        if self.permutations is None:
            self.permutations = permutations(self.sorted_combination)
        
        for permutation in self.permutations:
            valid = True
            for h in history:
                sequence, correct_positions = h[0], h[1][0]

                correct_positions_count = sum(1 for i in range(len(sequence)) if i < len(permutation) and sequence[i] == permutation[i])

                if correct_positions_count != correct_positions:
                    valid = False
                    break
            
            if valid:
                return permutation
        return None
               

    def get_next_combination(self, history):
        if len(history) == 0:
            return self.sorted_combination.copy()
        
        self.change_index = history[-1][1][0] + history[-1][1][1]

        if self.change_index == self.positions_count:
            return self.get_correct_sorted_combination(history)

        for i in range(self.change_index, self.positions_count):
            self.sorted_combination[i] += 1

        if self.sorted_combination[-1] == self.colors_count:
            return self.get_correct_sorted_combination(history)
        
        comb = self.sorted_combination.copy()
        random.shuffle(comb)
        return comb