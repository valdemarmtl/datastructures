def selection_sort(list_: list):
    count = len(list_)
    if count < 2:
        return
    for i in range(count-1):
        index = i
        for j in range(i+1, count):
            if list_[j] < list_[index]:
                index = j
        tmp = list_[i]
        list_[i] = list_[index]
        list_[index] = tmp


if __name__ == "__main__":
    list_of_elements = [3, 6, 1, 8, 4, 5]
    selection_sort(list_of_elements)
    print(list_of_elements)
