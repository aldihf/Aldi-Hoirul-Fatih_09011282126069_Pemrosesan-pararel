def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Contoh penggunaan
if _name_ == "_main_":
    # Contoh array yang akan diurutkan
    my_array = [64, 34, 25, 12, 22, 11, 90]

    print("Array sebelum diurutkan:", my_array)

    # Panggil fungsi bubble_sort
    bubble_sort(my_array)

    print("Array setelah diurutkan:", my_array)
