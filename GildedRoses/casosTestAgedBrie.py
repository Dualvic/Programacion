from clases import *
from agedbrie import *

if __name__ == '__main__':

    item = agedBrie("Aged Brie",2,0)

    for day in range(1,20):
        item.update_quality()
        print(item)
