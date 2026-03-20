# Taking input from user
arr = list(map(int, input("Enter elements (0, 1, 2 only): ").split()))

# Dutch National Flag Algorithm
low = 0
mid = 0
high = len(arr) - 1

while mid <= high:
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:  # arr[mid] == 2
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print("Sorted array:", arr)