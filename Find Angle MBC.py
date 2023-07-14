# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = int(input())
BC = int(input())
theta = round(math.degrees(math.atan(AB / BC)))
print(theta, chr(176), sep = '')
