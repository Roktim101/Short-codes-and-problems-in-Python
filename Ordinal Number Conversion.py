def ordinal_suffix(number):
    if 10 <= number % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(number % 10, "th")
    return str(number) + suffix

numbers = list(range(1, 101))

for number in numbers:
    print(ordinal_suffix(number), end=" ")
