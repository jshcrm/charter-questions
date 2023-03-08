def is_even(value: int) -> bool:
    return value % 2 == 0

def sum_of_even_integers(integers: list) -> int:
    return sum([x for x in integers if is_even(x)])


integers = [1, 2, 3, 4, 5, 6]

print(sum_of_even_integers(integers))
