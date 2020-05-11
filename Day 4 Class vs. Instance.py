class Person:
    def __init__(self,initialAge):
        if initialAge<0:
            print('Age is not valid, setting age to 0.')
            self.nage=0
        else:
            self.nage=initialAge
    def amIOld(self):
        if self.nage<13:
            print('You are young.')
        elif self.nage>=13 and self.nage<18:
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
        self.nage+=1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
