def solution(numbers, direction):
    if direction == "right":
        numbers.insert(0,numbers.pop())
    else:
        numbers.append(numbers.pop(0))
    return numbers

arr = [1, 2, 3]
print(solution(arr, "right"))