list_of_elements = [8, 1, 6, 2, 4, 3]

def insertion_sort(list_: list):
	count = len(list_)
	if count < 2: return
	for i in range(1, count):
		key = list_[i]
		j = i-1
		while j >= 0 and key < list_[j]:
			list_[j+1] = list_[j]
			j -= 1
		list_[j+1] = key


insertion_sort(list_of_elements)
print(list_of_elements)