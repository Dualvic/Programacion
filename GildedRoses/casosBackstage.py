from clases import *
from backstage import *

if __name__ == '__main__':

    item = backstage("Backstage passes to a TAFKAL80ETC concert",15,20)

    for day in range(1,20):
        item.update_quality()
        print(item)
