# https://www.hackerrank.com/challenges/finding-the-percentage
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print(format(round(sum(student_marks[query_name])/3,2), '.2f'))
