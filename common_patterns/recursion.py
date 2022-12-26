# Recursion: function that can call itself (recurse)
def tri_recurse(k):
    if (k > 0):
        result = k + tri_recurse(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\nRecursion Results")
tri_recurse(12)