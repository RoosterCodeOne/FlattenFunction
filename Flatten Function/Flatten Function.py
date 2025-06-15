def flatten(lst):
    result = []
    for num in lst:
        if type(num) is list:
            got_it = flatten(num)
            result.extend(got_it)
        else:
            result.append(num)
    return result

"""
print(f"REGULAR FLATTEN: {flatten([1, [2, 3], [4, [5]]])}")

crazy_nested = [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[1]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

print(f"CRAZY NESTED: {flatten(crazy_nested)}")

test_case = [1, [2, [3, [4, [5, [6, [7, 8, [9, [10]]]]]]]], 11]

print(f"TEST_CASE: {flatten(test_case)}")
"""

