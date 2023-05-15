class Mapping:
    def __init__(self):
        self.list = list
        self.xPos = []
        self.yPos = []
        self.zPos = []
        self.maxPos= []
        self.minPos= []
        self.a = (-52.27,11.96)
        self.b =(0, 800)

    def maprange(self,a,s):
        (a1, a2), (b1, b2) = a,(0, 800)
        return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

    #for s in range(1):
        # print("%g maps to %g" % (s, maprange((-52.27,11.96), (0, 255), s)))
        # print("%g maps to %g" % (-52.27, maprange( (-52.27,11.96), (0, 800), -52.27)))
        # print("%g maps to %g" % (11.96, maprange( (-52.27,11.96), (0, 800), 11.96)))
