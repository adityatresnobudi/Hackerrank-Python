# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input().strip())
Student = namedtuple("Student", ",".join(input().strip().split()))

student_list = list(Student(*input().strip().split()) for _ in range(N))
print(format(sum([int(i.MARKS) for i in student_list]) / N, ".2f"))
