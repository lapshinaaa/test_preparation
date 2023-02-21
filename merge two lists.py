def merging_lists(list1: list, list2: list) -> list:
    merged = []
    #   to iterate over the given lists
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1

        elif list1[i] >= list2[j]:
            merged.append(list2[j])
            j += 1

    if i < len(list1):
        merged += list1[i:]

    elif j < len(list2):
        merged += list2[j:]

    return merged


list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

print(*merging_lists(list1, list2))
