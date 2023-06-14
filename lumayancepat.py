print("Aulia Intan Prasasti")
import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

data = input("Masukkan angka-angka yang ingin diurutkan, pisahkan dengan spasi: ")
data = list(map(int, data.split()))

start_time = time.time()
bubble_sort(data)
end_time = time.time()
execution_time = end_time - start_time

print("Data Terurut:")
print(data)
print("Execution Time:", execution_time, "seconds")
