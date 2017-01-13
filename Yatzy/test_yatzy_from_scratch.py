import pytest
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)

def test_yatzy():
    assert 50 == Yatzy.yatzy(5,5,5,5,5)
    assert 0 ==  Yatzy.yatzy(5,5,5,5,4)
    assert 0 ==  Yatzy.yatzy(5,1,1,5,1)
    assert 50 == Yatzy.yatzy(2,2,2,2,2)

def test_ones():
    assert 0 == Yatzy.ones(5,5,5,5,5)
    assert 0 ==  Yatzy.ones(5,5,5,5,4)
    assert 3 ==  Yatzy.ones(5,1,1,5,1)
    assert 5 == Yatzy.ones(1,1,1,1,1)

def test_twos():
    assert 0 == Yatzy.twos(5,5,5,5,5)
    assert 0 ==  Yatzy.twos(5,5,5,5,4)
    assert 6 ==  Yatzy.twos(5,2,2,5,2)
    assert 10 == Yatzy.twos(2,2,2,2,2)

def test_threes():
    assert 0 == Yatzy.threes(5,5,5,5,5)
    assert 0 ==  Yatzy.threes(5,5,5,5,4)
    assert 9 ==  Yatzy.threes(5,3,3,5,3)
    assert 15 == Yatzy.threes(3,3,3,3,3)

@pytest.fixture
def inyector():
    # Es el setup de unittest o de JUnit
    tirada = Yatzy(1, 2, 3, 4, 5)
    return tirada

def test_fours(inyector):
    valor_esperado = 4
    assert valor_esperado ==inyector.fours()


def test_fives(inyector):
    valor_esperado = 5
    assert valor_esperado == inyector.fives()


def test_sixes(inyector):
    valor_esperado = 0
    assert valor_esperado == inyector.sixes()


def test_score_pair():
    assert 10 == Yatzy.pair(5,5,5,5,5)
    assert 10 ==  Yatzy.pair(5,5,5,5,4)
    assert 12 ==  Yatzy.pair(5,6,6,5,6)
    assert 6 == Yatzy.pair(3,3,3,3,3)
    assert 12 == Yatzy.pair(2,2,6,6,5)
    assert 0 == Yatzy.pair(1,2,3,6,5)


def test_two_pair():
    assert 20 == Yatzy.two_pair(5,5,5,5,5)
    assert 20 ==  Yatzy.two_pair(5,5,5,5,4)
    assert 22 ==  Yatzy.two_pair(5,6,6,5,6)
    assert 12 == Yatzy.two_pair(3,3,3,3,3)
    assert 16 == Yatzy.two_pair(2,2,6,6,5)
    assert 0 == Yatzy.two_pair(1,2,3,6,5)


def test_three_of_a_kind():
    assert 15 == Yatzy.three_of_a_kind(5,5,5,5,5)
    assert 15 ==  Yatzy.three_of_a_kind(5,5,5,5,4)
    assert 18 ==  Yatzy.three_of_a_kind(5,6,6,5,6)
    assert 9 == Yatzy.three_of_a_kind(3,3,3,3,3)
    assert 0 == Yatzy.three_of_a_kind(2,2,6,6,5)
    assert 0 == Yatzy.three_of_a_kind(1,2,3,6,5)


def test_four_of_a_kind():
    assert 20 == Yatzy.four_of_a_kind(5,5,5,5,5)
    assert 20 ==  Yatzy.four_of_a_kind(5,5,5,5,4)
    assert 0 ==  Yatzy.four_of_a_kind(5,6,6,5,6)
    assert 12 == Yatzy.four_of_a_kind(3,3,3,3,3)
    assert 0 == Yatzy.four_of_a_kind(2,2,6,6,5)
    assert 0 == Yatzy.four_of_a_kind(1,2,3,6,5)


def test_small_straight():
    assert 0 == Yatzy.smallStraight(5,5,5,5,5)
    assert 0 ==  Yatzy.smallStraight(5,5,5,5,4)
    assert 0 ==  Yatzy.smallStraight(5,6,6,5,6)
    assert 0 == Yatzy.smallStraight(3,3,3,3,3)
    assert 15 == Yatzy.smallStraight(4,2,3,1,5)
    assert 15 == Yatzy.smallStraight(1,2,3,4,5)


def test_large_straight():
    assert 0 == Yatzy.largeStraight(5,5,5,5,5)
    assert 0 ==  Yatzy.largeStraight(5,5,5,5,4)
    assert 0 ==  Yatzy.largeStraight(5,6,6,5,6)
    assert 0 == Yatzy.largeStraight(3,3,3,3,3)
    assert 15 == Yatzy.largeStraight(4,2,3,6,5)
    assert 15 == Yatzy.largeStraight(2,3,4,5,6)

def test_full_house():
    assert 0 == Yatzy.fullHouse(5,5,5,5,5)
    assert 0 ==  Yatzy.fullHouse(5,5,5,5,4)
    assert 28 ==  Yatzy.fullHouse(5,6,6,5,6)
    assert 0 == Yatzy.fullHouse(3,3,3,3,3)
    assert 24 == Yatzy.fullHouse(4,4,4,6,6)
    assert 12 == Yatzy.fullHouse(2,2,2,3,3)
    assert 0 == Yatzy.fullHouse(2,3,4,2,3)
