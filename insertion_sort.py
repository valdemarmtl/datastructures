list_of_elements = [8, 1, 6, 2, 4, 3]

def insertion_sort(list_: list)
	count = len(list_)
	if count < 2: return
	for i in range(1, count-1)
		tmp = list_.pop(i)
		j = i-1
		while tmp <= list_[j]:
			j--
			if j == 0: break
		list_.insert(j,tmp)

insertion_sort(list_of_elements)
print(list_of_elements)