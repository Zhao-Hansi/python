def delete_duplicate_number(list_origin):
    print(set(list_origin))


def delete_duplicate_number_and_keep_sort(lisy_origin):
    result_list = []
    for number in lisy_origin:
        if number not in result_list:
            result_list.append(number)
    print(result_list)


if __name__ == '__main__':
    list_origin = [1, 2, 4, 2, 4, 3, 3]
    delete_duplicate_number(list_origin)
    delete_duplicate_number_and_keep_sort(list_origin)
