class Player:
    """
        Třída reprezentující hráče hry Mastermind.
    """

    def __init__(self):
        self.next_combination = None

    def get_next_combination(self, history):
        """
            Vrátí kombinaci pro další tah. Nastavenou kombinaci vrátí jen jednou.
            Parametry:
                history - historie tahů (není potřeba pro tento typ hráče)
            Return:
                Kombinace pro další tah. (int[])
        """
        assert self.next_combination is not None, "Není nastaveno další číslo"
        nn = self.next_combination
        self.next_combination = None
        return nn
    
    def set_next_combination(self, next_combination):
        """
            Nastaví kombinaci pro další tah.
            Parametry:
                next_combination - Kombinace pro další tah. (int[])
        """
        self.next_combination = next_combination