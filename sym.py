set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

result_method = set_a.symmetric_difference(set_b)

result_operator = set_a ^ set_b

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Symmetric Difference (Method): {result_method}")
print(f"Symmetric Difference (Operator): {result_operator}")