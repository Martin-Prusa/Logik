import random
from itertools import permutations

class AutoPlayer:
    """
        Třída reprezentující automatického hádajícího hráče hry Mastermind.
    """

    def __init__(self, positions_count, colors_count):
        """
            Inicializuje nového automatického hráče.
            Parametry:
                positions_count - počet pozic v hádané kombinaci
                colors_count - počet možných barev
        """
        # Počet pozic v hádané kombinaci
        self.positions_count = positions_count

        # Počet možných barev
        self.colors_count = colors_count

        # Pomocný seznam barev, seřazenný od nejmenšího čísla po největší. Slouží pro pamatování si správných barev v hádané kombinaci.
        self.sorted_combination = [1] * positions_count

        # Index v sorted_combination, od kterého nejsou barvy správné. Od tohoto indexu se budou měnit barvy v dalším kole.
        self.change_index = 0

        # Seznam všech možných permutací sorted_combination
        self.permutations = None

    def get_correct_sorted_combination(self, history):
        """
            Vrátí permutaci sorted_combination, která splňuje všechny podmínky z předchozích tahů.
            Parametry:
                history - seznam předchozích tahů ve tvaru [(kombinace, (správné pozice, správné barvy))]
        """
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
        """
            Vrátí další hádanou kombinaci. 
            Pokud je historie prázdná, začíná kombinací, kde jsou samé jedničky.
            Dokud nezná všechny barvy v kombinaci, postupně zvyšuje číslo barvy na pozicích od change_index do konce. Výsledná kombinace je náhodně zamíchaná. To se hodí při vyhodnocování správných pozic.
            Change_index je vlastně počet již známých barev
            Když už zná všechny barvy, vrátí permutaci sorted_combination, která splňuje všechny podmínky z předchozích tahů.
            Parametry:
                history - seznam předchozích tahů ve tvaru [(kombinace, (správné pozice, správné barvy))]
            Return:
                kombinace - nová hádaná kombinace (int[])
        """
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