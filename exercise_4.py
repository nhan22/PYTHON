# Viết chương trình Python tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối
# cùng

List = [9, -1, 1, 4, -4, 1, -7, 2, -99, -43, 9, 2, 3, 4, 10, 10, 9, 8, 10, 5, 6, 7, -1, 9, -3, 99, -9, 832, -5, 9, 8, 3, 3, 1, 0]

vitri_Max = 0
Max = 0
for i in range(len(List)) :
    if List[i] > Max :
        Max = List[i]
        vitri_Max = i

print('Phan tu lon nhat la ', max(List))
print('Vi tri phan tu lon nhat cuoi cung la', vitri_Max)