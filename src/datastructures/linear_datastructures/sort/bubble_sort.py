def list_swap(list_: list, index_1: int, index_2: int):
    value_2 = list_.pop(index_2)
    list_.insert(index_1, value_2)


def bubble_sort(list_: list):
    count = len(list_)
    for i in range(count-1):
        print(list_)
        swapped = False
        for j in range(count-1):
            if list_[j] > list_[j+1]:
                list_swap(list_, j, j+1)
                swapped = True
        if not swapped:
            break
    print(list_)


if __name__ == "__main__":
    list_of_elements = [40, 30, 10, 50, 20]
    bubble_sort(list_of_elements)
