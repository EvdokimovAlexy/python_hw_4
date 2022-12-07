# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

def creat_lst():
    a = [int(input('Введите значние\nnum= ')) for i in range(int(input('Введите количество символов\nlen = ')))]
    return a
num = creat_lst()
print(num)
new_num = []
for i in range(len(num)):
    if num[i] != num[i-1]:
        new_num.append(num[i])
print(new_num)