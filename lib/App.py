def first_repeated_value(list):
    # create a Set to keep track of the values we've seen
    number_set = set()
    # iterate over each element from the list
    for i in range (0, len(list)):
        print(list[i])
        # if we've already seen a value, we've found the duplicate!
        if list[i] in number_set:
            return list[i]
        # otherwise, add the value to our set
        number_set.add(list[i])
        print(number_set)
    # return None if we reach the end and haven't found our value
    return None

first_repeated_value([1,2,3,3,4,4])
# answer = first_repeated_value([1,2,3,4])
# print(f"the first repeated value is {answer}")

