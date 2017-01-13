from clases import *
from sulfuras import *

class Sulfuras(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def update_quality(self):
            self.setQuality(80)
            self.setSell_in(0)
