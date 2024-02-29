# Viết chương trình Python tính trung bình cộng của cả danh sách, trung bình cộng các phần tử
# dương trong danh sách.

list = [9, -1, 1, 4, -4, 1, -7, 2, -99, -43, 9, 2, 3, 4, 10, 10, 9, 8, 10, 5, 6, 7, -1, 9, -3, 99, -9, 832, -5, 9, 8, 3, 3, 1, 0]

# N = 0

# N = int(input('Nhập số lượng phần tử trong danh sách \n'))

# for i in range(N):
#     Num = int(input('Nhập phần tử thứ {0}'))
#     list.append(Num)
print(list)
print('\n')
Sum = sum(list)
print('trung binh cong la ' + str(Sum/len(list)))
