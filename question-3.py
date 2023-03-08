def integers_are_contiguous(value: int, compare: int) -> bool:
    return compare in [value + 1, value - 1]

def max_sum_of_contiguous_integers(integers: list[int]) -> int:
    sums_of_contiguous_groups = []
    current_group = []

    for index, x in enumerate(integers):
        if current_group == []:
            current_group.append(x)
            continue

        # Check if value is contiguous with the last value in current group
        if integers_are_contiguous(current_group[-1], x):
            current_group.append(x)

            # If this is the last item in our list and the group has more than 1 value add it to sums list
            if index == (len(integers) - 1) and len(current_group) > 1:
                sums_of_contiguous_groups.append(sum(current_group))

            continue

        # Values not contiguous - if our current group has more than 1 value in it, sum it and add to sums list
        if len(current_group) > 1:
            sums_of_contiguous_groups.append(sum(current_group))

        # Start a new group with the new value
        current_group = [x]

    return max(sums_of_contiguous_groups)


integers = [1, -2, 3, 4, -5, 6, 7]

print(max_sum_of_contiguous_integers(integers))
