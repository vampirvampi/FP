def Summ_Not_Odd(list):
    if list == []:
        return 0
    else:
        if list[0] % 2 == 1:
            odd = list[0]
        else:
            odd = 0
        return odd + Summ_Not_Odd(list[1:])


def delete_elems(list, num):
    if len(list) == 1:
        if (list[0] < 0) & (list[0] > num):
            list.pop(0)
        return list
    else:
        if (list[0] < 0) & (list[0] > num):
            list.pop(0)
            return delete_elems(list, num)
        return delete_elems(list[1:], num)


def length(list):
    if list == []:
        return 0
    else:
        return 1 + length(list[1:])


def max_from_list(list, num):
    if len(list) == 1:
        if list[0] < num:
            return list[0]
    else:
        max = max_from_list(list[1:], num)
        if max == None:
            if list[0] < num:
                max = list[0]
        if list[0] < num & list[0] > max:
            return max
        else:
            return max


def mul_list(list, num, list2=None, prev=None):
    if list2 is None:
        list2 = []
    if (len(list) <= 1):
        return list2
    else:
        if (list[1] > num):
            if (prev == None):
                prev = list[1]
                return mul_list(list[2:], num, list2, prev)
            else:
                list2.append(prev * list[1])
                prev = list[1]
                return mul_list(list[2:], num, list2, prev)


def sort(list, cur, pr):
    if cur == len(list) - 1:
        pr = pr + 1
    elif list[cur] > list[cur + 1]:
        list[cur], list[cur + 1] = list[cur + 1], list[cur]
        sort(list, cur + 1, pr)
    elif list[cur] <= list[cur + 1]:
        sort(list, cur + 1, pr)
    if pr < len(list) - 1:
        sort(list, pr + 1, pr + 1)
    return list


if __name__ == '__main__':
    list2 = [-1, -2, 3, -5, 7, 12, 481, 42, -4, 6, 2, 11]
    list1 = [-1, 481, 42, -4, 6, 2, 11]
    list4 = [-1, -1, -1, -1, -1, -1, -1, -1, 0]

    print(Summ_Not_Odd([-1, 2, 3, 5, 7, 12]))
    delete_elems(list1, -3)
    print(list1)
    print(length(list1))
    print(max_from_list(list2, 16))
    list3 = mul_list(list2, -11)
    print(list3)
    print(sort(list3,0,0))
