# Take a passed list and recursively flatten it with the following cases:
# If the current element is a list, flatten it and extend the output list with it.
# If the current element is not a list, append it to the output list.
def flattenList(listToFlatten):
    output = []
    for element in listToFlatten:
        if isinstance(element, list):
            output.extend(flattenList(element))
        else:
            output.append(element)
    return output

bumpylist = [[1,2],3,[[4,5],6],7]

print("list before flatten: ")
print(bumpylist)
print("list after flatten: ")
print(flattenList(bumpylist))


