def running_sum(arr):
    result = []
    total = 0
    for num in arr:
        total += num
        result.append(total)
    return result

arr = [10, 60, 13, 44, 78]
print(running_sum(arr))  
