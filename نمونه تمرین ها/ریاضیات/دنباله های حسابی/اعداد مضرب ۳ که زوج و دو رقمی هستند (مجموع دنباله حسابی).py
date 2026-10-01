odd_multiples_of_3 = [i for i in range(10, 100) if i % 3 == 0 and i % 2 != 0]

total_sum = sum(odd_multiples_of_3)

print(f"اعداد: {odd_multiples_of_3}")
print(f"مجموع: {total_sum}")
