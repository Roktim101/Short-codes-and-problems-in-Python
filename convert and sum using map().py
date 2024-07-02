def convert_and_sum_mixed_list(mixed):

    numeric_values = list(map(float, mixed))    # Convert each element in the list to a float
    total_sum = sum(numeric_values)
    return numeric_values, total_sum


# Example usage
mixed = [1, "2", 3.0, "4"]
numeric_values, total_sum = convert_and_sum_mixed_list(mixed)

print("Numeric Values:", numeric_values)
print("Sum:", total_sum)



# another example of map()

mixed = [1, "two", 3.0, "four"]
joined_mixed = " | ".join(map(str, mixed))    # Convert each element in the list to a string
print(joined_mixed)

