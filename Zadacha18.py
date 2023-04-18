'''Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка содержит число X'''

N = abs(int(input('Введите количество элементов списка А: ')))
b = input("Введите через пробел элементы списка: ").split()
c = list(map(int, b))
if len(c) != N or N == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = abs(X - c[0])
    index = 0
    for i in range(1, N):
        count = abs(X - c[i])
        if count < min:
            min = count
            index = i
    print(f'Число {c[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - c[index])}')


