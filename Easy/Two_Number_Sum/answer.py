def twoNumberSum(array, targetSum):
    for x in array:
        for y in array:
            if x == y:
                pass
            elif x + y == targetSum:
                return [x, y]
            else:
                pass
    return []
