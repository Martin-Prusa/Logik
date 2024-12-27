class Player:
    def __init__(self):
        self.next_combination = None

    def get_next_combination(self):
        assert self.next_combination is not None, "Není nastaveno další číslo"
        nn = self.next_combination
        self.next_combination = None
        return nn
    
    def set_next_number(self, next_combination):
        self.next_combination = next_combination