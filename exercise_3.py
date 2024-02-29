# Viết chương trình Python tìm vị trí của phần tử dương cuối cùng trong danh sách

List = [9, -1, 1, 4, -4, 1, -7, 2, -99, -43, 9, 2, 3, 4, 10, 10, 9, 8, 10, 5, 6, 7, -1, 9, -3, 99, -9, 832, -5, 9, 8, 3, 3, 1, 0]

vitri = 0

for i in range(len(List)):
    if List[i] > 0:
        vitri = i
print('Vi tri phan tu duong cuoi cung la ',vitri)