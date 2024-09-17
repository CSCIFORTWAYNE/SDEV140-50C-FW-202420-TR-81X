"""Author: Angela Venable
   Student data program with lots of functions.
"""

def main():
    data = readClassData()
    names = 0
    studentIds = 1
    emails = 2
    programs = 3
    gpas = 4

    data.extend(readProgramGPA(data[studentIds]))
    for num in range(0, len(data[studentIds])):
        print(f"{data[studentIds][num]:s} - {data[names][num]:s} {data[gpas][num]:.2f}")


def readClassData():
    names = []
    studentIds = []
    emails = []
    with open('classroster.txt','r') as f:
        f.readline()
        for line in f:
            words = line.split()
            names.append(words[0] + ' ' + words[1] + ' ' +words[2])
            studentIds.append(words[3])
            emails.append(words[4])
        # print(names)
        # print(studentIds)
        # print(emails)
        return [names, studentIds, emails]
    #f = open("classroster.txt",'r')

def readProgramGPA(studentIds):
    programs = []
    gpas = []
    for student in studentIds:
        programs.append("")
        gpas.append(0.0)
    f = open('studentlist.txt', 'r')
    for line in f:
        data = line.split()
        i = findStudentById(studentIds= studentIds, id= data[0])
        if i != -1:
            programs[i] = getProgram(data[1])
            gpas[i] = float(data[2])
    return [programs, gpas]

def findStudentById(id, studentIds):
    for num in range(0, len(studentIds)):
        if studentIds[num] == id:
            return num
    return -1

def getProgram(programCode):
    programs = {"C":"CSCI", "S":"SDEV", "D":"DBMS", "I":"INFM"}
    return programs[programCode]


if __name__ == "__main__":
    main()

