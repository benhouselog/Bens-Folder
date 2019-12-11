class card:
    def __init__(self,soft_rank,hard_rank, suit): 
        self.__soft_rank = soft_rank
        self.__hard_rank = hard_rank
        self.__suit = suit

class AceCard(card):
    def __init__(self, suit):
        Card.__init__(self, 11, 1, suit)
        self.__face = 'A'

class FaceCard(Card):
    def __init__(self, suit, face):
        Card.__init__(self, 10, 10, suit)
        self.__face = face
        
    get_suit(self): str
    get_rank(self): int
    __str__(self):str

