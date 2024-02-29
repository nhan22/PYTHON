#  Viết chương trình Python xóa phần tử thứ k (k nhập từ bàn phím) trong danh sách.

List = [9, -1, 1, 4, -4, 1, -7, 2, -99, -43, 9, 2, 3, 4, 10, 10, 9, 3, 2, 3, 8, 10, 5, 6, 7, -1, 9, -3, 99, 99, -9, 832, -5, 9, 8, 3, 3, 1, 0]
print('Mảng trước khi chèn là : ', List)

deleted_K = int(input('Nhập số K cần xóa \n'))
if deleted_K >= 0 and deleted_K <= len(List):
    removed_item = List[deleted_K]
    del List[deleted_K]
    print("Phần tử ", removed_item, "đã được xóa khỏi danh sách.")
else:
    print("Vị trí không hợp lệ.")

List_end = List
print('Danh sách sau khi xóa số K là : ', List_end)