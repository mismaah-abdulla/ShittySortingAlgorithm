numbers = [6, 4, 8, 4, 2, 6, 2, 11, 23, 3, 1, 50, -3, 34, 24, 2, 0]
def sortArray(array):
    sortedArray = []
    highest = array[0]
    lowest = array[0]
    for i in range(len(array)):
        if array[i] >= highest:
            sortedArray.append(array[i])
            highest = array[i]
        elif array[i] <= lowest:
            sortedArray.insert(0, array[i])
            lowest = array[i]
        else:
            for j in range(len(sortedArray)):
                if array[i] <= sortedArray[j]:
                    sortedArray.insert(j, array[i])
                    break
    return sortedArray

print(numbers)
print(sortArray(numbers))
