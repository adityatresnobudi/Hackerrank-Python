# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath as cm

user_input = input()
polar = user_input.split("j")
polar.remove("")
if "-" in polar[0][0]:
    if "+" in polar[0]:
        r_theta = polar[0].split("+")
    else:
        r_theta = polar[0].split("-")
        r_theta.remove("")
        r_theta[0] = -1 * int(r_theta[0])
        r_theta[1] = -1 * int(r_theta[1])
else:
    if "-" in polar[0]:
        r_theta = polar[0].split("-")
        r_theta[1] = -1 * int(r_theta[1])
    else:
        r_theta = polar[0].split("+")
        
print(abs(complex(int(r_theta[0]), int(r_theta[1]))))
print(cm.phase(complex(int(r_theta[0]), int(r_theta[1]))))
