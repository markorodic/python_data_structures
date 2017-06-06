def bubblesort(array):
	for j in range(len(array)-1):
		for i in range(len(array)-1):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
	return array

# list = [7,4,2,3,1,6]
# print list
# print bubblesort(list)