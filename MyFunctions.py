
import math

def factorialList():
    count = 0
    inputs = []
    while True:
        user_in = input("Enter an integer number or E or e to exit:")
        if user_in == "e" or user_in == "E":
            break
        else:
            try:
                num = int(user_in)
            except ValueError:
                print("wrong input, please enter an integer")
                inputs.append(user_in)
                count += 1
                if count == 5:
                    break
            else:
                count = 0
                print("Factorial: {0}".format(math.factorial(num)))
                inputs.append(num)
    inp_occ = [(x,inputs.count(x)) for x in set(inputs)]
    print("Inputs: {0}, Occurrences: {1}".format([x[0] for x in inp_occ],
        [x[1] for x in inp_occ]))

def CalLetterGrade(points: float, gradescale: list = [98, 94, 91, 88, 85, 82, 79, 76, 73, 70, 67, 64]):
    grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-']
    if len(gradescale) > 12 or not (isinstance(points, float) or isinstance(points, int)) or not isinstance(gradescale, list) or all(isinstance(n, int) for n in gradescale) != True:
        return -1

    for i in range(len(gradescale)):
        if points >= gradescale[i]:
            return grades[i]
    return 'F'
