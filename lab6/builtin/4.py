def all_true(t):
    return all(t)

my_tuple = (True, True, False, True)
result = all_true(my_tuple)
print(result)