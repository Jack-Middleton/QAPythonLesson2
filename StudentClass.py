#creating a class for students

class Student:
    def __init__(self, name, age, grade="", class_="student"):
        self.name = name
        self.age = age
        self.class_ = class_
        self.grade = grade
        
    def __repr__(self):
        return f"{self.name} is {self.age} years old and is a {self.class_}, "
    
    
    
    
    def gradeCalc(self):
        homeworkCheck = True
        assessmentCheck = True
        finalCheck = True

        while homeworkCheck:
            try:
                homeworkScore = int(input("Enter your homework score /25: "))
            except:
                print("Please enter a valid number between 0  and 25: ")
                continue
            if (25 >= homeworkScore >= 0):
                homeworkCheck = False
            else:
                print("please enter a number between 0 and 25")
                continue

        while assessmentCheck:
            try:
                assessmentScore = int(input("Enter your assessment score /50: "))
            except:
                print("Please enter a valid number between 0  and 50: ")
                continue
            if (50 >= assessmentScore >= 0):
                assessmentCheck = False
            else:
                print("please enter a number between 0 and 50")
                continue

        while finalCheck:
            try:
                finalScore = int(input("Enter your final score /100: "))
            except:
                print("Please enter a valid number between 0  and 100: ")
                continue
            if (100 >= finalScore >= 0):
                finalCheck = False
            else:
                print("please enter a number between 0 and 100")
                continue



        totalMark = round((finalScore + assessmentScore + homeworkScore) / 175 * 100, 1)
        return totalMark
        




studentName = str(input("Please enter your name: "))
studentAge = int(input("Please enter your age: "))        
student1 = Student(studentName, studentAge)
print(f"{student1}, with an average score of {student1.gradeCalc()}%")


  
        


