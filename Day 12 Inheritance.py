class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName,lastName,idNumber,scores):
        Person.__init__(self,firstName,lastName,idNumber)
        self.scores=scores

    def calculate(self):
        sum_=0
        for i in self.scores:
            sum_+=i
        check=sum_//len(self.scores)
        if check in range(90,101):
            return "O"
        elif check in range(80,91):
            return "E"
        elif check in range(70,81):
            return "A" 
        elif check in range(55,71):
            return "P"
        elif check in range(40,56):
            return "D"
        elif check in range(0,41):
            return "T"
        
        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
