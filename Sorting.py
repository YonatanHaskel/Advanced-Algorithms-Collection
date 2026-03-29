def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr1 = [33, 2, 87, 65, 4, 49, -11, 0, 196]
end1 = bubble_sort(arr1)
print(f'sorted array by bubble sort: {end1}')


def merge(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    if i == len(arr1):
        for k in range(j, len(arr2)):
            result.append(arr2[k])
    else:
        for l in range(i, len(arr1)):
            result.append(arr1[l])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    if arr is not None and len(arr) > 1:
        l_arr, r_arr = arr[:len(arr) // 2], arr[len(arr) // 2:]
        sorted_l_arr, sorted_r_arr = merge_sort(l_arr), merge_sort(r_arr)
        result = merge(sorted_l_arr, sorted_r_arr)
        return result


arr2 = [18, 2, 33, 45, 0, 4, 99, 64]
end2 = merge_sort(arr2)
print(f'sorted array by merge sort: {end2}')


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr


arr3 = [2, 5, 1, 8, 3, 7, 9, 6, 0, 4]
end3 = selection_sort(arr3)
print(f'sorted array by selection sort: {end3}')

import random as rd


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = rd.choice(arr)
    left, mid, right = [], [], []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            mid.append(x)
        else:
            right.append(x)
    sorted_arr = quick_sort(left) + mid + quick_sort(right)
    return sorted_arr


arr4 = [12, 3, 88, 45, 14, 97, 6, 55, 9, 1]
end4 = quick_sort(arr4)
print(f'sorted array by quick sort: {end4}')


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


arr5 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
end5 = insertion_sort(arr5)
print(f'sorted array by insertion sort: {end5}')


def counting_sort(arr):
    if arr is None:
        return arr
    count = [0] * (max(arr) + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    result = []
    for k in range(len(count)):
        result.extend([k] * count[k])
    return result


arr6 = [9, 2, 5, 3, 1, 2, 6]
end6 = counting_sort(arr6)
print(f'sorted array by counting sort: {end6}')


def coktail_shaker_sort(arr):
    if arr is None:
        return arr
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        for k in range(len(arr) - i - 2, i - 1, -1):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
    return arr


arr7 = [83, 42, 11, 67, 90, 2, 5, 13, 74, 21]
end7 = coktail_shaker_sort(arr7)
print(f'sorted array by coktail shaker sort: {end7}')


def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            while i >= gap and arr[i - gap] > arr[i]:
                arr[i], arr[i - gap] = arr[i - gap], arr[i]
                i -= gap
        gap //= 2
    return arr


arr8 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
end8 = shell_sort(arr8)
print(f'sorted array by shell sort: {end8}')


def gnome_sort(arr):
    i = 0
    while i < len(arr):
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr


arr9 = [20, 17, 14, 11, 8, 5, 2, -1]
end9 = gnome_sort(arr9)
print(f'sorted array by gnome sort: {end9}')


def tim_sort(arr, run):
    for i in range(0, len(arr), run):
        arr[i:min(i + run, len(arr))] = insertion_sort(arr[i:min(i + run, len(arr))])
    while run < len(arr):
        i = 0
        while i < len(arr):
            if i + run < len(arr):
                arr[i:min(i + run * 2, len(arr))] = merge(arr[i:i + run], arr[i + run: min(i + run * 2, len(arr))])
            i += run * 2
        run *= 2
    return arr


arr10 = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0, -11, -22, -33, -44, -55, -66]
end10 = tim_sort(arr10, 4)
print(f'sorted array by tim sort: {end10}')


def heapify(arr, n, i):
    largest = i
    left, right = i * 2 + 1, i * 2 + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


arr11 = [4, 1, 3, 2, 6, 5]
end11 = heap_sort(arr11)
print(f'sorted array by heap sort: {end11}')


def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]
    for x in arr:
        if x == max(arr):
            index = len(arr) - 1
        else:
            index = int((x - min(arr)) / (max(arr) - min(arr) or 1) * (len(arr) - 1))
        buckets[index].append(x)
    result = []
    for b in buckets:
        insertion_sort(b)
        result.extend(b)
    return result


arr12 = [98, 2, 13, -49, 56, 1, 76, -34, 26, 12]
end12 = bucket_sort(arr12)
print(f'sorted array by bucket sort: {end12}')