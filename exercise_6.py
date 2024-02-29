# Viết chương trình Python tính số lượng các số dương liên tiếp nhiều nhất.

List = [9, -1, 1, 4, -4, 1, -7, 2, -99, -43, 9, 2, 3, 4, 10, 10, 9, 3, 2, 3, 8, 10, 5, 6, 7, -1, 9, -3, 99, 99, -9, 832, -5, 9, 8, 3, 3, 1, 0]

Dem = 0
Max = 0
for i in range(len(List)):
    Dem += 1
    if List[i] < 0:
        if Max < Dem:
            Max = Dem
        Dem = 0
print(Max)