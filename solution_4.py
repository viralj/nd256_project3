def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    try:
        _frequency = [0] * 3
        for num in input_list:
            _frequency[num] += 1
        new_list = []
        for i in range(3):
            new_list.extend([i] * _frequency[i])
        return new_list
    except Exception as e:
        print("Error => {}".format(e))
        return []


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
    print()


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])  # Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])  # Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])  # Pass
test_function([2, 1, 0, 2])  # Pass
test_function([0, 0, 0])  # Pass
test_function([0, 0, 3])  # Fail
