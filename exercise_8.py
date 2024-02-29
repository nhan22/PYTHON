#  Viết chương trình Python tính số lượng các phần tử liên tiếp đan dấu nhiều nhất (dãy phần tử liên tiếp được gọi là đan dấu nếu tích hai phần tử liên tiếp âm)

List = [9, -1, 1, 4, -4, 1, -7, 2, -99, -43, 9, 2, 3, 4, 10, 10, 9, 3, 2, 3, 8, 10, 5, 6, 7, -1, 9, -3, 99, 99, -9, 832, -5, 9, 8, 3, 3, 1, 0]

Dem = 0
MaxDem = 0

for i in range(len(List) - 1):
    if List[i] * List[i + 1] < 0:
        Dem += 1
    else:
        MaxDem = max(MaxDem, Dem) 
        Dem = 0 
print('Day phan tu dan dau nhieu nhat ', MaxDem)
