# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import re
ffile1 = open('output1.txt', 'r')
ffile2 = open('output2.txt', 'r')
ffile3 = open('file3.txt', 'w')
file1 = ffile1.readline()
file2 = ffile2.readline()


print(file1)
file3=list()
for i in range(len(file1)):
    if file1[i]=='^':
        file3.append(file1[i+1])
# print(file3)

file4=list(map(int, re.findall('\d+', file1)))
file5=list()
for i in range(len(file4)):
    if not i%2:
        file5.append(file4[i])
file5[-1] = file4[-2]
# print(file4)
# print(file5)


print(file2)
file3_1=list()
for i in range(len(file2)):
    if file2[i]=='^':
        file3_1.append(file2[i+1])
# print(file3_1)

file4_1=list(map(int, re.findall('\d+', file2)))
file5_1=list()
for i in range(len(file4_1)):
    if not i%2:
        file5_1.append(file4_1[i])
file5_1[-1] = file4_1[-2]
# print(file4_1)
# print(file5_1)   

file6=list()
if len(file5)<len(file5_1):
    file6=file5
    while len(file5)!=len(file5_1):
        file6.insert(0,0)
    file_result = file5_1+file6
else:
    file6=file5_1
    while len(file5)!=len(file5_1):
        file6.insert(0,0)
    file_result = file5+file6
# print(file6)
# print(file_result)

file_sum=list()
for i in range(int(len(file_result)/2)):
    file_sum.append(file_result[i]+file_result[int(len(file_result)/2)+i])
print(file_sum)

k=len(file_sum)-1
result=list()
while k>=0:
    if k==1:
        result.append(f'{file_sum[len(file_sum)-2]}*x')
    elif k==0:
        result.append(file_sum[len(file_sum)-1])
    else:
        result.append(f'{file_sum[len(file_sum)-k-1]}*x^{k}')
    result.append('+')
    k-=1
result.pop(-1)
result.append('=0')
print(result)
    
a=''.join(str(x) for x in result)
ffile3.write(''.join(str(x) for x in a))
ffile3.close()
ffile2.close()
ffile1.close()
























