# Viết chương trình Python tìm phần tử lớn thứ nhì của danh sách và các vị trí của các phần tử
# đạt giá trị lớn nhì

List = [9, -1, 1, 4, -4, 1, -7, 2, -99, -43, 9, 2, 3, 4, 10, 10, 9, 8, 10, 5, 6, 7, -1, 9, -3, 99, 99, -9, 832, -5, 9, 8, 3, 3, 1, 0]
Phantu = Phantulonnhi = float('-inf')

for i in range(len(List)):
    if List[i] > Phantu:
        Phantulonnhi = Phantu
        Phantu = List[i]
    elif List[i] > Phantulonnhi and List[i] != Phantu:
        Phantulonnhi = List[i]
print('Phan tu lon nhi la ',Phantulonnhi)
print('vi tri cac phan tu lon nhi')
for i in range(len(List)):
    if List[i] == Phantulonnhi:
        print(i)
