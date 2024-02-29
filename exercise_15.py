# Viết chương trình Python chèn danh sách [1,2,3] vào vị trí đầu, cuối và thứ 5 của danh sách

List = [9, -1, 1, 4, -4, 1, -7, 2, -99, -43, 9, 2, 3, 4, 10, 10, 9, 3, 2, 3, 8, 10, 5, 6, 7, -1, 9, -3, 99, 99, -9, 832, -5, 9, 8, 3, 3, 1, 0]
print('Mảng trước khi chèn là : ', List)
List_end = List
print('Các vị trí chèn lần lượt :')
print('1 - đâu mảng')
print('2 - vị trí bất kì trong mảng')
print('3 - Cuối mảng')

insert_Num = int(input('Nhập vị trí muốn chèn số \n'))
Num = [1,2,3]
if insert_Num == 1:
    List_end.insert(0, Num)
if insert_Num == 2:
    vitri = int(input('Nhập Vị trí muốn chèn \n'))
    List_end.insert(vitri, Num)
if insert_Num == 3:
    List_end.append(Num)
print('Mảng sau khi chèn là : ', List_end)