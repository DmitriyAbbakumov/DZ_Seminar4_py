# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def simple(a):
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        return True
    else:
        return False

N = int(input("введите число: "))
prime_factors = list()
i = 2
while N != 1:
    if N % i == 0 and simple(i) == True:
        N /= i
        prime_factors.append(i)
    else:
        i += 1
print(*prime_factors, sep="*")



# n = int(input("Введите число N: "))
# i = 2 
# list = []

# while i <= n:
#     if n % i == 0:
#         list.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители введенного числа указаны в списке: {list}")





