class FindMaxMin:
    def __init__(self,list):
        self.list = list     
        self.xPos = []
        self.yPos = []
        self.zPos = []
        self.maxPos= []
        self.minPos= []
        self.a =0
        self.b =800
        
        #print("test")/
    def maxPosition(self): 
        #print(len(self.list))
        #print(float(self.list[0][0]))
        for x in range(len(self.list)):
            self.xPos.append(float(self.list[x][0]))
            self.yPos.append(float(self.list[x][1]))
            self.zPos.append(float(self.list[x][2]))
        self.maxPos.append([max(self.xPos),max(self.yPos),max(self.zPos)])
        self.minPos.append([min(self.xPos),min(self.yPos),min(self.zPos)])
    def maprange(self,s):
        (a1, a2), (b1, b2) = (-52.27,11.96),(0, 800)
        return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
    
    #for s in range(1):
        # print("%g maps to %g" % (s, maprange((-52.27,11.96), (0, 255), s)))
        # print("%g maps to %g" % (-52.27, maprange( (-52.27,11.96), (0, 800), -52.27)))
        # print("%g maps to %g" % (11.96, maprange( (-52.27,11.96), (0, 800), 11.96)))
        
