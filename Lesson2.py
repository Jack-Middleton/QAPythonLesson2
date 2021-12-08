'''The program should take the students name,
homework score (/25),
assessment score (/50) and 
final exam score (/100) as inputs, and output their name and final ICT grade as a percentage.'''
def gradeCalc():
    homeworkCheck = True
    assessmentCheck = True
    finalCheck = True

    studentName = str(input("Enter your name: "))

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


    def totalGrade(finalScore, homeworkScore, assessmentScore):
        totalMark = round((finalScore + assessmentScore + homeworkScore) / 175 * 100, 1)
        return totalMark


    totalMark = totalGrade(finalScore, homeworkScore, assessmentScore)


    if totalMark > 90:
        grade = "A"
    elif totalMark > 75:
        grade = "B"
    elif totalMark > 50:
        grade = "C"
    else:
        grade = "Fail"


    print(f"{studentName} your total mark is {totalMark}, giving you a final grade of {grade}")