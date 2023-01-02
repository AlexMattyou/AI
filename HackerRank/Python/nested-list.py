# https://www.hackerrank.com/challenges/nested-list
students_grade = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_grade += [[name,score]]
    s = sorted(list(set([students_grade[i][1] for i in range(0,len(students_grade))])))
    low = [[students_grade[i][0]] for i in range(0,len(students_grade)) if students_grade[i][1] == s[1]]
    low = sorted(low)
    [print(y[0]) for y in low]
