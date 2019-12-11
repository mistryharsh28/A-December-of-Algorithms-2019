import random
# This algo will either take the odd onces out or even ones out


def the_decimation(array):
    # check if array sorted
    length = len(array)

    if length == 1:
        return array
    else:
        i = 0
        while(i != (length-1)):
            if(array[i + 1] >= array[i]):
                i = i + 1
            else:
                break

        if(i == length-1):
            return array

    # if not sorted
    even_or_odd_selection = random.randint(0,1)

    new_array = [value for index,value in enumerate(array) if index%2 == even_or_odd_selection]

    return the_decimation(new_array)


for _ in range(3):
    nums = list(range(10))
    k = random.choice(nums[1:])
    array = random.sample(nums, k=k)
    print(array)
    result = the_decimation(array)
    print('{} -> {}'.format(array, result))
