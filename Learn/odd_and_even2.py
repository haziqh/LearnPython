count_even = 0
for number in range(1, 100):
    if number % 2 == 0:
        print(number)
        count_even += 1
print(f"We have {count_even} even numbers.")

count_odd = 0
for number in range(1, 100):
    if number % 2 > 0:
        print(number)
        count_odd += 1
print(f"We have {count_odd} odd numbers.")
