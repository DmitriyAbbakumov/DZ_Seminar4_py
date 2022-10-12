# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
# for i in range (-10, 0): print(10**i,round(math.pi, -i),sep=' ->')
i = int(input("Введите кол-во знаков после зяпятой от 1 до 10: "))
while i < 1 or i > 10:
    i = int(input("Введите кол-во знаков после зяпятой от 1 до 10: "))
else:
    print(10**-i, round(math.pi, i), sep=' ->')





# qnt = int(input("Input the number of decimal places: "))

# pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095

# pi_for_user = round(pi, qnt+1)

# for i in range(qnt):
#     pi_for_user *= 10

# pi_for_user = math.trunc(pi_for_user)

# while pi_for_user > 10:
#     pi_for_user /= 10

# print(round(pi_for_user, qnt))

