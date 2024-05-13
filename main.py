def writeGrades():
    try:
        done = False
        dict = {}
        course = input("Enter course name: ")
        grade = input("Enter grade: ")
        dict[course] = int(grade)

        while not done:
            course = input("Enter course name: ")
            grade = input("Enter grade (\"done\" to finish): ")
            if grade == "done": break
            dict[course] = int(grade)

        return dict
    except Exception as e:
        print(e)
        exit()

def grades():
    try:
        write = input("Want to add grades? (y/n): ")
        if write == "y": pass
        else: exit()
        grades = writeGrades()

        term = input("Enter term number and year with no spaces: ")
        file = open(term, "w")
        sum = 0
        for key, value in grades.items():
            file.write(key + ": " + str(value) + "\n")
            sum += value
        average = sum/len(grades.items())
        file.write("Average is: " + str(average))
        file.close()


    except Exception as e:
        print(e)

grades()