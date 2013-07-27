def partition(lst):
	pivot = lst[0] # Choose pivot as first element
	k = 1
	for i in range(1, len(lst)):
		if lst[i] < pivot:
			lst[i], lst[k] = lst[k], lst[i]
			k += 1
	lst[k - 1], lst[0] = lst[0], lst[k - 1]
	return (lst[:k - 1], [pivot], lst[k:])

def quicksort(lst):
	if len(lst) < 2:
		return lst
	else:
		result = partition(lst)
		return quicksort(result[0]) + result[1] + quicksort(result[2])

input_string = input()
input_list = [int(i) for i in input_string.split()]
print(quicksort(input_list))