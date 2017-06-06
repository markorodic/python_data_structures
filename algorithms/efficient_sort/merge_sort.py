def merge_sort(array):
	length = len(array)
	if length < 2:
		return

	mid = length/2

	l = array[:mid]
	u = array[mid:]

	merge_sort(l)
	merge_sort(u)
	res = merge(l, u, array)

	return res

def merge(lower, upper, array):
    nL = len(lower)
    nU = len(upper)

    i = j = k = 0
    
    while i < nL and j < nU:
        if lower[i] < upper[j]:
            array[k] = lower[i]
            i += 1
        else:
            array[k] = upper[j]
            j += 1
        k += 1

    while i < nL:
        array[k] = lower[i]
        i += 1
        k += 1

    while j < nU:
        array[k] = upper[j]
        j += 1
        k += 1
    return array

list = [1,4,2,8,6,3]
print list
print merge_sort(list)