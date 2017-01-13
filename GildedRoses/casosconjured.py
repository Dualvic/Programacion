
from clases import *
from conjured import *

if __name__ == '__main__':

    item = Conjured("Conjured Mana Cake", 3, 6)
    # chequeo herencia __repr__
    for day in range(1,10):
        item.update_quality()
        print(item)
    # test update_quality
