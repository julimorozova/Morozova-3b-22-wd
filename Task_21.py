def concat_array(arr1, arr2):
    result = [*arr1, *arr2]
    return result


arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(concat_array(arr1, arr2))
