#  Viết chương trình Python tìm số phần tử là dương và là số nguyên tố của danh sách và vị trí
# của nó trong danh sách.

List = [9, -1, 1, 4, -4, 1, -7, 2, -99, -43, 9, 2, 3, 4, 10, 10, 9, 3, 2, 3, 8, 10, 5, 6, 7, -1, 9, -3, 99, 99, -9, 832, -5, 9, 8, 3, 3, 1, 0]

positive_primes = [] # Mảng chứa giá trị các số nguyên tố
positions = [] # Mảng chứa vị trí các số nguyên tố

def is_prime(x): # hàm tìm số nguyên tố
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

for i in range(len(List)):
    if List[i] > 0 and is_prime(List[i]):
        positive_primes.append(List[i])
        positions.append(i)
print("Số nguyên tố dương trong danh sách là:", positive_primes)
print("Vị trí của các số nguyên tố dương trong danh sách là:", positions)
