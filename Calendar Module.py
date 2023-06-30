# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar as cal

date = list(map(int, input().split()))
print(str(cal.day_name[cal.weekday(date[2], date[0], date[1])]).upper())
