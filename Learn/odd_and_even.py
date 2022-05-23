print("\n" + "------------------------------------------------")

print("Determine odd and even numbers in a given range from 1 to n.")

count_even = 0
input = input("What is your number (n)?: ")
for number in range(1, int(input)):
    if number % 2 == 0:
        print(number)
        count_even += 1
print(f"We have {count_even} even numbers.")

print("\n" + "------------------------------------------------")

count_odd = 0
for number in range(1, int(input)):
    if number % 2 > 0:
        print(number)
        count_odd += 1
print(f"We have {count_odd} odd numbers.")

print("\n" + "------------------------------------------------")
