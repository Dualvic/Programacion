'''
---------------------------------------------
| Quien: El jugador                         |
| El que: Hacer la jugada                   |
| Para que: Conseguir una puntuacion        |
---------------------------------------------
'''

class Yatzy:

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5

    @staticmethod
    def chance(*dice):
        total_points = 0
        for die in dice:
            total_points += die
        return total_points

    @staticmethod
    def yatzy(*dice):
        yatzy_value = 50
        if dice.count(dice[0]) == len(dice):
            return yatzy_value
        return 0

    @staticmethod
    def ones(*dice):
        total_points = 0
        for die in dice:
            if die == 1:
                total_points += die
        return total_points


    @staticmethod
    def twos(*dice):
        total_points = 0
        for die in dice:
            if die == 2:
                total_points += die
        return total_points

    '''
    ONE = 1
    return dice.count(ONE) * ONE
    '''

    @staticmethod
    def threes(*dice):
        total_points = 0
        for die in dice:
            if die == 3:
                total_points += die
        return total_points


    def fours(self):
        total_points = 0
        for die in self.dice:
            if die == 4:
                total_points += die
        return total_points


    def fives(self):
        total_points = 0
        for die in self.dice:
            if die == 5:
                total_points += die
        return total_points



    def sixes(self):
        total_points = 0
        for die in self.dice:
            if die == 6:
                total_points += die
        return total_points


    @staticmethod
    def pair(*dice):
        PAIR = 2
        for number in reversed(range(1,7)):
            if dice.count(number) >= PAIR:
                return number * PAIR
        return 0

    @staticmethod
    def two_pair(*dice):
        pairs=0
        PAIR = 2
        total_points=0
        for number in range(1,7):
            if dice.count(number) >= PAIR:
                total_points += number * PAIR
                pairs+=1
            if dice.count(number) >= 2*PAIR:
                total_points += number * PAIR
                pairs+=1
            if pairs == 2:
                return total_points
        return 0


    @staticmethod
    def three_of_a_kind(*dice):

        for face in range(1,7):
            if dice.count(face) >= 3:
                return face * 3
        return 0


    @staticmethod
    def four_of_a_kind(*dice):
        for face in range(1,7):
            if dice.count(face) >= 4:
                return face * 4
        return 0


    @staticmethod
    def smallStraight(*dice):
        for number in range(1,6):
            if dice.count(number) != 1:
                return 0
        return 15


    @staticmethod
    def largeStraight(*dice):
        for number in range(2,7):
            if dice.count(number) != 1:
                return 0
        return 15


    @staticmethod
    def fullHouse(*dice):
        PAIR = 0
        THIRDS = 0
        score = 0
        for number in range(1,7):
            if dice.count(number) == 3:
                score = score+ (number * 3)
                PAIR +=1
            elif dice.count(number) == 2:
                score = score + (number*2)
                PAIR +=1
            if numero2 == 1 and numero3 == 1:
                return score
        return 0
