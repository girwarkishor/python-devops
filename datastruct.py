
k = [1,[2,[3,[4,5]]]]

# result = [1,2,3,4,5]

result = []
def flattenlist(n):
    for each_element in n:
        if str(type(each_element)) == "<class 'int'>":   #isinstance()
            result.append(each_element)
        elif str(type(each_element)) == "<class 'list'>":
            flattenlist(each_element)
    return

flattenlist(k)
print(result)