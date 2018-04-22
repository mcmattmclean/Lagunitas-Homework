flatList = [1, 2, 3, 4, 5, 6]
bumpyList = [1, [2, 3], [4, [5, 6]]]
list2 = [[1,2],3,[[4,5],6],7]

def flattenList(listToFlatten):
    output = []
    for element in listToFlatten:
        if isinstance(element, list):
            output.extend(flattenList(element))
        else:
            output.append(element)
    return output

print("list before flatten: ")
print(list2)
print("list after flatten: ")
print(flattenList(list2))


