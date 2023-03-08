def sort_string(value: str) -> str:
    list_value = list(value)
    list_value.sort()
    return "".join(list_value)

def is_anagram(value: str, compare: str) -> bool:
    return sort_string(value) == sort_string(compare)


value = "silent"
compare = "listen"

print(is_anagram(value, compare))
