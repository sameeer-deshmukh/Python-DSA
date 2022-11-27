def binary_search(numbers, target):
    """
    takes "sortred" list of numbers and a target and returns the index of target

    takes O(log n) time - "logarithmic time"
    since it reduces the list size to half on every comparison 
    """

    first = 0
    last = len(numbers)

    while (first <= last):
        midpoint = (first + last) // 2
        if (numbers[midpoint] == target):
            return midpoint
        elif (midpoint < target): 
            first = midpoint
        elif (midpoint > target):
            last = midpoint
        else: 
            return None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 3

result = binary_search(numbers, target)
print(result)

