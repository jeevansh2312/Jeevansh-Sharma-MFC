
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
while True:
    ch = input("How you doin', You wanna sort (Y/N): ")
    if ch in "Yy" :
        arr = eval(input("Enter the array for sorting: "))
        i= int(input("Enter 1 for bubble sort, 2 for insertion sort, and 3 for merge sort: "))
        if i == 1:
            print(bubble_sort(arr))
        elif i == 2:
            print(insertion_sort(arr))
        elif i == 3:
            print(merge_sort(arr))
        else:
            print("Invalid Input, please try again")
    else:
        break

