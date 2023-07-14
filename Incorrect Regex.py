# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/usr/bin/python3

import re

test = 'test_string'
T = int(input())
for t in range(T):
    pattern = input()
    try:
        result = re.match(pattern, test)
        print ("True")
    except Exception:
        print ("False")
