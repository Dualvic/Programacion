from clases import *

class Conjured(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def update_quality(self):
            if self.sell_in >= 0:
                self.setQuality(-2)
            else:
                self.setQuality(-4)
            self.setSell_in()
