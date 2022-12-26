new_list = [1, 2, 3]
result = new_list[1]  # 2
# err = new_list[4]  # IndexError

if 1 in new_list:  # essentially a linear search
    print(True)

# constant time (appending to end)
# "ammortized" constant space complexity
new_list.append(3)

# more time complexity (all subsequent items in list have to be shifted)
# o(n)
new_list.insert(0, -3)
new_list.pop(0)

# big O of O(K) where K represents new elements
new_list.extend([4, 5, 6])
print(new_list)
