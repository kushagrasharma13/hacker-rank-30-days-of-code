class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
            max_=0
            for i in range(len(self.__elements)):
                    for j in range(i+1,len(self.__elements)):
                            temp=(self.__elements[i]-self.__elements[j])
                            if temp<0:
                                    temp=-(temp)
                            if temp>max_:
                                    max_=temp
            self.maximumDifference=max_
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
