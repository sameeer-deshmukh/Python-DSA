def recursive_binary_search(numbers, target):
    if len(numbers) == 0:
        return False
    else: 
        midpoint = len(numbers) // 2
        if numbers[midpoint] == target:
            return True
        else:
            if numbers[midpoint] < target:
                return recursive_binary_search(numbers[midpoint+1:], target)
            elif numbers[midpoint] > target:
                return recursive_binary_search(numbers[:midpoint], target)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 1

result = recursive_binary_search(numbers, target)
print(result)