# Function that returns max number out of the list passed to it
def find_max(arr):
    max = arr[0]
    for number in arr:
        if number > max:
            max = number
    return max
