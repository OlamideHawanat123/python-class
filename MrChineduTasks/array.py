def find_median(first_list, second_list):
    first_list.sort()
    second_list.sort()

    combined_list = first_list + second_list
    count = len(combined_list)
    if count % 2 == 1:
        number = count / 2
        index = number + 1
        return combined_list[index]
    else:
        number = count // 2
        second_number = number + 1
        index = (number + second_number) / 2
        return index


print(find_median([1, 2, 3, 4], [5, 6, 7, 8]))


