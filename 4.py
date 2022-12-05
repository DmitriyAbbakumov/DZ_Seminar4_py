# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


def mnogochlen():
    k=int(input("Введите степень: "))
    from random import randint
    result=list()
    while k >= 0:
        if k == 1:
            result.append(f'{randint(1,100)}*x')
        elif k == 0:
            result.append(randint(1, 100))
        else:
            result.append(f'{randint(1,100)}*x^{k}')
        result.append('+')
        k -= 1
    result.pop( - 1)
    result.append('=0')
    return result

a=''.join(str(x) for x in mnogochlen())
b=''.join(str(x) for x in mnogochlen())
def output_file(name, a):
    file_1 = open(name, 'w')
    file_1.write(''.join(str(x) for x in a))
    file_1.close()
output_file('output1.txt', a)
output_file('output2.txt', b)






# from random import randint

# k = int(input('Insert equation power: '))
# koefs = list()
# for i in range(1, k + 2):
#     koefs.append(randint(1, 100))

# ans = list()
# for i in range(len(koefs)):
#     if k == 1:
#         ans.append(f'{koefs[i]}*x')
#     elif k == 0:
#         ans.append(f'{koefs[i]}')
#     else:
#         ans.append(f'{koefs[i]}*x**{k}')
#     flag = randint(0, 1)
#     if flag == 1:
#         ans.append('+')
#     elif flag == 0:
#         ans.append('-')
#     k -= 1

# ans.pop(-1)
# ans.append('=0')
# fout = open('output.txt', 'w')
# fout.write(''.join(ans))
# fout.close()
